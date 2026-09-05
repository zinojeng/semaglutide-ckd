# Claude Code 跨 Session 協作手冊

適用版本：Claude Code `2.1.260`。目標是讓多個具名角色保留各自脈絡，同時以獨立 Git worktree 安全交付可稽核成果。

## 核心規則

- 一個角色、一個唯一 session 名稱、一個唯一 branch 與手動建立的 worktree。
- 所有 worktree 都從已核對的明確 commit SHA 建立；需要精確基準時，不使用 `claude --worktree` 的隱含基準。
- 在手動 worktree 內用 `--bg` 與 `--name` 啟動；不要設定 `bgIsolation:none`，也不要讓兩個寫作者共用同一工作目錄。
- prompt 必須列出角色、波次、可讀來源、唯一可寫路徑、禁止事項、交付格式與停止條件。
- prompt、訊息、log、commit 都不得包含 API key、token 或其他密鑰。MCP 應自行讀取既有安全設定。
- 只有狀態為 done 或已 `stop` 的 session 才可 `--resume`。session 忙碌時，不要 resume。

## 1. 從明確 SHA 建立隔離工作區

先把下列 `<...>` 全部替換為非機密值，再逐行執行：

```bash
REPO="<ABSOLUTE_REPO_PATH>"
BASE_SHA="<VERIFIED_40_CHAR_COMMIT_SHA>"
ROLE="<role>"
WAVE="<wave>"
RUN_ID="<unique_run_id>"
BRANCH="codex/<project>-${ROLE}-${WAVE}-${RUN_ID}"
WORKTREE="$REPO/.claude/worktrees/<project>-${ROLE}-${WAVE}-${RUN_ID}"

git -C "$REPO" show --no-patch --oneline "$BASE_SHA"
git -C "$REPO" worktree add -b "$BRANCH" "$WORKTREE" "$BASE_SHA"
git -C "$WORKTREE" rev-parse HEAD
git -C "$REPO" worktree list --porcelain
```

最後兩項輸出必須證明 worktree 位於預期路徑，且 `HEAD` 等於 `BASE_SHA`。若 branch 或路徑已存在，換新的 `RUN_ID`；不要重用活躍 worktree。

## 2. 啟動具名持久角色

```bash
cd "$WORKTREE"
claude --bg \
  --name "<project>-${ROLE}-${WAVE}-${RUN_ID}" \
  --effort high \
  --permission-mode acceptEdits \
  --add-dir "<AUTHORIZED_READ_ONLY_SOURCE_DIR>" \
  "Read <ABSOLUTE_PROMPT_FILE> completely. Work only in the named role and wave. Write only <EXACT_OUTPUT_PATHS>. Do not expose secrets, change settings, push, or edit forbidden paths. Commit only the authorized outputs when validation passes."
```

記錄啟動輸出的短 ID，並從 registry 記錄完整 session UUID、名稱、worktree、branch、基準 SHA、permission mode、角色與波次。不要把 registry 的瞬時狀態當成角色身分；完整 UUID 才是跨波次的持久識別。

## 3. 監看與控制

```bash
SHORT_ID="<SHORT_ID>"
claude agents --json
claude agents --json --all
claude logs "$SHORT_ID"
claude attach "$SHORT_ID"
claude stop "$SHORT_ID"
```

- `agents --json` 用於目前活躍 session；需要查完成狀態時加 `--all`。
- `logs` 是非互動式快照；`attach` 是進入該 session；`stop` 會保留可恢復的對話。
- 狀態不明時，先查 registry 與 log。不得因沒有新 log 就假定完成。

## 4. 忙碌 Session 的跨角色對話

目標 session 還在 working/busy 時，由目前運作中的 Claude coordinator 在 session 內呼叫 `ListAgents`，解析精確的名稱、UUID 與 worktree，再以 `SendMessage` 傳遞。不要對忙碌 session 執行 `--resume`；Claude Code 可能改為建立副本，使角色歷史分岔。

同一協作群組盡量使用相容的 permission mode。已驗證的限制是：permission-mode 類別不一致時，`SendMessage` 可能被 hold 等待核准，最後過期；此時必須記為「attempted, not delivered」，不可宣稱對方已收到。可改用指定的 durable handoff 檔案，並讓接收者在下一個可用 turn 明確讀取及回覆。

所有實質爭議使用下列三段式路由：

```text
CHALLENGE <ISSUE_ID>
Claim: <challenged claim>
Evidence/locator: <source ID and exact locator>
Risk: <why it matters>
Requested disposition: <accept, revise, quarantine, or investigate>
Owner: <recipient role>
```

```text
RESPONSE <ISSUE_ID>
Decision: <accept, revise, reject, or unresolved>
Evidence/locator: <supporting source and exact locator>
Replacement wording: <canonical wording, if revised>
Files affected: <paths>
Residual uncertainty: <explicit uncertainty>
```

```text
CLOSED <ISSUE_ID>
Disposition: <accepted, corrected, quarantined, or deferred>
Canonical wording/evidence: <final form>
Applied in: <commit and paths>
Closed by: <director role>
```

只有收到 `RESPONSE` 且 director 核對來源與實際 diff 後，才能發出 `CLOSED`。訊息 ID、delivery 狀態與回覆應寫入 session log。

## 5. 延續已完成或已停止的角色

先確認 session 不在 running/working/busy，再以完整 UUID 延續：

```bash
claude agents --json --all
cd "<THE_ROLE_WORKTREE>"
claude --bg --resume "<FULL_SESSION_UUID>" \
  "Continue as the same role for <NEXT_WAVE>. Read <HANDOFF_PATH>. Write only <EXACT_OUTPUT_PATHS>. Preserve all evidence and rights guardrails."
```

恢復後再次檢查 registry，確認沒有意外產生第二個角色副本。若原 session 仍忙碌，改走 `ListAgents`／`SendMessage`，或先明確 `stop` 再 resume。

## 6. 來源權利與雲端解析閘門

任何 PDF 上傳到 LlamaParse 或其他 cloud parser 前，都必須完成：

1. 核對 DOI、題名、版本與正式來源，排除錯檔。
2. 記錄取得路徑、access status、license／授權依據與檢查日期。
3. 僅允許 open-access、publisher-authorized、institution/user-authorized 或其他明確合法路徑；restricted、條款不明或僅因可登入取得者，一律停止雲端上傳並改採本機閱讀或 metadata-only。
4. 解析產物保存在 ignored cache；除非有再散布權，不把全文或完整解析內容 commit 到公開 repo。
5. 完成頁碼／表格／圖表 locator QA，並把 parser、輸入雜湊、來源與授權狀態寫入 acquisition ledger。

密鑰只能由已設定的 MCP 或安全 key file／environment 讀取；不得貼進 prompt、shell history、session message 或 Markdown。

## 7. 交付與整合檢查

每個角色完成前應執行：

```bash
OUTPUT_PATH="<AUTHORIZED_OUTPUT_PATH>"
git -C "$WORKTREE" status --short
git -C "$WORKTREE" diff --check
git -C "$WORKTREE" diff -- "$OUTPUT_PATH"
```

角色只 commit 授權路徑，不 push。整合者先核對基準、commit 清單、diff、引用 locator、權利紀錄與未解衝突，再於主工作區選擇性整合。停止 session 後，只有在 worktree 乾淨且 commit 已安全整合時，才進行 worktree／branch 清理。

## 最小稽核紀錄

每次啟動或延續至少記錄：角色、session 名稱與完整 UUID、短 ID、Claude 版本、時間區、worktree、branch、基準 SHA、permission mode、可寫範圍、實際檢查來源、commit、未解衝突、訊息 delivery 狀態，以及下一個接手角色。
