# 2026-09-09 新增全文：身分、邊界與權利稽核

**用途：** 公開、安全的來源 QA 紀錄；不是全文重製、解析檔發布或授權判定書。
**稽核單位：** 以收到的五個 Markdown 檔案為「artifact」，先用 SHA-256 鎖定版本，再判斷檔內真正的 article boundary。下列行號只對表列 SHA-256 的版本有效。

**獨立覆核：** 2026-09-09 由實際五個 artifact 重新計算全部 SHA-256，並以 NCBI PubMed／DOI metadata 另行核對文章題名與識別碼；雜湊與表列值逐一相符。錯抓檔的 DOI 對應 PMID 39504530–39504534，題名均為 *Frailty in Older Adults* correspondence／reply。

## 結論先行

- 五個檔案不等於五篇可直接引用的 semaglutide/CKD 論文：其中一檔是完全錯抓的 frailty correspondence；另兩檔是同一期雜誌多篇 letters 被合併的 issue-level composite；NEJM 檔則把來函與作者回覆合在同一 artifact。
- 這批檔案位於既有 2026-09-07 post-FLOW 私人 cache／manifest 之外，**未納入既有 27-source cache**，也不得藉此把 cache 數量改寫為 32。
- 原始 Markdown 不屬於公開研究成品，**不得加入 public Git tracking**。公開庫只保留本稽核所需的最少 metadata、雜湊、短篇學術摘要與引用連結。
- 五檔均**不可整檔直接進入 RAG**：除了 rights gate 尚未成立，還有錯抓、跨文章污染、雙欄／表格錯位與 figure 資訊不完整等 evidence-integrity 風險。後續引用應先切出正確 evidence unit，再以 PubMed、DOI landing page 或獲授權的人工作業獨立核對。
- 本輪已發生一次性的隔離 `identity／article-boundary／claim QA`，並以本稽核公開揭露；這項事後稽核不構成 automated-processing authorization，也不允許將原始檔轉入可重複查詢的 AI／RAG、向量索引、批次解析或再散布流程。

## Artifact registry

| 收到的檔名 | 真正身分 | DOI / PMID | SHA-256 | 有效行範圍 | 判定 |
|---|---|---|---|---:|---|
| `Semaglutide for Chronic Kidney Disease in Type 2 Diabetes . LETTER.md` | *N Engl J Med* 2024 correspondence：讀者來函及 FLOW 作者回覆 | [10.1056/NEJMc2410532](https://doi.org/10.1056/NEJMc2410532)；[PMID 39504528](https://pubmed.ncbi.nlm.nih.gov/39504528/)、[PMID 39504529](https://pubmed.ncbi.nlm.nih.gov/39504529/) | `e75d31646973a4a040ff03804d900d5319c9f0681c8eb8540e3e9f3d5332d0a0` | 1–65 | **可作人工論證核對；不是兩個獨立全文 artifact。** 引用時須分清「來函主張」與「作者回覆」，不能把兩者合寫成同一作者結論。 |
| `Semaglutide for Chronic Kidney Disease in Type 2 Diabetes. Reply.md` | 實際內容為 *N Engl J Med*「Frailty in Older Adults」correspondence packet，非 FLOW／semaglutide | [10.1056/NEJMc2411327](https://doi.org/10.1056/NEJMc2411327)；PMID [39504530](https://pubmed.ncbi.nlm.nih.gov/39504530/)–[39504534](https://pubmed.ncbi.nlm.nih.gov/39504534/) | `086c01f63622163cf8f8133c508864d621e7d8334e73fdf8598ddaf2cd221f46` | 無；1–195 均非目標文獻 | **`EXCLUDE_WRONG_ARTICLE`：身分錯抓，永久排除。** 不可因檔名含 `Reply` 就引用為 FLOW 作者回覆，也不得進 semaglutide/CKD 索引。 |
| `Semaglutide and kidney function.. direct kidney protection or an artifact.md` | *Kidney International* 2025;107:359–360，Ayoub、Wong、Glassock 來函 | [10.1016/j.kint.2024.11.003](https://doi.org/10.1016/j.kint.2024.11.003)；[PMID 39566843](https://pubmed.ncbi.nlm.nih.gov/39566843/) | `32139b7eefe216f1fb91deeeb224e54a70d02733f00ea48c52e7924a031ef471` | 37–71 | **issue-level composite，僅中段為目標。** 1–31 與 73–105 是其他 letters／頁尾內容，必須排除。 |
| `Response to the letter to the editor entitled ..Semaglutide and kidney function.. direct kidney protection or an artifact.md` | *Kidney International* 2025;108:948–950，FLOW 作者回覆 | [10.1016/j.kint.2025.07.008](https://doi.org/10.1016/j.kint.2025.07.008)；[PMID 41110891](https://pubmed.ncbi.nlm.nih.gov/41110891/) | `3b5b048c183d474923903f1575725bf444f8d9bfb4aac62a62a843021f6af77d` | 41–102 | **issue-level composite，邊界可切出但 figure parse 不完整。** 1–39 是 lupus nephritis 來函，不屬於 FLOW。 |
| `Glucagon-like peptide-1 receptor agonists to improve cardiorenal outcomes.. data from FLOW and beyond.md` | Faruque、Yau、Cherney，*Curr Opin Nephrol Hypertens* 2025;34:232–240，narrative review | [10.1097/MNH.0000000000001066](https://doi.org/10.1097/MNH.0000000000001066)；[PMID 40047207](https://pubmed.ncbi.nlm.nih.gov/40047207/) | `340aba811ff07d9138e7f2cadc414c293693337b2043101c62ad300497c986eb` | 1–416 | **身分正確，但僅能作二級來源與論點地圖。** 解析後表格與圖形不可直接當成經 QA 的數據來源。 |

## 解析與內容 QA

### 1. NEJM 來函／作者回覆合併檔

檔內先呈現讀者對背景用藥、依從性及外推性的質疑，後接 FLOW 作者回覆。作者回覆明確更正「試驗未使用 SGLT2 抑制劑」這項說法：基線已有 15.6% 使用，追蹤期間另有相近比例開始使用。這是論證鏈，不是新的隨機比較；公開文章應以「質疑—回覆—仍未解問題」三欄呈現，且不可把背景用藥 subgroup 解讀為 additivity 證明。

### 2. 假 semaglutide reply

檔名與內容完全不符。正文、DOI 與權利頁均指向 frailty correspondence，沒有可挽救的 FLOW 內容。這是典型的 filename-only identity failure；任何自動流程都必須在解析前用 title + DOI + PMID 三項 gate 驗身分。

### 3. Kidney International 質疑信

同一 Markdown 串接三篇不同 letters。目標內容只在 37–71 行，核心是質疑體重／體組成變化、肌酸酐生成及 BSA index 是否影響 eGFR slope 的解讀。此檔可支持「作者提出何種問題」，不能單獨支持 semaglutide 有或沒有直接腎臟機轉。

### 4. Kidney International 作者回覆

同一 Markdown 前段是完全無關的 lupus nephritis 來函。目標回覆在 41–102 行；第 68 行可直接辨識 1.16（95% CI 0.86–1.47）與「without BSA correction」1.04（0.71–1.37），證明乾淨 CI 不是由 Faruque 檔的破損字串回填。需要注意的是，原文仍替兩者印出 `/1.73m²/year`；公開綜述應如實保留分析標籤並標示 unit／index wording 待釐清，不得自行把第二項改標為絕對 GFR 單位。Figure 1 被解析成不完整的 number-at-risk table，並未保留可重製的曲線幾何。圖表若用於演講，應回看原始頁面／圖檔；若公開發布，使用自行重繪並清楚標示數據來源與重繪者，不可從這份 Markdown 截圖冒充原圖。

### 5. Faruque 等人 review

文章身分完整，但跨頁表格有欄位位移，且至少一處信賴區間字串出現格式錯誤（`0.86–0.1.47`）。文中以背景 SGLT2i subgroup 描述「independent／synergistic」，並在概念圖中把不同試驗、族群與 estimand 的 eGFR-slope 效果並列甚至加總；這些是 review 作者的推論框架，不是 factorial randomized evidence。任何數值、表格重繪或「四支柱可加成」主張都必須回到各 primary report／supplement 核對。

## Rights boundary

| Artifact | 檔內可見的權利訊息 | 本專案的處置界線 |
|---|---|---|
| 兩個 NEJM artifacts | personal use only；未經許可不得作其他使用；Massachusetts Medical Society 保留所有權利 | 可在合法存取條件下由獲授權讀者閱讀、做一般短篇學術筆記與正常引用；不得公開全文、截圖或解析檔，也不得在未確認 processing basis 前整檔送入雲端 parser、AI 或 RAG。 |
| 兩個 *Kidney International* composites | Elsevier／International Society of Nephrology 保留所有權利，且明列 text/data mining、AI training 與類似技術 | 視為 automated-processing basis 未建立的 rights-restricted derivatives；僅保留最少稽核紀錄，排除後續 AI/RAG／再解析。圖表重用須另查授權；公開版優先使用獨立重繪。 |
| Faruque 等 review | Wolters Kluwer Health 保留所有權利；檔內沒有可支持公開再散布或 TDM/ML 的肯定授權 | 作為獲授權人工閱讀的二級來源與 citation discovery；不發布全文／表格／圖形，不把本 Markdown 當成可再散布或可批次索引的資料集。 |

這些標示是依收到 artifact 中的 notice 做的保守 publication-control 判斷，不取代出版社最新條款、機構合約或法律意見。`內部學術演講` 可說明使用情境，但不會自動產生複製、TDM/ML、第三方上傳、錄影發布或 GitHub 再散布的權利。

## 可引用與不可引用的分界

可公開保留：bibliographic metadata、DOI／PMID、artifact SHA-256、article boundary、短篇自行撰寫的批判性摘要，以及經 primary source 獨立核對的數值。

不可公開保留：來源全文或大段原文、出版社表格／圖形截圖、可逆推出全文的結構化抽取、錯抓檔、rights-restricted parse，以及未通過欄位與圖形 QA 的數值轉錄。

## 後續 ingest gate

1. 先以 title + DOI + PMID 驗證身分，再判斷是否為 issue-level composite。
2. 以 SHA-256 固定 artifact 版本，所有行號、修正與排除範圍都綁定該雜湊。
3. 分別記錄 access basis、automated-processing basis、figure/table reuse basis 與 redistribution basis；四者不可互相代替。
4. 只有通過 article-boundary、rights、numeric、table/figure layout 四道 gate 的衍生資料，才可進入限定用途的研究索引；**本批五檔目前沒有任何一檔通過整檔 RAG gate。**
5. 研究文章引用時以 primary report／official human-readable page 為優先；review 僅用於定位爭點與追溯原始文獻。
