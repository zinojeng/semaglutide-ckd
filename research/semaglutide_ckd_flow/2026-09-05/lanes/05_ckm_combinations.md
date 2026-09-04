# Lane 05 — Cardio-kidney-metabolic（CKM）與合併治療證據備忘錄

**撰寫者角色：** flow-ckm（心腎代謝／合併治療專家）
**Wave：** 1（獨立研究）
**輸出範圍：** 依 brief `orchestration/prompts/05_ckm_combinations.md`
**證據截止日：** 2026-09-05
**狀態：** 完成初稿，等待 Wave 2 同儕覆核（endocrinology lane 將覆核本檔的 CKM 排序邏輯）

> 本備忘錄僅供跨 session 協作使用；正式的 07–16 號交付文件由 director/reconciler 撰寫。所有量化論斷均附來源代碼與定位（檔名＋段落/行號，或已驗證之網路來源＋驗證狀態）。

---

## 0. 來源代碼對照表（本檔案使用）

| 代碼 | 文獻 | 本地全文 | 驗證狀態 |
|---|---|---|---|
| `FLOW-PRIMARY-2024` | Perkovic V et al. NEJM 2024;391:109-121（FLOW 主報告）DOI 10.1056/NEJMoa2403347 | `fulltext/FLOW_primary_NEJM_2024_fulltext.md` | ✅ 本地全文核對 |
| `FLOW-SUPP-2024` | FLOW Supplementary Appendix | `fulltext/FLOW_supplement_fulltext.md` | ✅ 本地全文核對 |
| `FLOW-SGLT2-2024` | Mann JFE et al. Nat Med 2024;30:2849-2856 DOI 10.1038/s41591-024-03133-0 | `fulltext/glp1_cardiorenal_Mann_2024.md` | ✅ 本地全文核對 |
| `FLOW-MRA-2025` | Rossing P et al. Diabetes Care 2025 DOI 10.2337/dc25-0472 PMID 40730031 | `fulltext/glp1_cardiorenal_Rossing_2025.md` | ✅ 本地全文核對（Europe PMC 開放全文） |
| `FLOW-CVSEVERITY-2025` | Mahaffey KW et al. Eur Heart J 2025;46:1096-1108 DOI 10.1093/eurheartj/ehae613 PMID 39211948 | `fulltext/glp1_cardiorenal_Mahaffey_2025.md` | ✅ 本地全文核對 |
| `COMBO-MODEL-NEUEN-2024` | Neuen BL et al. Circulation 2024;149:450-462 DOI 10.1161/CIRCULATIONAHA.123.067584 PMID 37952217 | `fulltext/glp1_cardiorenal_Neuen_2024.md` | ✅ 本地全文核對（壽命模擬，非 RCT） |
| `REVIEW-SAWAMI-2024` | Sawami K et al. Cardiovasc Diabetol 2024;23:410 DOI 10.1186/s12933-024-02500-y PMID 39548500 | `fulltext/glp1_cardiorenal_Sawami_2024.md` | ✅ 本地全文核對（敘述性回顧，證據等級最低，僅作背景脈絡） |
| `FLOW-HF-2024` | Pratley RE et al. JACC 2024 DOI 10.1016/j.jacc.2024.08.004 PMID 39217553 | 無本地全文 | ⚠️ 未取得全文；數字經 WebSearch 由多個獨立二手摘要（ACC.org、PubMed 摘要）交叉核對，**未直接引用原文文字** |
| `FLOW-CVPHENOTYPE-2026` | JACC 2026 DOI 10.1016/j.jacc.2026.02.5125 PMID 42233552（FLOW CV 亞群：ASCVD／HF／PREVENT≥20%） | 無本地全文 | ⚠️ 未取得全文；數字經 WebSearch 由 ACC.org 臨床摘要、TCTMD、PubMed 摘要交叉核對，**未直接引用原文文字**，需 librarian 補全文驗證 |
| `AMPLITUDE-O-SGLT2-2022` | Lam CSP et al. Circulation 2022;145:565-574 DOI 10.1161/CIRCULATIONAHA.121.057934 | 無本地全文；於 `FLOW-SGLT2-2024` discussion 中被引用（ref 16） | ⚠️ 書目記錄經 WebSearch 核對存在且正確；分子為 **efpeglenatide**（非 semaglutide），僅作間接證據 |
| `REG-FDA-OZEMPIC-2026` | FDA OZEMPIC 仿單，Indications and Usage（DailyMed setid adec4fd2-6858-4c99-91d4-531f5f2a2d79） | 無本地全文 | ✅ 官方 DailyMed 全文擷取成功，標籤修訂日期 2026-05 |
| `REG-EMA-OZEMPIC-2024` | EMA CHMP 2024-12 正面意見，Ozempic SmPC 腎臟適應症更新 | 無本地全文 | ⚠️ 核准事實（日期、適應症擴充方向）經多家獨立新聞源交叉核對；**未取得 EMA SmPC 官方 PDF 逐字文字**（fetch 被擋） |
| `REG-TFDA-OZEMPIC-2026` | 台灣衛福部食藥署「胰妥讚」仿單，許可證字號衛部菌疫輸字第001107號 | 無本地全文 | ✅ 官方仿單查詢平台（mcp.fda.gov.tw）擷取成功，修訂日期 2026-01-26 |
| `GUIDE-KDIGO-2026-DRAFT` | KDIGO 2026 Diabetes and CKD Guideline Update — Public Review Draft（2026-03） | 無本地全文 | ⚠️ **僅為公眾意見徵詢草案**；PDF 直接擷取失敗（binary），內容以 kdigo.org 官網公告與 Guideline Central 摘要交叉核對，**未逐字引用**——見第 5 節警示 |
| `GUIDE-ADA-2026` | ADA Standards of Care in Diabetes—2026, Ch.11 Chronic Kidney Disease and Risk Management, Diabetes Care 2026;49(Suppl.1):S246 | 無本地全文 | ⚠️ 原文（diabetesjournals.org）擷取被拒（403）；內容以二手摘要（Pharmacy Times、DiabetesOnTheNet）交叉核對，**確切建議編號（11.7b／9.10-9.11）與逐字文字未驗證** |
| `GUIDE-CKM-2026` | 2026 AHA/ACC/ADA/ASN CKM Syndrome Guideline, JACC DOI 10.1016/j.jacc.2026.03.056（2026-06-09 發布） | 無本地全文 | ⚠️ 發布事實已確認（多獨立來源、正式 DOI）；**排序/疊加建議之逐字文字未取得**（原文擷取被拒） |
| `GUIDE-KDIGO-2022` / `GUIDE-KDIGO-2024` | KDIGO 2022 / 2024 Diabetes-CKD guideline（背景描述） | 無本地全文，本 session 未重新核對原文 | ⚠️ 依 master prompt 既有描述與一般已知內容做背景陳述，**本 session 未獨立重新擷取原文核對**，逐字文字不應被引用 |

---

## 1. Baseline vs. post-randomization SGLT2i：為何「無交互作用」不等於「證明相加療效」

### 1.1 FLOW 的實際數字（`FLOW-SGLT2-2024`）

FLOW 為 SGLT2i 基線使用（baseline，非隨機分派）預先設定（prespecified）之亞組分析：

- 基線有服用 SGLT2i：n=550（15.6%）（semaglutide 277／placebo 273）
- 基線未服用 SGLT2i：n=2,983（semaglutide 1,490／placebo 1,493）
- 主要結果（五項複合終點）：
  - SGLT2i 使用者：41/277（14.8%）vs 38/273（13.9%），**HR 1.07（95% CI 0.69–1.67）P=0.755**
  - 非使用者：290/1,490（19.5%）vs 372/1,493（24.9%），**HR 0.73（95% CI 0.63–0.85）P<0.001**
  - **P for interaction = 0.109**（`FLOW-SGLT2-2024`, l.36-48, l.117-126）
- 腎臟特異性四項複合終點（排除 CV death）：SGLT2i 亞組 HR 1.18（95% CI 0.71–1.98）P=0.532；非 SGLT2i 亞組 HR 0.75（95% CI 0.61–0.90）P=0.003（`FLOW-SGLT2-2024`, l.64-69）
- Total eGFR slope 治療組間差：SGLT2i 亞組 0.75 mL/min/1.73m²/年（95% CI −0.01, 1.50）；非 SGLT2i 亞組 1.25（95% CI 0.91, 1.58）；**P interaction = 0.237**（`FLOW-SGLT2-2024`, l.41-43, l.77-84）
- Cystatin C 為基礎之 eGFR slope 差異：SGLT2i 亞組 0.92（95% CI 0.16, 1.68）；非 SGLT2i 亞組 1.55（95% CI 1.21, 1.88）；P interaction 值於 Table 1 為 0.901（cystatin C 分析）、0.686（creatinine 分析）（`FLOW-SGLT2-2024`, l.412-450）
- MACE：P interaction 0.741；all-cause death：P interaction 0.901（`FLOW-SGLT2-2024`, l.86-97）
- UACR week-104 下降：SGLT2i 亞組 24%（95% CI 4–39%）；非 SGLT2i 亞組 34%（95% CI 26–40%）；P interaction 0.279（`FLOW-SGLT2-2024`, l.100-103）

### 1.2 為何統計上無法把這些數字讀成「相加療效已被證實」

1. **檢定力（power）問題是結構性的，不是可忽略的細節。** SGLT2i 亞組僅 550 人、主要終點僅 79 例事件（41+38），95% CI 寬達 0.69–1.67，橫跨 1（無效線）遠且不對稱。FLOW 整體試驗是以約 854 例主要終點事件為目標設計 90% power（`FLOW-MRA-2025` Statistical Analysis 段, l.57），此檢定力設計是針對「整體族群 vs. placebo」，**並未針對 SGLT2i 亞組交互作用檢定做樣本數估算**。`FLOW-SGLT2-2024` 作者本身在 Discussion 明白寫道："power was limited due to the low use of SGLT2i at trial entry"、"the power for testing interactions was low"（`FLOW-SGLT2-2024`, l.462-464, l.480-482）。
2. **未達統計顯著的交互作用 P 值（P=0.109 / 0.237 / 0.741 / 0.901）是「未能拒絕虛無假設（無異質性）」，不是「證明虛無假設為真（效果相同或相加）」。** 在低檢定力亞組下，這個區分尤其重要——CLAUDE.md 規則 5 明確要求不可把「無顯著交互作用」讀成「證明同等或相加療效」。
3. **基線 SGLT2i 使用本身並非隨機分派變項。** SGLT2i 使用者與非使用者在基線特徵上有系統性差異（較年輕、女性比例較低、eGFR 較高、收縮壓較低；`FLOW-SGLT2-2024` l.97-98），即使在各亞組內 semaglutide vs. placebo 仍是隨機化比較，但「SGLT2i 亞組」本身的異質性使得跨亞組比較（interaction test）的解釋力弱於真正的析因設計（factorial design）試驗。
4. **試驗期間治療暴露會「污染」原始亞組定義，且污染方向不對稱，傾向使亞組差異更難被偵測（bias toward the null for detecting heterogeneity）。** 未於基線服用 SGLT2i 者，試驗期間新啟用 SGLT2i 的比例在 placebo 組明顯高於 semaglutide 組（約 18 個月時 placebo ~10% vs semaglutide ~5%；36 個月時 placebo ~20% vs semaglutide ~10%；`FLOW-SGLT2-2024` l.109-114）。這代表：（a）"未使用 SGLT2i" 這個比較組隨時間持續「稀釋」，越到後期越不是真正的 SGLT2i-naive 族群；（b）placebo 組較高的 SGLT2i 加藥率，理論上會壓低 placebo 組事件率、使 semaglutide 相對效果看起來變小——即差異被低估而非高估；（c）此為未隨機分派之治療起始（treatment-by-indication confounding），time-dependent Cox 模型結果（HR 0.75，95% CI 0.65–0.86；`FLOW-SGLT2-2024` l.126-129）僅可視為 hypothesis-generating，不能等同隨機化比較。
5. **試驗追蹤期（中位 3.4 年）對「合併用藥的腎臟終點」而言可能過短。** `FLOW-SGLT2-2024` Discussion 明白指出：腎病事件（約 24 個月時累積約 5%）發生較 MACE（約 12 個月時累積約 5%）慢，"a trial duration of 3.4 median years may be too short to examine kidney outcomes...of combined drug use within the relatively small cohort of 550 participants"（`FLOW-SGLT2-2024` l.484-493）。
6. **eGFR slope 與 UACR 方向上是一致的（semaglutide 在有／無 SGLT2i 下均顯著優於 placebo），這是"未觀察到有害交互作用、方向一致"的支持性證據，但仍不能外推為"相加之硬終點療效已獲證實"。** `FLOW-SGLT2-2024` 作者自己的措辭是"suggest benefits of semaglutide are observed irrespective of SGLT2i use"（l.463-464），並非"additive benefit is established"。

### 1.3 間接證據：AMPLITUDE-O 與 SMART-C（非 semaglutide 直接證據）

- `AMPLITUDE-O-SGLT2-2022`（efpeglenatide vs placebo，SGLT2i 亞組 n=618/15.2%）：整體 MACE 之交互作用 P 值約 0.68（跨多個二手摘要交叉核對一致），提示 GLP-1RA 效益不因 SGLT2i 使用而改變；但 `FLOW-SGLT2-2024` Discussion 另指出該試驗個別終點（albuminuria、heart failure 獲較大效益；MI/stroke 效益被稀釋）存在方向不一致的訊號（`FLOW-SGLT2-2024` l.474-480，引用 ref 16）。**分子不同（efpeglenatide 非上市藥物、非 semaglutide），僅可作類別層級間接證據，不可直接外推至 semaglutide+SGLT2i。**
- SMART-C（SGLT2 Inhibitor Meta-Analysis Cardio-Renal Trialists Consortium）：`FLOW-MRA-2025` Discussion 引用（ref 30）指出 SGLT2i 之效益「regardless of baseline use of GLP-1RA」（`FLOW-MRA-2025` l.251）。**此為引用自二手討論段落，本 session 未獨立取得 SMART-C 原始論文核對**，且其邏輯方向與本節相反（是 SGLT2i 效益不受 GLP-1RA 影響，而非 semaglutide 效益不受 SGLT2i 影響的獨立驗證）。

### 1.4 小結（可用措辭）

> 現有 FLOW 資料**支持**"semaglutide 加在 SGLT2i 之上，沒有明顯有害交互作用訊號，eGFR slope 與 UACR 效益方向一致地保留"；**不支持**"semaglutide 加在 SGLT2i 之上被隨機證據證實可再降低硬腎臟終點"這一更強的因果聲明。這是 statistical power 不足加上未隨機分派亞組定義、加上不對稱之試驗中用藥起始所共同造成的結構性限制,而非單純測量誤差。

---

## 2. FLOW 的 MRA 亞組：能／不能推論到 finerenone 什麼

### 2.1 FLOW 的實際數字（`FLOW-MRA-2025`）

- 基線 MRA 使用：n=257（7.3%），其中 **spironolactone 218 例（84.8%）、eplerenone 38 例（14.8%）、esaxerenone 1 例（0.4%）、finerenone 0 例**（`FLOW-MRA-2025` l.75）。原文明確說明：finerenone「於 2021 年 7 月首次核准，且在 FLOW 收案期結束後才上市」（FLOW 收案 2019/6–2021/5）。
- 主要腎臟複合終點：MRA 使用者 23/136（16.9%）vs 36/121（29.8%），**HR 0.51（95% CI 0.30–0.86）P=0.012**；非使用者 308/1,631（18.9%）vs 374/1,645（22.7%），**HR 0.79（95% CI 0.68–0.92）P=0.002；P interaction = 0.12**（`FLOW-MRA-2025` l.205）
- 3 年絕對風險差與 NNT：MRA 使用者 ARD −0.11（95% CI −0.20, −0.01），**NNT 9**；非使用者 ARD −0.04（95% CI −0.07, −0.02），**NNT 23**（`FLOW-MRA-2025` l.205）——注意此為 exploratory 亞組層級 NNT，非整體試驗 NNT。
- 四項腎臟特異性複合終點（排除 CV death）：MRA 使用者 HR 0.38（95% CI 0.15–0.84）；非使用者 HR 0.82（95% CI 0.68–0.99）；**P interaction = 0.068**（`FLOW-MRA-2025` l.211-213）
- Renal replacement therapy 單一組件：MRA 使用者 HR 0.18（95% CI 0.03–0.71，僅 11 例事件）；非使用者 HR 0.91（95% CI 0.68–1.23）；**P interaction = 0.027**（唯一達統計顯著之交互作用，但事件數極少）（`FLOW-MRA-2025` l.205）
- eGFR slope（creatinine 基礎）差異：MRA 使用者 1.38 mL/min/1.73m²/年（95% CI 0.21–2.54）；非使用者 1.15（95% CI 0.83–1.46）；P interaction 0.71（`FLOW-MRA-2025` l.225）
- MACE、全因死亡：P interaction 分別為 0.75、0.89（`FLOW-MRA-2025` l.233-235）
- 安全性：hyperkalemia（>5.5 mEq/L）於 MRA 使用者 22.1% (sema) vs 19.0% (placebo)，非使用者 13.6% vs 17.6%，P interaction 0.12（`FLOW-MRA-2025` l.241）——**無跡象顯示 semaglutide 加重 MRA 相關高血鉀風險**，但此為 exploratory、事件數有限。

### 2.2 明確的推論邊界

1. **這是「semaglutide ± 類固醇型 MRA（主要 spironolactone）」的亞組分析，不是「semaglutide + finerenone」的直接證據。** Finerenone 為非類固醇型（nonsteroidal）MRA，藥理學（MR 選擇性、組織分布、心腎纖維化相關基因調控作用）與 spironolactone/eplerenone 不同，且已有其自身的大型硬終點 RCT 證據基礎（FIDELIO-DKD、FIGARO-DKD/FIDELITY），不能假設同一類（MRA）內部效果可直接互換外推。這是 CLAUDE.md 規則 6 明文禁止的推論。
2. **數字上 MRA 使用者的相對效果（HR 0.51）優於非使用者（HR 0.79），但 P interaction = 0.12（未達顯著），且此為 exploratory 亞組（該研究本身在 Limitations 明確標註 "This analysis should be considered exploratory"；`FLOW-MRA-2025` l.255）。** 259 例使用者中僅 59 例主要終點事件，信賴區間寬，`FLOW-MRA-2025` 原作者自己的措辭是「numerically greater reduction」、「numbers were small, so further large-scale studies are required」（l.247），並非宣稱已證實 additive effect。**本備忘錄不採用該論文摘要中「add to the body of evidence regarding the additive treatment effect」（l.245 Conclusions）此一措辭作為結論性推論**，因其與同一論文 Discussion／Limitations 段落所述的檢定力限制不完全一致；紅隊／director 應留意此原文本身內部語氣落差。
3. **試驗中新啟用 MRA 的分析（113 例 semaglutide vs 160 例 placebo 新啟用任何 MRA，其中 finerenone 分別 22 例 vs 28 例；`FLOW-MRA-2025` l.217）為非隨機分派之post-hoc time-dependent分析（"can only be considered hypothesis generating"，原文 l.255）。** Finerenone 暴露總計僅 50 例（22+28），事件數過少，不足以單獨分析。
4. **可作為間接證據的是 FIDELITY 分析中的 GLP-1RA 亞組（944 GLP-1RA 使用者 vs 12,082 非使用者，於 finerenone 對照 placebo 的效果上無顯著交互作用；`FLOW-MRA-2025` l.247 引用 ref 24）。** 這是方向相反的間接證據——從 finerenone 試驗族群中看 GLP-1RA 背景用藥是否改變 finerenone 效果，而非 semaglutide 試驗中看 finerenone 背景用藥。**本 session 未獨立取得 FIDELITY GLP-1RA 亞組原始論文核對數字**，僅轉引自 `FLOW-MRA-2025` 討論段。
5. **無任何已完成之隨機對照試驗，將 semaglutide + finerenone 組合本身設計為受試臂進行硬終點檢定。** 若有正在進行中之相關試驗（如 semaglutide/finerenone 合併之機轉或替代終點試驗），需由 source librarian 於後續波次核實是否存在、進度與是否已有結果；本 session 未檢索到已完成、可引用之直接 RCT。

### 2.3 小結（可用措辭）

> FLOW 的 MRA 亞組分析顯示 semaglutide 效益在有／無基線 MRA（絕大多數為 spironolactone）下方向一致、無顯著交互作用（P=0.12），且無明顯有害之高血鉀交互訊號；**但由於 finerenone 於 FLOW 收案期間幾乎未被使用（基線 0 例、試驗中新啟用僅 22 例於 semaglutide 組），本分析不能作為 semaglutide + finerenone 具相加硬腎臟終點療效的證據。** 現有支持 semaglutide + finerenone 合併使用的論據，本質上是機轉互補的推論與間接（FIDELITY 中 GLP-1RA 背景亞組）證據，屬於 expert extrapolation／indirect evidence 等級，非 direct randomized evidence。

---

## 3. RASi + SGLT2i + semaglutide 三重療法，及四藥（+finerenone）疊加：直接、間接、外推證據分層

| 證據層級 | 內容 | 來源 | 評語 |
|---|---|---|---|
| **直接隨機證據** | 無。沒有已完成的 RCT 以「RASi+SGLT2i+semaglutide vs RASi+SGLT2i」或「四藥 vs 三藥」為隨機分派臂，針對硬腎臟/心血管終點做檢定。 | — | FLOW 本身的 SGLT2i 亞組是**基線用藥狀態**分層而非隨機分派合併治療；見第 1 節。 |
| **FLOW 內部間接證據** | RASi 幾乎為全體背景用藥（`FLOW-MRA-2025` Table 1：RAASi 95.2–95.3%），SGLT2i 基線 15.6%。因此 FLOW 主要結果（HR 0.76）本身即是在「幾乎全員 RASi ± 少數 SGLT2i」背景下的 semaglutide 效果，可視為「RASi+semaglutide」有直接隨機證據；「RASi+SGLT2i+semaglutide」僅在 550 人的亞組中有描述性（非設計用以檢定相加效益）資料。 | `FLOW-PRIMARY-2024`, `FLOW-SGLT2-2024` | 這是本次 CKM 分析中最重要的一點：**FLOW 的整體 HR 0.76 本來就已內含少數 SGLT2i 使用者**，不是純粹「RASi-only」對照下的效果。 |
| **跨試驗間接證據（不同分子）** | `AMPLITUDE-O-SGLT2-2022`（efpeglenatide + SGLT2i 亞組）：MACE/腎臟複合終點在 SGLT2i 使用與否下方向一致，P interaction 未達顯著。 | 見第 1.3 節 | 類別層級支持性證據，非 semaglutide 分子專屬。 |
| **跨試驗間接證據（meta-analysis）** | Badve 等 2025 GLP-1RA 心腎結果統合分析（11 trials, 85,373 participants；於 T2D 族群中複合腎臟結果 HR 0.82 [0.73–0.93]、kidney failure HR 0.84 [0.72–0.99]、MACE HR 0.87 [0.81–0.93]、全因死亡 HR 0.88 [0.83–0.93]）—— 引自 `FLOW-MRA-2025` Discussion（l.249），**本 session 未獨立取得 Badve 2025 原文核對**，僅為二手轉引之數字，master prompt 亦已將其列為需檢索之類別效應文獻（見 §VI）。 | 轉引自 `FLOW-MRA-2025` | 這是 GLP-1RA class-level 證據，不等於「semaglutide 加在 SGLT2i/RASi 之上」的相加效益證明；且此統合分析未針對「合併用藥狀態」做分層。 |
| **模型外推（非 RCT）** | `COMBO-MODEL-NEUEN-2024`：以 2 個 SGLT2i 試驗（CANVAS, CREDENCE）、2 個 nsMRA 試驗（FIDELIO-DKD, FIGARO-DKD）與 8 個 GLP-1RA 試驗之個別治療效果，用 actuarial life-table 方法「假設」三藥完全相加（或敏感度分析採 50% 相加）於同一批 CANVAS/CREDENCE 傳統治療組病人身上做壽命模擬。結果：MACE HR 0.65（95% CI 0.55–0.76）、3 年 ARR 4.4%（95% CI 3.0–5.7）、NNT 23（95% CI 18–33）；50 歲起始者 MACE 無事件存活延長 3.2 年（95% CI 2.1–4.3）；CKD progression 存活延長 5.5 年（95% CI 4.0–6.7）；50%相加假設下 MACE 存活延長降為 2.4 年（95% CI 1.1–3.5）。 | `COMBO-MODEL-NEUEN-2024` Abstract | **這是本檔案中最貼近「四藥/三藥疊加效益」量化描述的資料，但其本質是建立在「效果相加」這一未被驗證的統計假設上的壽命模擬（simulation），並非測量得到的隨機證據。** 且其 GLP-1RA 效果來自 8 個異質試驗（未必含 semaglutide 或 FLOW 族群），SGLT2i 資料來自 CANVAS/CREDENCE（非 EMPA-KIDNEY/DAPA-CKD），finerenone 資料來自 FIDELIO/FIGARO——並非把 FLOW 本身納入模型。使用時必須明確標示為「模擬估算」而非「試驗證實」。 |
| **敘述性回顧（最低證據等級，僅背景）** | `REVIEW-SAWAMI-2024`：綜述 GLP-1RA+SGLT2i、加上 finerenone 三聯之潛在互補機轉與現況，結論呼籲需要更多研究確定合適族群。 | `REVIEW-SAWAMI-2024` Abstract | 屬 expert review/perspective，非原始數據來源，本檔案僅引用其定位問題的方式，不引用其作為療效證據。 |

### 3.1 FLOW 主報告對排序議題的原文立場

`FLOW-PRIMARY-2024` Discussion 明確將 RASi、SGLT2i、以及「finerenone 之礦皮質素受體拮抗」三者稱為「guideline-directed medical therapies」，並將 semaglutide 定位為第四種可考慮**加入（consider...along with these other proven therapies）**的治療選項，而非取代：

> "Because three other guideline-directed medical therapies have been shown to have benefits in patients with type 2 diabetes and chronic kidney disease (RAS inhibition, SGLT2 inhibition, and mineralocorticoid-receptor antagonism with finerenone), clinicians and patients will need to consider the order and priority of use for semaglutide... Combination therapy is likely to be important in the future, and we found no clear heterogeneity of effect among patients receiving SGLT2 inhibitors at baseline as compared with those who were not, although the statistical power of this analysis was limited."（`FLOW-PRIMARY-2024`, l.978-1010）

同段亦明確承認限制：

> "the number of participants who were receiving these agents [SGLT2i/MRA] at baseline was modest, which limited our ability to assess the effects of combination therapy. The trial was also not powered to detect differences within and between important subgroups"（`FLOW-PRIMARY-2024`, l.1063-1067）

**這是 FLOW 主報告作者群自己的定調：semaglutide 是"可與其他三種已證實療法一併考慮"的第四選項，而非"已證實優於或可取代"，且明確承認合併療法檢定力不足。這段文字未使用"four pillars"一詞，而是列舉三種既有 guideline-directed therapies + semaglutide。**

### 3.2 「Four pillars」用語的來源與定位（重要 flag）

依 brief 指示，不可將"four pillars"一詞當作已由指引正式背書（guideline-endorsed），除非指引本身實際使用或明確操作化此詞。本 session 檢核結果：

- `FLOW-PRIMARY-2024`（NEJM 主報告）：**未使用**"four pillars"一詞；僅將 RASi/SGLT2i/finerenone-MRA 稱為既有之 guideline-directed medical therapies，semaglutide 為第四種待考慮選項。
- `FLOW-MRA-2025`（Rossing 2025，FLOW 試驗相關作者撰寫之次分析論文）：**明確使用**"fourth pillar"／"four pillars"描述（"supporting a fourth pillar in the management of CKD in addition to RAS inhibition, SGLT2 inhibition, and nonsteroidal MRAs"，l.37；"This supports the concept of four pillars for optimal management of CKD in T2D..."，l.251，並引用其自身文獻 ref 31 作為此概念的出處）。**這是試驗相關研究者於期刊論文（非官方指引）中使用的敘述性／倡議性語言，不是 KDIGO 或 ADA 官方指引文字。**
- `GUIDE-KDIGO-2026-DRAFT`：依二手摘要（Guideline Central、KDIGO 官網公告），該 2026 年 3 月公眾意見徵詢草案似乎採用「foundational therapy（SGLT2i+statin+RASi）+ additional risk-based therapy（nsMRA、GLP-1RA、抗血小板）」的框架敘述，語意上接近四要素模型，但**本 session 未能取得草案 PDF 原文逐字確認其是否直接使用"four pillars"一詞、或該框架的確切操作化條件（如起始順序、聯合起始條件）**。且此草案截至 2026-09-05 仍**僅為公眾意見徵詢版本**（意見徵詢期已於 2026-04-13 截止，本 session 未查得正式定案發布之確認日期）——**依 CLAUDE.md 規則 5 及 brief 要求，必須明確標示為草案，不得引用為已定案之指引建議**。
- ADA 2025/2026、2026 CKM 指引：本 session 未能獨立取得逐字原文確認是否使用"four pillars"字樣（見第 5 節之逐項 flag）。

**結論措辭：**"Four pillars"目前最明確可考據之出處，是 FLOW 試驗相關作者（如 Rossing 2025）在同儕審查論文中的敘述性用語，並得到 FLOW 主報告"三個既有療法+semaglutide"論述的間接呼應；**尚不能確認任何一份官方 KDIGO/ADA/CKM 指引已將"four pillars"作為正式操作化建議之標題或用語**——KDIGO 2026 草案可能正朝此方向發展，但草案狀態與未逐字驗證的內容,使此點必須留待 librarian／director 以官方原文複核後才能提升確定等級。

### 3.3 四藥全用（RASi+SGLT2i+finerenone+semaglutide）證據總結

無任何一層證據（直接、間接、模型外推）可支持"四藥全用已被隨機證據證實可疊加降低硬腎臟終點"此一強論斷。可負責任陳述的最高等級是：

> 機轉層面（不同降壓/血流動力學/抗發炎-抗纖維化路徑）與各別藥物之獨立 RCT 證據，加上模型式壽命模擬（`COMBO-MODEL-NEUEN-2024`，以完全相加或 50% 相加為假設）顯示四藥合併"理論上"可能帶來可觀的額外絕對風險下降與無事件存活延長；但**沒有一項已完成的隨機對照試驗直接測試四藥合併相對於三藥或更少藥物組合的硬終點效果**，FLOW 本身對此議題的貢獻僅限於一個檢定力不足、事件數稀少的基線用藥亞組描述。

---

## 4. HF、MACE、CV death、全因死亡：依 CKD 嚴重度與心血管表現型分層

### 4.1 依 CKD 嚴重度（`FLOW-CVSEVERITY-2025`，prespecified）

母族群：3,533 人，中位追蹤 3.4 年。KDIGO 風險分層：低/中風險 242（6.8%）、高風險 878（24.9%）、極高風險 2,412（68.3%）（`FLOW-CVSEVERITY-2025` l.37, l.104-107）。

- **CV death/MI/stroke 複合終點**（此處為 confirmatory secondary endpoint，非主要終點）：整體 HR 0.82（95% CI 0.68–0.98）P=0.03；依 eGFR（</≥60）、UACR（</≥300）、KDIGO 風險分層，**所有 P interaction > 0.13**，方向一致（`FLOW-CVSEVERITY-2025` l.38, l.114）。
- **全因死亡**：整體 HR 0.80（95% CI 0.67–0.95）P=0.01；依 eGFR P interaction=0.21，依 KDIGO 風險分層 P interaction=0.23，方向一致（`FLOW-CVSEVERITY-2025` l.120）。
- **唯一達統計顯著之交互作用——全因死亡依 UACR：P interaction = 0.01**；UACR≥300 mg/g：HR 0.70（95% CI 0.57–0.85，支持 semaglutide）；UACR<300 mg/g：HR 1.17（95% CI 0.83–1.65，數值上偏向較高死亡率但 CI 涵蓋 1）（`FLOW-CVSEVERITY-2025` l.38, l.120-123）。
- **非致死性 MI 依 eGFR 之交互作用亦達顯著：P interaction = 0.04**（eGFR<60 HR 0.94 [0.63–1.39] vs eGFR≥60 HR 0.28 [0.09–0.87]），但同時觀察到 semaglutide 組非致死性 stroke 數值上較多（63 vs 51 於 stroke；52 vs 64 於 MI）（`FLOW-CVSEVERITY-2025` l.117）。
- **作者自身對這兩個顯著交互作用的解讀（重要，須完整保留）：** "Of 15 interactions tested, two showed significant P-interaction <.05 ... The authors are not aware of biologically plausible mechanisms and, given the number of interactions tested without correction for multiplicity and opposite directions of effect, believe these are likely due to chance."（`FLOW-CVSEVERITY-2025` l.153）。**本備忘錄採用相同判斷：在 15 個交互作用檢定、未做多重比較校正的情況下，2 個 P<0.05 且方向不一致（一個利於高 UACR 死亡率下降、一個利於高 eGFR 之 MI 下降）的訊號，較可能是機會性發現（multiplicity），而非可推廣之效果調節因子（effect modifier）——但由於缺乏事前之多重比較校正計畫，此判斷本身也應標示為作者研判而非決定性排除。**
- **Absolute risk 與 NNT（Week 156, Aalen-Johansen 法）：** CV death/MI/stroke：ARR −0.02（95% CI −0.04, −0.002）P=.035，**NNT 45（95% CI 23–623）**；全因死亡：ARR −0.03（95% CI −0.05, −0.004）P=.019，**NNT 39（95% CI 21–238）**（`FLOW-CVSEVERITY-2025` l.128-130）。**注意信賴區間極寬（尤其 CV death/MI/stroke 之 NNT 上限達 623），使用時務必連同 CI 一併呈現，不可僅報單點估計。**

### 4.2 依心血管表現型（`FLOW-CVPHENOTYPE-2026`，⚠️ 二手來源交叉核對，未逐字驗證原文）

族群定義（依 WebSearch 交叉核對之摘要數字）：established ASCVD 1,198/3,533（33.9%）；HF 678/3,533（19.2%，與 `FLOW-PRIMARY-2024` baseline table 之 342+336=678 [19.2%] 完全吻合，`FLOW-PRIMARY-2024` l.226，內部一致性佳）；無既定 CVD 但 PREVENT 高風險 1,329/2,000（66.5%，僅計無 ASCVD/HF 之次族群）。

- 主要腎臟複合終點 HR：ASCVD 亞組 0.80、無 ASCVD 0.74；HF 亞組 0.67、無 HF 0.79；PREVENT≥20% 亞組 0.73、非高風險 0.73（各亞組方向一致，效果量接近）。
- 3 年 NNT（主要腎臟終點）：ASCVD 亞組 22、HF 亞組 13、PREVENT≥20% 亞組 17。
- 全因死亡 HR：ASCVD 0.82／無 ASCVD 0.78；HF 0.75／無 HF 0.81；高總 CVD 風險 0.71／非高風險 0.82。
- **此節數字之驗證等級低於第 4.1 節**：本 session 因原文（jacc.org）擷取被拒，僅能以 ACC.org 臨床摘要、TCTMD 新聞稿、PubMed 摘要三方交叉核對取得一致數字，**未取得信賴區間、P interaction 值、事件數等關鍵細節之逐字確認**。使用於正式交付文件前，**強烈建議 source librarian 於 Wave 2 補做原文全文取得與核對**。

### 4.3 心衰竭專屬結果（`FLOW-HF-2024`，⚠️ 同樣為二手來源交叉核對）

- HF 事件或 CV death 複合：HR 0.73（95% CI 0.62–0.87）P=0.0005
- HF 事件單獨：HR 0.73（95% CI 0.58–0.92）P=0.0068
- CV death 單獨（此分析脈絡下報告值）：HR 0.71（95% CI 0.56–0.89）
- HF 住院或需靜脈治療之緊急就診：HR 0.74（95% CI 0.58–0.94）P=0.0154（26% 風險降低之描述）
- HF 住院或需靜脈利尿劑之緊急就診：HR 0.76（95% CI 0.59–0.97）P=0.0248；semaglutide 117 例 first events（2.0/100 PY）vs placebo 149 例（2.6/100 PY）
- 基線 HF：semaglutide 組 342 例（19.4%）、placebo 組 336 例（19.0%）（此欄位已於 `FLOW-PRIMARY-2024` Table 1, l.226 本地核對一致）

**安全性資料交叉參照（`FLOW-PRIMARY-2024` Table 3, 本地核對）：** 嚴重不良事件—心衰竭：semaglutide 133/1767（7.5%）vs placebo 175/1766（9.9%）（`FLOW-PRIMARY-2024` l.1045）。此為安全性通報（AE）層級之心衰竭事件計數，**與 `FLOW-HF-2024` 之預先設定 HF 療效終點分析（adjudicated efficacy outcome）並非同一分析架構，兩者方向一致（均利於 semaglutide）但不可互相替代引用**。

### 4.4 CV/HF 結果對本 CKM 章節的意涵

1. semaglutide 對 CV death/MI/stroke、全因死亡、HF 事件的效益在幾乎所有依 CKD 嚴重度與心血管表現型定義之亞組中方向一致，**這支持"廣泛適用性"而非"僅限特定表現型"的定位**，但仍應以 NNT 及其寬 CI 呈現絕對效益隨風險分層而變化的幅度（例如 HF 亞組 NNT 13 vs ASCVD 亞組 NNT 22，此為預期中"基礎風險越高、絕對效益越大"的型態，而非效果調節之異質性證據）。
2. 唯二達統計顯著的交互作用（全因死亡依 UACR、非致死性 MI 依 eGFR）方向不一致、缺乏機轉解釋、且未經多重比較校正，**依 CLAUDE.md 規則 5 不應被解讀為「UACR 越低死亡效益越差」或「eGFR 越高 MI 效益越好」的確立效果調節因子**，僅可標示為 exploratory signal，並列入 12 號文件（證據缺口與爭議）供 director 決定是否需要更審慎之措辭。
3. HF 專屬與 CV 表現型分析的驗證等級低於 CKD 嚴重度分析（4.1 節），**應在最終文件中明確標示驗證等級差異**，並建議由 librarian 補齊原文。

---

## 5. 指引演進與現行法規狀態

### 5.1 KDIGO

- **KDIGO 2022 / 2024 Diabetes-CKD 指引**：依 master prompt 既有描述，KDIGO 2022 將 GLP-1RA 主要定位於 metformin/SGLT2i 之後用於血糖管理與心血管效益；KDIGO 2024 CKD 綜合指引之出版時間點大致早於 FLOW 結果發表。**本 session 未於本波次重新獨立擷取這兩份指引原文核對逐字文字**，此處僅作背景脈絡陳述，正式交付文件中的逐字引用應由持有原文之 lane（或 source librarian）核實後方可寫入 11 號文件。
- **KDIGO 2026 Diabetes and CKD Guideline Update — Public Review Draft（2026-03）：**
  - 狀態確認：kdigo.org 官方公告確認為 2026 年 3 月發布之公眾意見徵詢草案，意見徵詢期至 **2026-04-13** 截止；本 session 檢索至 2026-09-05 **未查得正式定案／最終發布之確認訊息**。**依 brief 要求「Never call... unless the actual guideline uses or clearly operationalizes it」以及 CLAUDE.md「若全文無法驗證，需明確聲明，不得將論斷提升至確立地位」，本檔案將此份文件全程標示為 DRAFT，不作為已定案指引引用。**
  - 內容範圍（依二手摘要）：更新聚焦於新 Chapter 1（定義／預防／風險評估）、Chapter 2（血糖監測）、Chapter 4（藥物治療整合），證據回顧涵蓋至 2025 年 7 月發表之研究，採用 GRADE 方法評估證據強度與建議等級。
  - 據稱內容方向（**未逐字驗證，僅供 librarian 後續核查參考**）：草案似朝「foundational therapy（SGLT2i + statin + RASi）＋ additional risk-based therapy（nsMRA、GLP-1RA、抗血小板）」的框架發展，且據稱新增 finerenone/nsMRA 之 1A 級建議（eGFR≥25 mL/min/1.73m²、血鉀正常、UACR≥30 mg/g、已達最大耐受劑量 RASi 時），並可能允許 SGLT2i 與 nsMRA 同時起始以降低高血鉀風險評估之複雜度；GLP-1RA 之定位（依二手摘要）延續為 T2D+CKD 血糖管理之建議藥物類別，並新增針對合併肥胖者優先使用 GLP-1RA 以促進體重下降之實務要點（practice point）。**這些描述性內容全部標示為未逐字驗證，不得在 07-16 號正式文件中以引號直接引用，僅可在明確標註"依草案二手摘要，待核實"的前提下作為背景陳述。**

### 5.2 ADA Standards of Care

- **ADA Standards of Care in Diabetes—2026, Chapter 11（Chronic Kidney Disease and Risk Management）**：已確認存在（Diabetes Care 2026;49[Suppl 1]:S246，PubMed ID 41358881），惟本 session 對 diabetesjournals.org 之原文擷取請求被伺服器拒絕（403），**未能取得確切建議編號（如 11.7b）與逐字建議文字**。依交叉比對之二手摘要，內容方向大致為：
  - 於 eGFR 20–60 mL/min/1.73m² 及/或有白蛋白尿之成人 T2D，建議使用具實證效益之 SGLT2i 或 GLP-1RA 以兼顧血糖管理、延緩 CKD 進展與降低心血管事件風險（不論 A1C 是否達標）；
  - 於 eGFR<30 mL/min/1.73m²（advanced CKD）之成人 T2D，因低血糖風險較低及心血管事件降低證據，GLP-1RA 為血糖管理之優先選項。
  - **此二點內容方向與 FLOW/SOUL 之族群定位大致相符，具合理性，但由於未能取得原文逐字確認建議編號與確切措辭，本檔案不將其作為可直接引用之指引原文，僅作方向性背景陳述，並列入待驗證清單（見 5.4 節）。**

### 5.3 2026 AHA/ACC/ADA/ASN CKM Syndrome Guideline

- **發布事實已確認**：2026-06-09 由 ACC/AHA/ADA/ASN 聯合發布首份 CKM（cardiovascular-kidney-metabolic syndrome）指引，正式發表於 JACC，DOI 10.1016/j.jacc.2026.03.056（另有 Circulation 版本 DOI 前綴 CIR.0000000000001453），此為多獨立來源（PubMed、AHA Professional Heart Daily、JACC 官方 DOI）交叉核對之硬事實，可信度高。
  - 大方向（依 TCTMD 報導引述該指引共同作者 Ndumele 之發言）：對 T2D+CKD 族群，指引提及 GLP-1RA、SGLT2i、finerenone（nsMRA）均為可同時改善代謝與降低心血管風險之有效療法，並建議以 PREVENT 方程式量化 10 年及 30 年 ASCVD/HF/總 CVD 風險以分層治療強度。
  - **本 session 未能取得該指引原文中針對 RASi+SGLT2i+finerenone+GLP-1RA 排序或疊加使用之逐字建議文字與其證據等級（Class of Recommendation / Level of Evidence）**（原文網頁擷取多次被拒）。**"four pillars"一詞未在本 session 檢索到的任何二手報導中被明確歸屬於此指引本身**（見第 3.2 節）。

### 5.4 現行法規狀態（FDA／EMA／台灣 TFDA）——需嚴格區分「法規適應症」vs「試驗收案條件」vs「指引建議」

| 項目 | 內容 | 核准/修訂日期 | 驗證狀態 |
|---|---|---|---|
| **FDA（美國）** | OZEMPIC 仿單 Indications and Usage 第三項（逐字）："to reduce the risk of sustained eGFR decline, end-stage kidney disease, and cardiovascular death in adults with type 2 diabetes mellitus and chronic kidney disease."（另兩項適應症為血糖控制之輔助治療、已建立心血管疾病者降低 MACE 風險） | 原始 CKD 適應症核准 2025-01-28；本 session 擷取之 DailyMed 標籤版本修訂日期為 **2026-05** | ✅ 官方 DailyMed 全文逐字擷取確認 |
| **EMA（歐盟）** | Ozempic SmPC 更新以納入降低腎臟疾病相關事件風險之適應症敘述 | CHMP 正面意見 2024-12（多獨立新聞源一致） | ⚠️ 核准事實確認，**SmPC 逐字文字未取得**（官方 PDF 擷取被拒） |
| **台灣 TFDA** | 「胰妥讚（Ozempic）」仿單適應症第三項（逐字，中文）："用於已有慢性腎臟病的第二型糖尿病病人時，可降低eGFR持續下降、進展至腎臟病末期或心血管疾病死亡之風險。" 許可證字號：衛部菌疫輸字第001107號 | 仿單最新變更日期：**2026-01-26** | ✅ 官方仿單查詢平台（mcp.fda.gov.tw）逐字擷取確認 |

**三地法規適應症文字實質一致（均對應 FLOW 主要複合終點之三個核心元素：eGFR 持續下降／ESKD／CV death），此為法規對 FLOW 主要終點之直接背書；但需明確強調三點區分：**

1. **法規適應症 ≠ FLOW 試驗收案條件。** FLOW 收案為 eGFR 25–75 mL/min/1.73m² 且 UACR 依 eGFR 分層 >100 或 >300 mg/g（`FLOW-MRA-2025` l.47）；法規適應症文字本身**未在核准文字中重述這些精確的 eGFR/UACR 收案界值**，即法規適應症的文字範圍（"adults with type 2 diabetes mellitus and chronic kidney disease"）在字面上寬於 FLOW 實際收案之精確族群定義，處方時仍應以試驗族群作為療效外推之主要依據。
2. **法規適應症 ≠ 指引建議之優先序（sequencing）。** 三地法規文字均只敘述"可降低...風險"之適應症，**未規定應在 RASi/SGLT2i/finerenone 之前、之後或同時使用**，排序問題屬於指引（KDIGO/ADA/CKM）與臨床判斷範疇，不屬於法規標籤內容。
3. **法規適應症 ≠ 合併療法之相加效益證明。** 法規核准是基於 FLOW 整體族群（多數僅合併 RASi、少數合併 SGLT2i、幾乎無 finerenone）之效果，**不代表法規機關已對"合併 SGLT2i"或"合併 finerenone"之相加效益做出正式評估或背書**。

---

## 6. 實務排序／疊加治療演算法（附證據等級與監測限制）

> 本演算法為根據以上證據分層所做之臨床操作化整理，非官方指引逐字引用；證據等級標示採 brief 建議之校準用語（established／strongly supported／suggestive／hypothesis-generating／unknown）。

### 6.1 起始原則

1. **RASi（已達最大耐受標籤劑量）為所有情境之基礎（established，來自數十年 RCT 證據與 FLOW/FIDELIO/FIGARO/CREDENCE/DAPA-CKD/EMPA-KIDNEY 之共同收案前提，非本檔案重新驗證範圍）。**
2. **SGLT2i：對 eGFR≥20（依各藥物標籤／FIDELITY 族群下限）合併白蛋白尿或 CKD 之 T2D，屬 established 之腎臟與心血管保護基礎治療**（CREDENCE/DAPA-CKD/EMPA-KIDNEY 等專屬腎臟終點試驗，非本檔案重新驗證範圍，僅作既有基礎陳述）。
3. **Semaglutide（GLP-1RA）：對 T2D 合併白蛋白尿性 CKD（eGFR 25–75、UACR>100–300 依分層），FLOW 提供 established 等級之硬腎臟終點、MACE、全因死亡降低證據**（`FLOW-PRIMARY-2024`），且此效益在已有 RASi±SGLT2i 背景下方向一致地保留（strongly supported 其"可疊加使用而不互相抵銷"，但**相加之硬終點量化幅度為 unknown／suggestive**，見第 1、3 節）。
4. **Finerenone/nsMRA：對持續性白蛋白尿（多數操作化為 UACR≥30–300 mg/g 依各建議版本）且血鉀正常、eGFR 通常≥25 者，屬 established 之腎臟與心血管保護治療（FIDELIO-DKD/FIGARO-DKD/FIDELITY，非本檔案重新驗證範圍）。與 semaglutide 併用之直接硬終點證據目前為 unknown（無 RCT），間接證據（FIDELITY 之 GLP-1RA 亞組、FLOW 之類固醇型 MRA 亞組）為 suggestive／hypothesis-generating。**

### 6.2 疊加順序建議（實務操作，非官方指引逐字）

- 順序本身**證據等級為 suggestive-to-hypothesis-generating**：現有資料不支持"必須依固定順序"的強論斷，KDIGO 2026 草案方向（未逐字驗證）似乎正朝"及早合併／同時起始"而非"依序升階"發展,但此為草案內容,不可作為定案依據。
- 實務上合理且有機轉/安全性依據的起始次序建議：
  1. 確診 T2D+CKD 且合併白蛋白尿 → 先確認/優化 RASi 至最大耐受劑量。
  2. RASi 穩定後，依 eGFR 是否符合標籤下限，加入 SGLT2i（血糖與腎臟保護基礎，較低之容積不足／DKA 風險需衛教）。
  3. 若持續白蛋白尿且血鉀、eGFR 條件允許，加入 finerenone/nsMRA（需監測血鉀）。
  4. 若血糖未達標、體重過重、有 ASCVD/HF 共病、或腎臟風險仍高（如 KDIGO 極高風險、UACR 持續升高），加入 semaglutide/GLP-1RA——**FLOW 資料支持此步驟不需等待"血糖未達標"才啟用**，因 FLOW 收案不要求 HbA1c 未達標（HbA1c ≤10% 即可收案），且 CKM 指引方向（未逐字驗證）似乎將 GLP-1RA 定位為可與 SGLT2i 同層級之心腎保護藥物而非僅血糖後線藥物。
  - **此順序非強制流程圖，臨床上四類藥物之間可依血鉀、腎功能、GI 耐受性、體重目標、心衰竭表現型等因素同時或近乎同時起始**，尤其在心血管高風險（既有 ASCVD/HF）或極高 KDIGO 風險族群，及早合併可能較符合"及早介入以累積更長無事件存活期"之邏輯（`COMBO-MODEL-NEUEN-2024` 模擬支持此方向，但為模型而非 RCT，見 3.3 節）。

### 6.3 監測限制（合併治療下需特別注意）

| 風險 | 相關藥物組合 | 監測重點 |
|---|---|---|
| 高血鉀 | RASi + finerenone/nsMRA（±MRA 類固醇型） | 起始前及起始後定期血鉀／eGFR 監測（依 FIDELIO/FIGARO 方案節奏）；FLOW MRA 亞組未見 semaglutide 加重高血鉀風險（P interaction 0.12，見 2.1 節），但屬 exploratory 資料 |
| 容積不足／腎前性 AKI | SGLT2i + semaglutide（尤其合併嘔吐/腹瀉、利尿劑、老年、衰弱） | 病假日規則（sick-day rules）衛教、脫水風險評估；`FLOW-CVSEVERITY-2025` 顯示 AKI/腎衰竭嚴重不良事件於各 KDIGO 風險分層 semaglutide 與 placebo 相近（見 4.1 節安全性數據），未見明顯過量訊號，但仍需個別化評估 |
| GI 不良反應疊加 | Semaglutide（單獨即有明顯 GI AE 負擔） | `FLOW-PRIMARY-2024` Table 3：嚴重不良事件-腸胃道 semaglutide 5.4% vs placebo 5.3%（本地核對, l.1049）；因 GI AE 導致永久停藥 semaglutide 高於 placebo（233 [13.2%] vs 211 [11.9%]，`FLOW-PRIMARY-2024` l.1038），且原文另指出因腸胃道疾病停藥之具體比較為 79 [4.5%] vs 20 [1.1%]（l.991-992，需與 Table 3 合併解讀）——起始劑量滴定與衛教為關鍵 |
| eGFR 快速下降之低估風險 | SGLT2i 起始初期之"acute dip"、semaglutide 之肌肉量下降對 creatinine-based eGFR 之影響 | 建議以 cystatin C-based eGFR 或追蹤 slope 而非單次數值判斷；`FLOW-SGLT2-2024` 之 cystatin C 分析與 creatinine 分析結果方向一致（見 1.1 節），支持效果非單純肌肉量流失之偽象，但此為 post hoc 分析 |
| 血糖過低 | Semaglutide/GLP-1RA + insulin 或 sulfonylurea，尤其晚期 CKD | 此為既有已知風險，本檔案不重複展開（屬安全性/晚期 CKD 專責 lane 範疇），僅於此提示合併治療情境下需同步檢視降血糖藥物調整 |

### 6.4 演算法使用限制聲明

本節演算法**綜合彙整**現有直接、間接與模型證據及法規/草案指引方向性資訊而成，非對任一官方指引之逐字重述，亦不構成病人個別化醫療建議（依 CLAUDE.md Safety 段落）。任何"建議同時起始"或"建議特定順序"之表述，證據等級最高僅達 suggestive，關鍵仍待 KDIGO 2026 定案版本、ADA 2026 原文、CKM 指引原文之逐字核實後由 director 於 13 號文件（臨床決策框架）定案。

---

## 7. 待驗證清單（交付 librarian／director／red-team）

以下項目本 session 因原文擷取受阻（403 或二進位 PDF 無法解析）而**僅能以二手來源交叉核對**，尚未達到可逐字引用之驗證等級，建議由 source librarian 於 Wave 2 或後續波次以其他管道（如機構訂閱存取、PMC 開放全文、官方 API）補齊：

1. `FLOW-HF-2024`（Pratley JACC 2024 心衰竭專屬分析）全文——第 4.3 節數字待逐字核對。
2. `FLOW-CVPHENOTYPE-2026`（JACC 2026 CV 表現型亞組分析，DOI 10.1016/j.jacc.2026.02.5125）全文——第 4.2 節數字待逐字核對，尤其信賴區間、P interaction 值、事件數。
3. `GUIDE-KDIGO-2026-DRAFT` 原文 PDF——第 5.1 節之"four pillars"框架、finerenone 1A 建議條件、GLP-1RA 定位之確切文字待核對；並需持續追蹤是否已於 2026-09-05 前後正式定案發布。
4. `GUIDE-ADA-2026`（Diabetes Care 2026;49[Suppl 1]:S246）原文——第 5.2 節建議編號（如 11.7b）與逐字文字待核對。
5. `GUIDE-CKM-2026`（JACC DOI 10.1016/j.jacc.2026.03.056）原文——第 5.3 節排序/疊加建議之逐字文字、Class of Recommendation/Level of Evidence 待核對。
6. `REG-EMA-OZEMPIC-2024`：EMA SmPC 官方 PDF 逐字適應症文字待核對（目前僅有核准事實與方向性描述）。
7. Badve 等 2025 GLP-1RA meta-analysis 原文（master prompt §VI 已列為必檢索文獻）——本檔案第 3 節數字為轉引自 `FLOW-MRA-2025` Discussion，未獨立核對。
8. FIDELITY GLP-1RA 亞組分析原文（`FLOW-MRA-2025` ref 24）——第 2.2 節第 4 點數字為轉引，未獨立核對。
9. SMART-C（SGLT2 Inhibitor Meta-Analysis Cardio-Renal Trialists Consortium）原文（`FLOW-MRA-2025` ref 30）——第 1.3 節數字為轉引，未獨立核對。

---

## 8. 本 lane 結論摘要（供 director 整合用）

1. **SGLT2i 併用：** 無有害交互作用訊號、eGFR slope/UACR 效益方向一致地保留，但因亞組檢定力不足與試驗中不對稱之 SGLT2i 加藥，"相加之硬終點療效"為 unknown，不可宣稱已證實（第 1 節）。
2. **MRA/finerenone 併用：** FLOW 之 MRA 亞組幾乎全為類固醇型 MRA（spironolactone/eplerenone），finerenone 暴露趨近於零；semaglutide+finerenone 合併之硬終點證據目前為 indirect/extrapolated，非 direct randomized evidence（第 2 節）。
3. **三重/四重疊加：** 無直接 RCT；最具體的量化"疊加效益"數字來自 `COMBO-MODEL-NEUEN-2024` 之壽命模擬（假設完全或 50% 相加），必須清楚標示為模型估算而非試驗證實（第 3 節）。
4. **CV/HF 結果：** 依 CKD 嚴重度之效益一致（`FLOW-CVSEVERITY-2025`，本地驗證），依心血管表現型之效益方向亦一致但驗證等級較低（`FLOW-CVPHENOTYPE-2026`／`FLOW-HF-2024`，待補全文）；僅有的顯著交互作用（UACR×死亡率、eGFR×MI）經作者自身判斷為機會性發現，不宜作效果調節因子解讀（第 4 節）。
5. **指引與法規：** FDA/EMA/台灣 TFDA 三地法規適應症文字實質一致並已逐字（FDA、TFDA）或事實（EMA）確認，但法規適應症不等於排序建議或相加效益證明；KDIGO 2026 仍為草案狀態，"four pillars"一詞目前最明確之出處是試驗相關作者之期刊論文（`FLOW-MRA-2025`），尚未在本 session 驗證之任一官方指引原文中逐字確認（第 5 節）。
6. **排序演算法：** 已提供，但明確標示為證據整理而非逐字指引重述，關鍵開放問題留待官方原文核實後定案（第 6 節）。

**下一個最需要本 lane 證據的 session：** director/reconciler（用於 07_SGLT2_COMBINATION_EVIDENCE.md、08_MRA_FINERENONE_COMBINATION_EVIDENCE.md、11_GUIDELINE_REGULATORY_EVOLUTION.md、13_CLINICAL_DECISION_FRAMEWORK.md）；以及 Wave 2 中將覆核本檔之 endocrinology lane（CKM 排序邏輯）與 source librarian（待驗證清單之原文補齊）。
