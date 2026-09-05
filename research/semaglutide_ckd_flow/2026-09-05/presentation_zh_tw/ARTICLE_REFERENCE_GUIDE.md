# 04｜五篇文章的投影片用 reference 快速索引（zh-TW）

> 用途：供主流程把本檔各節追加到 `articles_zh_tw/01` 至 `05` 的文末，或拆成投影片來源表與 speaker notes。內容只沿用 `14_MASTER_EVIDENCE_TABLE.md`、`16_FINAL_SYNTHESIS_ZH_TW.md`、`SOURCE_LEDGER.csv` 與五篇文章已核實資料。證據截止日為 2026-09-05。

## 已完成、可直接插入的公開視覺

下列素材已把 source ID、精確 locator 與推論限制放入圖面；完整圖說與 30 秒講稿見 [`VISUAL_ASSET_CATALOG_ZH_TW.md`](./VISUAL_ASSET_CATALOG_ZH_TW.md)。

| 文章／結果段 | 建議視覺 | 可直接使用檔案 | 最短 inline reference |
|---|---|---|---|
| 文章 01：五項 vs 四項、個別腎衰竭組成 | FLOW endpoint/component forest | [PNG](./public_assets/redrawn/01_flow_endpoints_forest_zh_tw@2x.png)／[SVG](./public_assets/redrawn/01_flow_endpoints_forest_zh_tw.svg) | `FLOW-PRIMARY-2024, Table 2, p.116` |
| 文章 01：eGFR early／chronic／total | eGFR 三階段圖 | [PNG](./public_assets/redrawn/02_flow_egfr_phases_zh_tw@2x.png)／[SVG](./public_assets/redrawn/02_flow_egfr_phases_zh_tw.svg) | `FLOW-PRIMARY-2024, Fig.1D/Table 2, pp.114,116,119–120` |
| 文章 02：基線 SGLT2i | 次族群 forest | [PNG](./public_assets/redrawn/03_flow_sglt2_subgroup_forest_zh_tw@2x.png)／[SVG](./public_assets/redrawn/03_flow_sglt2_subgroup_forest_zh_tw.svg) | `FLOW-SGLT2-2024, Figs.1–2/Table 1` |
| 文章 02：MRA／finerenone 邊界 | 次族群 forest | [PNG](./public_assets/redrawn/04_flow_mra_subgroup_forest_zh_tw@2x.png)／[SVG](./public_assets/redrawn/04_flow_mra_subgroup_forest_zh_tw.svg) | `FLOW-MRA-2025, Figs.1–2/Tables 1–2` |
| 文章 03：SELECT／SOUL／pooled | 分隔式脈絡圖 | [PNG](./public_assets/redrawn/05_select_soul_pooled_context_zh_tw@2x.png)／[SVG](./public_assets/redrawn/05_select_soul_pooled_context_zh_tw.svg) | `SELECT-KIDNEY-2024; SOUL-KIDNEY-2026; SELECT-FLOW-SOUL-POOLED-2026` |
| 文章 04：安全性與停藥 | paired dot plot | [PNG](./public_assets/redrawn/06_flow_safety_dotplot_zh_tw@2x.png)／[SVG](./public_assets/redrawn/06_flow_safety_dotplot_zh_tw.svg) | `FLOW-PRIMARY-2024, Table 3 p.120; FLOW-SUPPLEMENT-2024, S4–S5` |
| 文章 02：CKD 嚴重度下的 MACE | Mahaffey 原始 Figure 2 | [JPG](./public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg)／[署名](./public_assets/ATTRIBUTION.md) | `FLOW-CKDSEVERITY-2025, Fig.2 p.1103, CC BY 4.0` |
| 文章 03：SELECT kidney composite | SELECT 原始 Figure 1 | [PNG](./public_assets/source_figures/SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png)／[署名](./public_assets/source_figures/ATTRIBUTION.md) | `SELECT-KIDNEY-2024, Fig.1 p.2059, CC BY 4.0` |

## 使用與權利標記

- `NR`：目前證據庫未報告，或本案未取得可核實的原始 Table／Figure／頁碼。不得自行補值。
- `公開可重用原圖`：本案已核實為 CC BY 4.0。使用時仍須列作者、期刊、DOI、授權連結，若有裁切、標註或翻譯須註明修改，並另查圖中是否有第三方素材。
- `公開版重繪`：以本案已核實的數值製作可編輯表格／圖，頁腳引原始來源。不要把出版社版面、表格造型或 PDF 截圖放入公開 repo。
- `僅本機來源截圖`：可供演講準備時核對，但本案未確認可公開再散布。公開 GitHub 版本只留 source ID、locator、官方連結與重繪資料。
- `摘要層級`：只取得並核實 structured abstract。可重繪摘要明載的事實，不得暗示看過未取得的 Table／Figure；原圖 locator 標 `NR`。
- `官方文件短引`：仿單、指引與 protocol／SAP 採短篇幅轉述與官方連結，不重製頁面、流程圖或大段文字。FLOW protocol／SAP 帶有贊助者專有／保密文字，不進公開 repo。

建議每張數據投影片頁腳使用：`作者 et al. 期刊 年；Table/Figure/Results；DOI。` 若內容屬次族群、事後或未校正分析，在同一頁腳直接加上 `exploratory`、`post hoc` 或 `unadjusted for multiplicity`，不要只放在 speaker notes。

---

## 文章 01｜FLOW 設計、主要結果與 CV death

### 01-A｜FLOW 收案族群與背景治療

- **文章插入位置：**「FLOW 收了哪些病人」段後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`FLOW-SUPPLEMENT-2024`；`FLOW-PROTOCOL-2021`。
- **Exact locator：** `FLOW-PRIMARY-2024` Table 1，journal pp.112–113，本機 `FLOW.pdf` pp.4–5；`FLOW-SUPPLEMENT-2024` Eligibility Criteria，supplement pp.11–13；`FLOW-PROTOCOL-2021` synopsis pp.6–7。
- **投影片視覺：** 公開版重繪「兩條 eGFR／UACR 收案路徑」加右側基線特徵表。Table 1 原頁只作僅本機來源截圖。
- **一句圖說：** FLOW 聚焦 T2D 合併白蛋白尿性 CKD，平均 eGFR 47.0、UACR 中位數 567.6 mg/g，不能代表所有 CKD。
- **30 秒口述：** FLOW 不是一般糖尿病族群。eGFR 50 至 75 的病人要有 UACR 大於 300，eGFR 25 至低於 50 則要有 UACR 大於 100。約 95% 使用 ACEi 或 ARB，基線 SGLT2i 只有 15.6%，MRA 7.3%，且沒有 finerenone。
- **投影片頁腳短引：** Perkovic V, et al. *N Engl J Med*. 2024;391:109–121. Table 1. doi:10.1056/NEJMoa2403347；FLOW protocol v5.0, synopsis pp.6–7。
- **授權／公開限制：** NEJM 表格與 supplement 原頁不放公開 repo。Protocol 只短引，不重製。公開版本使用自製、可編輯的兩路徑圖。

### 01-B｜主要終點的五項組成

- **文章插入位置：**「主要終點不是純腎臟終點」段後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`FLOW-SUPPLEMENT-2024`。
- **Exact locator：** `FLOW-PRIMARY-2024` Methods，journal p.111／local PDF p.3；Table 2，journal p.116／local PDF p.8；`FLOW-SUPPLEMENT-2024` Table S2 註記，supplement PDF p.24。
- **投影片視覺：** 公開版重繪五項終點結構圖，將 CV death 用不同顏色框出。旁邊另列排除 CV death 的四項腎臟專屬複合終點。
- **一句圖說：** FLOW 的確認性主要終點包含 CV death，四項腎臟專屬複合終點則是支持性結果。
- **30 秒口述：** 頭條 HR 0.76 對應五項終點，包括持續 eGFR 下降至少 50%、持續 eGFR 低於 15、慢性 KRT、腎因性死亡與心血管死亡。排除心血管死亡後的 HR 0.79 位於確認性階層之外，必須和主要結果並列但不能升格。
- **投影片頁腳短引：** Perkovic V, et al. *N Engl J Med*. 2024;391:109–121. Methods p.111 and Table 2 p.116. doi:10.1056/NEJMoa2403347。
- **授權／公開限制：** 原表僅本機核對。公開版只重繪終點架構與已核實數值。

### 01-C｜主要結果與腎臟專屬結果成對呈現

- **文章插入位置：**「核心結果：應該成對報告」表後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`。
- **Exact locator：** Figure 1，journal pp.114–115，本機 PDF pp.6–7；Results「Primary Outcomes」journal p.115；Table 2，journal p.116，本機 PDF p.8。
- **投影片視覺：** 演講現場可在取得適當權利後引用 Figure 1 的累積發生率曲線。公開 repo 採兩列原創 forest／數據表：五項 HR 0.76（0.66–0.88）與四項 HR 0.79（0.66–0.94）。
- **一句圖說：** Semaglutide 降低含 CV death 的五項主要複合終點 24%，腎臟專屬四項結果提供方向一致但推論層級較低的支持。
- **30 秒口述：** 主要複合事件為 331 對 410，HR 0.76，三年 NNT 20。腎臟專屬事件為 218 對 260，HR 0.79，但未受確認性階層與多重比較保護。18.7% 與 23.2% 是未定時點粗比例，不能拿來重算三年 ARR 或 NNT。
- **投影片頁腳短引：** Perkovic V, et al. *N Engl J Med*. 2024;391:109–121. Figure 1 and Table 2. doi:10.1056/NEJMoa2403347。
- **授權／公開限制：** NEJM 原圖不進公開 repo。若無出版社許可，公開簡報也以可編輯重繪為優先。

### 01-D｜個別腎衰竭組成沒有獨立確認

- **文章插入位置：**「個別腎衰竭事件沒有被單獨證明」段後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`。
- **Exact locator：** Table 2，journal p.116，本機 PDF p.8；Discussion，journal pp.119–120。
- **投影片視覺：** 公開版重繪三列 component forest：持續 eGFR<15、慢性 KRT、腎因性死亡。每列加上「outside confirmatory hierarchy」標籤。
- **一句圖說：** KRT、持續 eGFR<15 與腎因性死亡均未被 FLOW 單獨確認，試驗證明的是包含這些事件的複合終點下降。
- **30 秒口述：** KRT 的 HR 0.84、持續 eGFR<15 的 HR 0.80，信賴區間都跨 1。腎因性死亡只有 5 對 5 例，HR 0.97。這些結果不能改寫成「透析下降 16%」或「腎衰竭下降 20%」，因為個別組成沒有足夠檢定力。
- **投影片頁腳短引：** Perkovic V, et al. *N Engl J Med*. 2024;391:109–121. Table 2 and Discussion, pp.116, 119–120. doi:10.1056/NEJMoa2403347。
- **授權／公開限制：** 公開版重繪，避免截取出版社 Table 2。

### 01-E｜eGFR 總斜率、急性期與慢性期

- **文章插入位置：**「eGFR 斜率提供另一條腎臟證據線」段後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`。
- **Exact locator：** Table 2 與 Results，journal p.116；Discussion，journal pp.119–120；本機 PDF p.8。
- **投影片視覺：** 可編輯三列 dumbbell／數據表，不憑空畫完整 eGFR 曲線。列出總斜率 −2.19 對 −3.36、0 至 12 週變化 −1.07 對 −1.05、12 週後慢性斜率 −2.36 對 −3.30。
- **一句圖說：** FLOW 的腎功能訊號主要來自慢性斜率分離；基線至第 12 週未見 semaglutide 專屬的差異性 acute dip，但不能排除更早且已消退的 transient dip。
- **30 秒口述：** 總斜率組間差為每年 +1.16。兩組前 12 週都下降約 1.06，組間差只有 −0.03；這只支持「至第 12 週沒有組間差異性 dip」，不是「完全沒有急性變化」。第 12 週後的慢性斜率差為 +0.94。這個形態支持較慢的長期 eGFR 流失，但不能排除更早 transient dip，也不能單靠軌跡指定唯一機轉。
- **投影片頁腳短引：** Perkovic V, et al. *N Engl J Med*. 2024;391:109–121. Table 2. doi:10.1056/NEJMoa2403347。
- **授權／公開限制：** 使用自製圖與原始數值。不要從缺少逐時點數值的來源擬合或數位化一條新曲線。

### 01-F｜提前終止與階層式檢定

- **文章插入位置：**「提前終止如何影響信心」段後。
- **穩定 source ID：** `FLOW-SAP-2023`；`FLOW-SUPPLEMENT-2024`。
- **Exact locator：** `FLOW-SAP-2023` §2.1 pp.6–7、§2.3.1 p.12、§2.4.1 pp.17–18；`FLOW-SUPPLEMENT-2024` Statistical Methods Relating to the Interim Analysis and Hierarchical Testing，supplement PDF pp.16–17。
- **投影片視覺：** 公開版自製時間線：854 計畫事件、約 570 事件期中分析、2023-10-10 DMC 建議、2024-02-06 lock、最終 741 事件、雙側門檻 0.0322。
- **一句圖說：** FLOW 越過預先設定的療效邊界而提前終止，主要分析已調整群組序貫設計，長期效應量仍需保留一般性的早停警語。
- **30 秒口述：** 試驗原計畫至少 854 件主要事件，期中分析在約三分之二資訊量進行。DMC 建議因療效停止，最終累積 741 件。主要終點使用群組序貫方法調整，三項確認性次要終點依階層通過，但沒有各自重新做群組序貫調整。
- **投影片頁腳短引：** FLOW SAP v3.0, §§2.1, 2.3.1, 2.4.1；FLOW Supplement, Statistical Methods, PDF pp.16–17。
- **授權／公開限制：** Protocol／SAP 僅短引與自製時間線。原文件、頁面截圖或衍生全文不公開。

---

## 文章 02｜SGLT2i、MRA、finerenone 與次族群

### 02-A｜基線 SGLT2i 次族群的主要與腎臟專屬結果

- **文章插入位置：**「已使用 SGLT2i」核心表後。
- **穩定 source ID：** `FLOW-SGLT2-2024`。
- **Exact locator：** Figure 1，Nat Med 2024;30:2849–2856，p.2851；Figure 2，p.2852；Results；Table 1，p.2853。
- **投影片視覺：** 可公開使用具完整歸屬的 CC BY 4.0 Figure 1，或重繪二乘二 forest。建議重繪以便把主要五項、腎臟專屬四項與 P-interaction 放在同一畫面。
- **一句圖說：** 基線 SGLT2i 使用者的估計不精確，五項（含 CV death）主要終點 P-interaction=0.109 並未證明效果相同，也未證明加成。
- **30 秒口述：** 基線使用者只有 550 人與 79 件主要事件。五項主要終點 HR 為 1.07 對 0.73，P-interaction 0.109。腎臟專屬終點 HR 為 1.18 對 0.75，P-interaction 0.100。寬信賴區間同時容許效益、無效與傷害。
- **投影片頁腳短引：** Mann JFE, et al. *Nat Med*. 2024;30:2849–2856. Figures 1–2. doi:10.1038/s41591-024-03133-0. CC BY 4.0。
- **授權／公開限制：** 本文與圖像的 CC BY 4.0 已核實。重用時保留歸屬、授權連結與修改說明，另查第三方 credit line。

### 02-B｜孤立的 ≥50% eGFR 下降交互作用

- **文章插入位置：** SGLT2i 表後的限制段。
- **穩定 source ID：** `FLOW-SGLT2-2024`。
- **Exact locator：** Figure 2，p.2852；Results。
- **投影片視覺：** 只用一列放大 forest，旁邊以醒目文字標 `nominal, unadjusted for multiplicity`。不要把這列做成整張投影片的勝負結論。
- **一句圖說：** 持續 eGFR 下降 ≥50% 的 P-interaction=0.023 是未校正的單一組成訊號，不足以證明 SGLT2i 使用者受害。
- **30 秒口述：** 使用者 HR 1.30，非使用者 HR 0.66，交互作用 P 值 0.023。這是多個終點與次族群中的孤立名目訊號，且使用者事件少。它應提出研究問題，不應推翻整體結果或成為停用組合的因果證據。
- **投影片頁腳短引：** Mann JFE, et al. *Nat Med*. 2024;30:2849–2856. Figure 2, p.2852. doi:10.1038/s41591-024-03133-0. Nominal interaction, multiplicity unadjusted。
- **授權／公開限制：** 同 02-A。若裁切原圖，註明裁切與標註均為修改。

### 02-C｜Cystatin-C 分析回答測量疑慮

- **文章插入位置：**「Cystatin-C 分析補的是測量疑慮」段後。
- **穩定 source ID：** `FLOW-SGLT2-2024`。
- **Exact locator：** Table 1，p.2853；Results；Extended Data Figures 4–7。
- **投影片視覺：** 公開版重繪三列 marker／endpoint-dependence 表，分別呈現修改五項終點、總 cystatin-C 斜率與第 104 週變化。標題不要寫「加成性證明」或把 0.74 畫成預設 1.07 的替代值。
- **一句圖說：** 在基線 SGLT2i 使用者中，預設 creatinine-based 五項 HR 1.07 與事後修改 cystatin-C HR 0.74 是不同 estimand；不可平均、拼成範圍或互相推翻，亦未回答加成性。
- **30 秒口述：** 事後修改的 cystatin-C 五項結果在使用者與非使用者分別為 0.74 與 0.70，交互作用 P 值 0.844；預設 creatinine-based 使用者估計則是 1.07。修改終點取消了確認性測量要求，且與預設分析使用不同標記／終點定義，因此兩者都不是可任選的唯一真值。它只能呈現 marker／endpoint dependence，不能升格為新的確認性或加成性結果。
- **投影片頁腳短引：** Mann JFE, et al. *Nat Med*. 2024;30:2849–2856. Table 1 and Extended Data Figures 4–7. doi:10.1038/s41591-024-03133-0. Post hoc analysis。
- **授權／公開限制：** CC BY 4.0，仍需歸屬與修改說明。

### 02-D｜MRA 次族群不是 finerenone 次族群

- **文章插入位置：**「MRA 次族群不是 finerenone 次族群」核心表後。
- **穩定 source ID：** `FLOW-MRA-2025`。
- **Exact locator：** Figure 1；Figure 2；Results；Supplementary Tables 1–2。Figure 1 顯示主要與腎臟專屬複合，Figure 2 顯示個別組成與 CV 結果。
- **投影片視覺：** 公開版重繪 MRA 使用者／非使用者 forest，頂端先放組成：spironolactone 218、eplerenone 38、esaxerenone 1、finerenone 0。
- **一句圖說：** FLOW 的 257 名 MRA 使用者幾乎全為類固醇型 MRA，不能把 HR 0.51 解讀為 semaglutide 與 finerenone 的直接組合效果。
- **30 秒口述：** 五項（含 CV death）主要終點在 MRA 使用者與非使用者的 HR 為 0.51 與 0.79，P-interaction 0.12。使用者只有 59 件主要事件。腎替代治療的 P-interaction 0.027 更只有 11 件使用者事件，屬未校正探索，不能證明加成或真實效應修飾。
- **投影片頁腳短引：** Rossing P, et al. *Diabetes Care*. 2025. Figures 1–2 and Supplementary Tables 1–2. doi:10.2337/dc25-0472. Exploratory subgroup interpretation。
- **授權／公開限制：** 本案未建立可把出版社原圖置入公開 repo 的改作授權。僅本機核對原圖，公開版重繪數值並連結 DOI。

### 02-E｜CKD 嚴重度與「未偵測到異質性」

- **文章插入位置：**「CKD 嚴重度」段後。
- **穩定 source ID：** `FLOW-CKDSEVERITY-2026-CJASN`；`FLOW-CKDSEVERITY-2025`。
- **Exact locator：** CJASN 2026 Figures 1、2、5 與 Results；Mahaffey et al. *Eur Heart J*. 2025;46:1096–1108，Figures 2–4，journal pp.1103–1106。
- **投影片視覺：** 可公開使用 CC BY 4.0 原圖並完整歸屬，或重繪兩張 forest。第一張呈現 eGFR／UACR 的主要終點 P-interaction .83／.42；第二張只作探索頁，呈現死亡率名目交互作用。
- **一句圖說：** 五項（含 CV death）主要終點未偵測到 CKD 嚴重度異質性，但低 UACR 與死亡率次族群仍不精確或屬事後探索。
- **30 秒口述：** UACR 低於 100 的 350 人是篩選後再分類，不是前瞻性低白蛋白尿世代，HR 0.70 的區間為 0.34 到 1.44。UACR 高低的死亡率交互作用與 UACR 至少 2,000 的死亡訊號未校正，不能承諾較大絕對效益。
- **投影片頁腳短引：** Tuttle KR, et al. *CJASN*. 2026;21:841–851. Figures 1, 2, 5. doi:10.2215/CJN.0000000974；Mahaffey KW, et al. *Eur Heart J*. 2025;46:1096–1108. Figures 2–4. doi:10.1093/eurheartj/ehae613. CC BY 4.0。
- **授權／公開限制：** 兩文 CC BY 4.0 已核實。Mahaffey 舊本機轉錄曾有數值錯置，只有 fresh official Europe PMC artifact 與出版 Figure 2 可作權威來源。

### 02-F｜跨試驗 comparator 只做脈絡，不排名

- **文章插入位置：**「為何 SGLT2i／finerenone 仍是重要 comparator」兩表後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`CREDENCE-2019`；`CREDENCE-EGFR-SLOPE-2020`；`DAPA-CKD-2020`；`DAPA-CKD-BASELINE-2020`；`EMPA-KIDNEY-2023`；`FIDELIO-DKD-2020`；`FIDELITY-POOLED-2022`。
- **Exact locator：** `14_MASTER_EVIDENCE_TABLE.md`「Contextual comparator trials」的 primary-source locator block；各原始來源的 Methods／Results、指定 Tables／Figures。各試驗可直接比較的統一 Table／Figure：`NR`。
- **投影片視覺：** 自製「終點定義與收案邊界」矩陣。不要以 HR 大小排序，也不要製作 league table。
- **一句圖說：** FLOW、CREDENCE、DAPA-CKD、EMPA-KIDNEY 與 FIDELIO／FIDELITY 的族群、終點與 eGFR acute phase 不同，HR 只能在各試驗內解讀。
- **30 秒口述：** 這張表的目的是回答每個試驗研究了誰、CV death 是否納入、腎衰竭如何定義、背景治療有多少。SGLT2i 的專屬 CKD 與 HF 證據涵蓋較廣，不代表可以把跨試驗 HR 直接排成藥物名次。
- **投影片頁腳短引：** Source IDs 與 DOI 依 `SOURCE_LEDGER.csv`；詳細 locator 見 `14_MASTER_EVIDENCE_TABLE.md`，Contextual comparator trials。
- **授權／公開限制：** 公開版只使用本案原創矩陣與數值短引，不拼貼各出版社原表。

---

## 文章 03｜SELECT、SOUL、類別效應與機轉

### 03-A｜FLOW、SELECT、SOUL 回答不同問題

- **文章插入位置：**「三個試驗，其實在問三個不同問題」表後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`SELECT-KIDNEY-2024`；`SOUL-PRIMARY-2025`；`SOUL-KIDNEY-2026`。
- **Exact locator：** FLOW Table 2，journal p.116；SELECT Table 1、Figures 1–5、Methods／Results；`SOUL-PRIMARY-2025` structured abstract；`SOUL-KIDNEY-2026` Results，journal p.259／local PDF p.4，Table 1，p.260／PDF p.5，Figure 2，p.261／PDF p.6，Figure 3，p.262／PDF p.7。
- **投影片視覺：** 自製三欄矩陣：族群、劑量／途徑、腎臟終點地位、估計值。三個 HR 不做排序箭頭。
- **一句圖說：** 三項試驗顯示方向可整合，但族群、劑量、途徑與腎臟終點地位不能視為等效。
- **30 秒口述：** FLOW 研究 T2D 與白蛋白尿性 CKD，使用 1.0 mg 皮下注射，腎臟與 CV death 複合是主要終點。SELECT 是無糖尿病的肥胖與 ASCVD，使用 2.4 mg。SOUL 是 14 mg 口服，MACE 之後的腎臟階層未通過。
- **投影片頁腳短引：** Perkovic V, et al. doi:10.1056/NEJMoa2403347；Colhoun HM, et al. doi:10.1038/s41591-024-03015-5；SOUL sources doi:10.1056/NEJMoa2501006 and 10.2337/dc25-1080。
- **授權／公開限制：** SELECT 為 CC BY 4.0。FLOW 原圖不公開。SOUL 的數值與表圖位置已用受限 PDF 核對，但該 PDF／解析檔與原表圖不得散布；公開版僅重繪已核實數值。

### 03-B｜SELECT 的硬終點邊界與連續結果

- **文章插入位置：**「SELECT」段後。
- **穩定 source ID：** `SELECT-KIDNEY-2024`；`SELECT-GLYCEMIA-2024`。
- **Exact locator：** SELECT kidney Table 1、Figures 1–5；Results；Methods「Correlation and mediation analysis」；PMCID PMC11271413。糖尿病前期比例見 `SELECT-GLYCEMIA-2024` PubMed structured abstract／Results。
- **投影片視覺：** 可公開使用 CC BY 4.0 的 Figure 1 或 Figures 4–5，建議另做可編輯兩層圖：上層腎臟複合 HR 0.78，下層第 104 週 eGFR、總斜率與 UACR。
- **一句圖說：** SELECT 支持無糖尿病診斷族群的腎臟訊號，但並非專屬非糖尿病 CKD 硬終點試驗。
- **30 秒口述：** 腎臟複合終點為 1.8% 對 2.2%，HR 0.78。它包含新發巨量白蛋白尿，排除該成分後未達顯著。只有約五分之一符合 eGFR 低於 60 或 UACR 至少 30，且 66.4% 為糖尿病前期，所以不能推論完全脫離代謝路徑。
- **投影片頁腳短引：** Colhoun HM, et al. *Nat Med*. 2024;30:2058–2066. Table 1 and Figures 1–5. doi:10.1038/s41591-024-03015-5. CC BY 4.0。
- **授權／公開限制：** CC BY 4.0，須歸屬與註明修改。Reporting Summary 尾段未全面 QA，不作投影片證據來源。

### 03-C｜SELECT 體重中介不能外推到硬腎臟終點

- **文章插入位置：** SELECT 段第 5 點後。
- **穩定 source ID：** `SELECT-KIDNEY-2024`。
- **Exact locator：** Methods「Correlation and mediation analysis」及相應 Results；Figures 4–5。中介模型只使用基線與第 104 週 eGFR 變化。
- **投影片視覺：** 自製「估計對象」框圖：體重變化對第 104 週 eGFR 變化，中介比例 81%（41–120%）。將 eGFR slope 與 hard composite 放在框外。
- **一句圖說：** SELECT 的 81% 體重中介估計只對應第 104 週 eGFR 變化，不能套到斜率或硬腎臟複合終點。
- **30 秒口述：** 81% 看起來很大，但信賴區間超過 100%，且模型只用兩個時間點。這不是 FLOW 中介分析，也沒有證明所有腎臟效益由體重造成。投影片要把估計對象寫在數字旁邊，避免聽眾記成一般性結論。
- **投影片頁腳短引：** Colhoun HM, et al. *Nat Med*. 2024;30:2058–2066. Correlation and mediation analysis. doi:10.1038/s41591-024-03015-5. CC BY 4.0。
- **授權／公開限制：** 公開版自製框圖。若引用原圖，遵循 CC BY 4.0 歸屬與修改標示。

### 03-D｜SOUL 階層失敗後的 eGFR 斜率

- **文章插入位置：**「SOUL」段後。
- **穩定 source ID：** `SOUL-PRIMARY-2025`；`SOUL-KIDNEY-2026`；`SOUL-PROTOCOL-2021`。
- **Exact locator：** `SOUL-PRIMARY-2025` PubMed structured abstract；`SOUL-KIDNEY-2026` Results，journal p.259／local PDF p.4，Table 1，p.260／PDF p.5，Figure 2，p.261／PDF p.6，Figure 3，p.262／PDF p.7；`SOUL-PROTOCOL-2021` pp.17–19 與 §10.3.2.1 p.50。
- **投影片視覺：** 自製階層圖。第一格五項腎臟／CV death HR 0.91，P=0.19；後續總 eGFR 斜率差 +0.40 標 `formally exploratory`。
- **一句圖說：** SOUL 的腎臟複合未達顯著，因此後續 eGFR 斜率即使名義 P<0.0001，也只能作探索性解讀。
- **30 秒口述：** SOUL 五項終點為 403 對 435，HR 0.91，P 0.19。四項腎臟專屬 HR 0.86，同樣未顯著。總斜率差 +0.40 的方向有利，但階層 gate 已停止。差異不能單獨歸因於口服途徑，因族群風險與事件率也不同。
- **投影片頁腳短引：** SOUL primary doi:10.1056/NEJMoa2501006；SOUL kidney doi:10.2337/dc25-1080. Structured abstracts, Results. eGFR slope formally exploratory。
- **授權／公開限制：** 定量主張以 structured abstract 為主要依據；受限 PDF 僅用來核對表圖位置。ADA 文章無 CC 授權聲明，本案受限解析亦有權利事件；公開版僅重繪已核實數值與 DOI，不散布原表、原圖、PDF 或解析檔。

### 03-E｜SELECT、FLOW、SOUL 預先設定彙總

- **文章插入位置：**「彙總分析」段後。
- **穩定 source ID：** `SELECT-FLOW-SOUL-POOLED-2026`。
- **Exact locator：** PubMed structured abstract／Methods／Findings，PMID 42567173。全文 Table／Figure locator：`NR`。
- **投影片視覺：** 自製兩列 forest：主要 pooled kidney/CV-death composite（持續 ≥50% eGFR 下降、腎衰竭、腎因性死亡或 CV death）HR 0.84；排除 CV death 的較窄次要複合 HR 0.80。終點定義可畫成對照條，但 pooled estimate 不與 FLOW／SOUL 排成三個獨立 HR 的 matched triplet。
- **一句圖說：** 彙總分析使用結構上協調的終點並增加估計精確度，但 pooled HR 已包含三項母試驗，並未消除族群、劑量與途徑上的異質性。
- **30 秒口述：** 30,787 人的彙總中，主要複合事件為 973 對 1,134，HR 0.84；排除 CV death 的較窄複合事件為 347 對 416，HR 0.80。Methods 已核實兩個終點定義，但 pooled estimate 含 FLOW、SELECT、SOUL 資料，與母試驗統計相依；不得把 pooled 0.84／0.80 與 FLOW 0.76／0.79 或 SOUL 0.91／0.86 當成三個獨立值作效果排名，也不能當作血糖或體重中介分析。
- **投影片頁腳短引：** Mann JFE, et al. *Lancet Diabetes Endocrinol*. Published online 2026-08-07. PubMed Methods/Findings. doi:10.1016/S2213-8587(26)00134-8. Abstract-level evidence。
- **授權／公開限制：** 摘要層級且無本案已核實全文重用授權。沒有原圖可用，公開版只重繪摘要明載數值。

### 03-F｜類別效應與機轉證據階梯

- **文章插入位置：**「類別效應」與「腎臟保護可能怎麼發生」之間。
- **穩定 source ID：** `GLP1-CLASSMETA-BADVE-2025`；`SUSTAIN6-MEDIATION-2021`；`GLP1R-LOCALIZATION-2014`；`GLP1-RENAL-CROSSTALK-2024`。
- **Exact locator：** Badve PubMed structured abstract／Findings，PMID 39608381；SUSTAIN-6 mediation Methods／Figure 1A–F；GLP1R localization Methods／Results，PMID 24467746；renal crosstalk review 的 human renal physiology 與 receptor-localization sections，PMID 38105752。
- **投影片視覺：** 自製證據階梯，底層列 outcome RCT／meta-analysis，中層列非 FLOW 中介分析，上層列人體生理與組織定位。直接腎元 GLP-1R 路徑標 `未確立`。
- **一句圖說：** 類別層級腎臟訊號受到支持，確切人體機轉仍是多路徑假說，直接腎元 GLP-1 receptor 作用尚未確立。
- **30 秒口述：** 十項 T2D RCT 的腎臟專屬複合 HR 為 0.82，但分子證據厚度不均。非 FLOW 中介分析提示血糖與血壓可能部分參與。最佳人體定位研究把受體放在腎絲球前血管平滑肌，不在腎小管或腎絲球細胞，因此不要畫成已知的直接腎元作用。
- **投影片頁腳短引：** Badve SV, et al. doi:10.1016/S2213-8587(24)00271-7；Mann JFE, et al. doi:10.1111/dom.14443；Pyke C, et al. doi:10.1210/en.2013-1934；Hinrichs GR, et al. doi:10.1152/ajpcell.00476.2023。
- **授權／公開限制：** Badve 為摘要層級，接受稿路徑為 CC BY-NC-ND，勿公開改作其原圖。其餘來源以短引與自製概念圖呈現，不複製原機轉圖。

---

## 文章 04｜安全、晚期 CKD、透析、法規與雙專科

### 04-A｜FLOW 安全性：受試者數與事件數分開

- **文章插入位置：**「FLOW 安全性」表後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`FLOW-SUPPLEMENT-2024`。
- **Exact locator：** `FLOW-PRIMARY-2024` Table 3，journal p.120／本機 PDF p.12；`FLOW-SUPPLEMENT-2024` Table S4，supplement pp.28–31；Table S5，p.32。
- **投影片視覺：** 公開版重繪 grouped dot plot，分開「至少一件事件的受試者」與「episode count」。Table 3、S4、S5 頁面只作僅本機來源截圖。
- **一句圖說：** FLOW 未見嚴重不良事件整體增加，但 semaglutide 的永久停藥與 GI 停藥比例較高。
- **30 秒口述：** 嚴重不良事件受試者為 49.6% 對 53.8%。永久停藥是 13.2% 對 11.9%，其中 GI 原因為 4.5% 對 1.1%。嚴重低血糖受試者都是 2.1%，但 episode ratio 1.02 是不同計數單位，不能混成 hazard ratio。
- **投影片頁腳短引：** Perkovic V, et al. *N Engl J Med*. 2024;391:109–121. Table 3；FLOW Supplement Tables S4–S5. doi:10.1056/NEJMoa2403347。
- **授權／公開限制：** NEJM 原表不進公開 repo，改用本案重繪與短引。

### 04-B｜AKI 與容量耗竭的床邊風險

- **文章插入位置：**「AKI」段後。
- **穩定 source ID：** `FLOW-SUPPLEMENT-2024`；`FDA-OZEMPIC-USPI-S038-2026`。
- **Exact locator：** FLOW Supplement Table S4，pp.28–31；FDA label Warnings and Precautions「Acute Kidney Injury Due to Volume Depletion」與 Renal Impairment §8.6。
- **投影片視覺：** 自製臨床路徑圖：GI loss／攝取下降，加上利尿劑或 SGLT2i，導向容量與腎功能評估。FLOW 的 AKI 124 對 123、脫水 10 對 10置於側欄。
- **一句圖說：** FLOW 的平均 AKI 計數沒有失衡，仿單警語仍要求在 GI loss 與容量耗竭情境監測腎功能。
- **30 秒口述：** 試驗裡嚴重 AKI preferred term 為 7.0% 對 7.0%，脫水 0.6% 對 0.6%。這降低直接腎毒性的疑慮，但臨床病人可能同時有晚期 CKD、利尿劑、SGLT2i、嘔吐或進食差，個別腎灌流風險不能被平均值抵消。
- **投影片頁腳短引：** FLOW Supplement Table S4；Ozempic U.S. Prescribing Information, Warnings「Acute Kidney Injury Due to Volume Depletion」and §8.6。
- **授權／公開限制：** 官方仿單只作短引與官方連結，不截圖整頁。公開版使用原創臨床路徑。

### 04-C｜視網膜病變：FLOW 與 SUSTAIN-6 問題不同

- **文章插入位置：**「視網膜病變」段後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`FLOW-SUPPLEMENT-2024`；`SUSTAIN6-RETINOPATHY-2018`；`FDA-OZEMPIC-USPI-S038-2026`。
- **Exact locator：** systematic retinopathy 402（22.8%）vs 398（22.5%）：`FLOW-PRIMARY-2024` Safety narrative，journal p.117／local PDF p.9，及 Table 3，journal p.120／PDF p.12；serious eye SOC 53 vs 30：`FLOW-SUPPLEMENT-2024` Table S4，PDF p.30；SUSTAIN-6 retinopathy Methods §2.1.4／Results，PMCID PMC5888154；FDA label「Diabetic Retinopathy Complications」。
- **投影片視覺：** 自製兩欄對照。FLOW 欄列系統性計數與排除不穩定病變，SUSTAIN-6 欄列外部判讀的視網膜併發症 HR 1.76。
- **一句圖說：** FLOW 的中性視網膜病變計數不能取消高風險病人的眼科監測，也不能把較廣泛的 eye-disorder SOC 改稱為判讀事件。
- **30 秒口述：** FLOW 的糖尿病視網膜病變為 22.8% 對 22.5%，但排除了不穩定病變。SUSTAIN-6 的判讀併發症 HR 1.76，未受多重比較保護。合理作法是在已有病變、使用胰島素或預期 HbA1c 快速下降時加強追蹤，而不是宣稱直接視網膜毒性。
- **投影片頁腳短引：** FLOW primary Safety p.117 and Table 3 p.120；FLOW Supplement Table S4 p.30；SUSTAIN6 retinopathy, Methods §2.1.4/Results, PMCID PMC5888154；Ozempic USPI, Diabetic Retinopathy Complications。
- **授權／公開限制：** 公開版自製對照表，只短引來源，不重製出版社或仿單原圖。

### 04-D｜晚期 CKD 的營養、功能與容量清單

- **文章插入位置：**「晚期 CKD 的床邊清單」段後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`FDA-OZEMPIC-USPI-S038-2026`；`FLOW-PROTOCOL-2021`。
- **Exact locator：** FLOW Tables 1–2／Results，journal pp.112–116；Table 3，journal p.120／local PDF p.12；FDA label Warnings 與 §8.6；FLOW protocol synopsis pp.6–7。特定肌少症、握力或營養門檻：`NR`。
- **投影片視覺：** 本案原創床邊 checklist，分為開始前、滴定期、病日、營養功能與透析乾體重。不要新增數值門檻。
- **一句圖說：** 晚期 CKD 的關鍵不只是 eGFR，還要把 GI 攝取、容量狀態與營養功能放在同一份監測計畫。
- **30 秒口述：** FLOW 的淨體重差為 −4.10 kg，但沒有瘦體組織、握力、衰弱或營養結果。無須腎功能劑量調整是 PK 陳述，不等於超出 FLOW 邊界的療效證明。高齡或 G4/G5 病人應分開判讀脂肪、組織與體液變化。
- **投影片頁腳短引：** Perkovic V, et al. doi:10.1056/NEJMoa2403347；Ozempic USPI, Warnings and §8.6；FLOW protocol v5.0, synopsis pp.6–7。
- **授權／公開限制：** Checklist 為本案原創綜整。來源只作短引，protocol 與仿單頁面不重製。

### 04-E｜透析後持續用藥的選定族群

- **文章插入位置：**「洗腎證據」表後。
- **穩定 source ID：** `FLOW-DIALYSIS-SAFETY-2026`。
- **Exact locator：** PubMed structured abstract，Research Design and Methods／Results，PMID 41893299；受限原文位置：Figure 1，journal p.1001／local PDF p.4，Table 1，p.1002／PDF p.5，Table 2，p.1003／PDF p.6，Figure 2，p.1004／PDF p.7。
- **投影片視覺：** 自製篩選漏斗：來源報告分母 34,064，307 人開始透析，165 人持續原分派用藥，semaglutide 71、安慰劑 94。旁註四母試驗名目 N 合計 34,084，差 20 人未解。
- **一句圖說：** 透析分析只描述開始透析後仍持續原分派用藥的 165 人，不能回答維持性透析中新開始 semaglutide 的療效。
- **30 秒口述：** 這是以活到透析且持續用藥為條件的事後族群，隨機比較已被選擇過程破壞。嚴重不良事件 45% 對 57% 可作初步描述，MACE 與死亡的事件率不能轉成 HR 或因果效果，也沒有透析脫離或移植效益證明。
- **投影片頁腳短引：** Klein KR, et al. *Diabetes Care*. 2026. PubMed structured abstract, Results. PMID 41893299. Post hoc descriptive analysis。
- **授權／公開限制：** 摘要數字可短引。ADA 公開存取不等於 CC 授權，受限解析檔有權利事件，原 PDF／表／圖不散布。

### 04-F｜美國、台灣與歐盟法規差異

- **文章插入位置：**「法規」表後。
- **穩定 source ID：** `FDA-OZEMPIC-APPROVAL-S025-2025`；`FDA-OZEMPIC-USPI-S038-2026`；`TFDA-OZEMPIC-2026`；`EMA-OZEMPIC-SMPC-2026`。
- **Exact locator：** FDA approval letter；USPI Indications §1.1；TFDA official indication／revision section；EMA SmPC §§4.1、5.1。
- **投影片視覺：** 自製三欄法域表。日期、文字地位與 FLOW 收案邊界分開列示，不用國旗作證據替代。
- **一句圖說：** 美國與台灣有獨立 CKD 適應症文字，歐盟把 FLOW 放在 SmPC §5.1，但 §4.1 未新增同型獨立 CKD 適應症。
- **30 秒口述：** 同一份 FLOW 在不同法域轉化成不同標籤。美國 2025 年首次核准 CKD 風險降低，台灣現行標籤有獨立條款，但 2026-01-26 只確認為修訂日。歐盟仍以 T2D 血糖控制為 §4.1 適應症，不能說三地文字相同。
- **投影片頁腳短引：** FDA S-025 approval letter and Ozempic USPI S-038 §1.1；TFDA 衛部菌疫輸字第001107號；EMA EMEA/H/C/004174 §§4.1, 5.1。Accessed through evidence cutoff 2026-09-05。
- **授權／公開限制：** 官方文件短引與連結。不要在公開 repo 大量重製標籤頁面或商標版面。

### 04-G｜指引時序與內分泌科／腎臟科視角

- **文章插入位置：**「指引演進」及「內分泌科與腎臟科」兩節之間。
- **穩定 source ID：** `KDIGO-DIABETES-CKD-2022`；`KDIGO-CKD-2024`；`ADA-STANDARDS-2026`；`CKM-GUIDELINE-2026`；`KDIGO-DIABETES-CKD-UPDATE-2026-DRAFT`；核心結果另引 `FLOW-PRIMARY-2024`。
- **Exact locator：** KDIGO 2022 Figure 23、Recommendation 4.2.1、Practice Points 4.1–4.3；ADA 2026 Chapter 11 recommendations 11.7a–b、11.9、11.11b 與 Chapter 9 recommendations 9.10–9.11；CKM 2026 official AHA summary；KDIGO 2026 public-review status page。CKM 完整 sequencing recommendation：`NR`，未逐字核實。
- **投影片視覺：** 上半部自製時間線，下半部兩欄問題清單。內分泌欄聚焦血糖、體重與 ASCVD，腎臟欄聚焦終點是否含 CV death、腎衰竭組成、容量與營養。
- **一句圖說：** 指引時序解釋 FLOW 前後定位差異，雙專科則用不同問題共同校正同一份證據。
- **30 秒口述：** KDIGO 2022 與 2024 都早於 FLOW 完整納入。ADA 2026 已把具證據效益的 GLP-1RA 放入 CKD 進展與 CV 風險建議，同時保留 SGLT2i 的基礎地位。CKM 2026 的「或」不能讀成等效或頭對頭排序，KDIGO 2026 截止日仍是草案。
- **投影片頁腳短引：** KDIGO 2022 Figure 23/Rec 4.2.1；ADA Standards 2026, 11.7a–b and 9.10–9.11；2026 CKM guideline official AHA summary；KDIGO 2026 public-review status。
- **授權／公開限制：** 只短引官方建議與自製時間線。CKM 快取稿有 AHA 再利用限制且解析 QA 不完整，不重製原圖、表或長段文字。

---

## 文章 05｜病例、22 問、證據缺口與演算法

### 05-A｜五種病例表現型矩陣

- **文章插入位置：**「五個病例」結束後。
- **穩定 source ID：** `FLOW-PROTOCOL-2021`；`FLOW-PRIMARY-2024`；`FLOW-SGLT2-2024`；`FLOW-MRA-2025`；`SELECT-KIDNEY-2024`；`SOUL-PRIMARY-2025`。
- **Exact locator：** FLOW protocol synopsis pp.6–7；FLOW Tables 1–2；SGLT2 Figure 1／Table 1；MRA Figure 1／Supplementary Tables 1–2；SELECT Table 1／Figures 1–5；SOUL structured abstract Results。
- **投影片視覺：** 自製五列 matrix，欄位只放表現型、是否符合 FLOW、可辯護的證據等級與主要未知。不要把個案做成固定藥物順序。
- **一句圖說：** 病人是否符合 FLOW 表現型，和多藥排序或加成性是否已證明，是兩個不同問題。
- **30 秒口述：** 病例 A 最接近 FLOW。病例 B 符合收案但已用 SGLT2i，增量硬腎臟效益未知。病例 C 必須先取得 UACR，eGFR 25 是下界。病例 D 的 finerenone 組合沒有直接隨機證據。病例 E 需要分開看 FLOW、SELECT 與 SOUL 的劑量與族群。
- **投影片頁腳短引：** Source IDs and exact locators as listed above；full citations in `SOURCE_LEDGER.csv`。
- **授權／公開限制：** 病例矩陣為本案原創綜整。不要嵌入受限來源截圖。

### 05-B｜22 問拆成四個演講模組

- **文章插入位置：**「22 個臨床問題」表前。
- **穩定 source ID：** 各題沿用原表 source ID；總索引為 `15_CLAIM_EVIDENCE_MAP.md` 與 `SOURCE_LEDGER.csv`。這兩者是專案定位檔，不取代原始出版來源。
- **Exact locator：** 每題使用文章原表「核心來源／exact locator」欄；單一統一原始 Table／Figure：`NR`。
- **投影片視覺：** 自製四段章節頁：證明了什麼、如何與現有治療並用、誰在證據外、安全與監測。每段挑 3 至 5 題，剩餘題放 appendix。
- **一句圖說：** 22 問適合用來建立 Q&A 導航，不宜在一張投影片壓成 22 列小字。
- **30 秒口述：** 主講只需要四個問題群。第一群校正 endpoint，第二群處理 SGLT2i 與 finerenone，第三群標出低 UACR、eGFR<25 與透析邊界，第四群處理 GI、容量、營養與眼科追蹤。每題答案保留 established、suggestive 或 unknown。
- **投影片頁腳短引：** 依每題原始 source ID 逐張列示；不得只引用專案內部綜整檔。
- **授權／公開限制：** 導航圖為本案原創。所有定量頁仍須回引原始論文、仿單或指引。

### 05-C｜FLOW 證據邊界地圖

- **文章插入位置：**「哪些人仍在證據邊界外」表後。
- **穩定 source ID：** `FLOW-PROTOCOL-2021`；`FLOW-SUPPLEMENT-2024`；`FLOW-CKDSEVERITY-2026-CJASN`；`FLOW-DIALYSIS-SAFETY-2026`；`SELECT-KIDNEY-2024`。
- **Exact locator：** protocol synopsis pp.6–7；supplement Eligibility Criteria pp.11–13；CJASN Figures 1–2；dialysis PubMed structured abstract／Results；SELECT Table 1／Figures 1–5。
- **投影片視覺：** 自製綠／黃／灰 evidence map。綠色只放符合 FLOW 收案者，黃色放不精確次族群或間接資料，灰色放 eGFR<25、維持性透析、移植、T1D、腎絲球腎炎／ADPKD 與衰弱營養缺口。
- **一句圖說：** FLOW 的直接效益證據有清楚的 T2D、eGFR 與白蛋白尿邊界，邊界外資料多為不精確、間接或尚未研究。
- **30 秒口述：** UACR≤100 的 350 人是基線再分類，不能代表持續正常白蛋白尿。eGFR<25、維持性透析與移植在 FLOW 沒有直接療效資料。SELECT 與透析分析提供旁證，但研究問題不同，所以投影片以顏色區分而不把旁證升格。
- **投影片頁腳短引：** FLOW protocol v5.0, synopsis pp.6–7；FLOW Supplement Eligibility pp.11–13；CJASN 2026 Figures 1–2；PMID 41893299；doi:10.1038/s41591-024-03015-5。
- **授權／公開限制：** 地圖為本案原創。protocol、NEJM supplement 與 ADA 原頁不公開；CJASN／SELECT CC BY 4.0 圖可在完整歸屬下使用。

### 05-D｜表現型導向演算法

- **文章插入位置：**「表現型導向的分層演算法」段後。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`FLOW-SGLT2-2024`；`FLOW-MRA-2025`；`COMBO-MODEL-NEUEN-2024`；`ADA-STANDARDS-2026`；`FDA-OZEMPIC-USPI-S038-2026`。
- **Exact locator：** FLOW Table 2／Discussion；SGLT2 Figure 1／Table 1；MRA Figure 1／Supplementary Tables 1–2；Neuen PubMed structured abstract／Results，PMID 37952217；ADA recommendations 11.7a–b、9.10–9.11；USPI Warnings／§8.6。
- **投影片視覺：** 可編輯流程圖，但標題寫「證據組織架構」。每個節點放證據層級；多藥節點明示 `直接加成性 unknown`。
- **一句圖說：** 演算法依表現型與耐受性組織證據，不是經 RCT 驗證的固定一至四階梯。
- **30 秒口述：** 先確認 FLOW 邊界，再建立 RASi 與 SGLT2i 的腎臟／HF 基礎。Finerenone 與 semaglutide 依殘餘白蛋白尿、血鉀、肥胖、ASCVD 與血糖需求分流。若需要多藥，必須說明最佳順序與加成性未知，模型 NNT 不能當治療承諾。
- **投影片頁腳短引：** FLOW doi:10.1056/NEJMoa2403347；Mann doi:10.1038/s41591-024-03133-0；Rossing doi:10.2337/dc25-0472；Neuen doi:10.1161/CIRCULATIONAHA.123.067584；ADA 2026 recommendations。
- **授權／公開限制：** 流程圖為本案原創。不要重製指引原演算法，也不要將模型化數字視為 RCT 資料。

### 05-E｜共同決策的雙句式結尾

- **文章插入位置：**「最後的共同決策句」段後，亦可作最後一張投影片。
- **穩定 source ID：** `FLOW-PRIMARY-2024`；`FLOW-SGLT2-2024`；`FLOW-MRA-2025`。
- **Exact locator：** FLOW Table 2／Discussion，journal pp.116、119–120；SGLT2 Figure 1／Table 1；MRA Figure 1／Supplementary Tables 1–2。
- **投影片視覺：** 純文字結尾頁，左側「可以有把握地說」，右側「仍需誠實說」。不用裝飾性藥物照片。
- **一句圖說：** FLOW 已建立相符族群的隨機器官結果證據，個別腎衰竭、超界療效與多藥加成性仍未確立。
- **30 秒口述：** 對符合 FLOW 的病人，可以明確說 semaglutide 降低含 CV death 的主要複合終點，也減慢 eGFR 斜率。同時要說清楚，KRT 與 eGFR<15 沒有個別確認，eGFR<25 與透析沒有直接療效資料，和 SGLT2i 或 finerenone 的增量硬腎臟效益仍未知。
- **投影片頁腳短引：** Perkovic V, et al. Table 2/Discussion. doi:10.1056/NEJMoa2403347；Mann JFE, et al. doi:10.1038/s41591-024-03133-0；Rossing P, et al. doi:10.2337/dc25-0472。
- **授權／公開限制：** 文字與版面為本案原創，頁腳只列必要 citation。

---

## 可直接貼入五篇文章文末的統一提示

> ### 投影片用 reference 快速索引
>
> 本文對應的投影片來源、原始 Table／Figure／頁碼、建議圖說、30 秒口述與公開再利用限制，整理於 `presentation_zh_tw/ARTICLE_REFERENCE_GUIDE.md`。投影片上的數據 citation 應直接指向原始 source ID 與 exact locator，不以本篇綜整代替原始來源。原圖截圖是否可公開使用，依該列授權標記決定；未確認授權者僅供本機核對，公開版本改用可編輯重繪。

## 發表前自查

### Endpoint 與 CV death

- [ ] 每一次出現 FLOW `HR 0.76` 或「下降 24%」，同一畫面都寫明「五項主要複合終點，包含 CV death」。
- [ ] FLOW `HR 0.79` 明示為排除 CV death 的四項腎臟專屬複合終點，且標示支持性、位於確認性階層之外、未校正多重比較。
- [ ] 不把「CV death 約占主要終點各組成事件約 35%」改寫成首次事件占比或治療效果占比，也不從重疊的 component counts 做代數分解。
- [ ] 不寫「腎衰竭下降 24%」。KRT、持續 eGFR<15、腎因性死亡均保留個別未確認的地位。

### Interaction 與探索性分析

- [ ] SGLT2i 的主要與腎臟專屬終點 P-interaction 0.109／0.100 只解讀為「未偵測到異質性」，不解讀為等效、效果完整保留或加成。
- [ ] SGLT2i 的持續 eGFR 下降 ≥50% P-interaction 0.023 標示 `nominal, unadjusted for multiplicity`，不宣稱使用者受害。
- [ ] MRA 主要終點 P-interaction 0.12 不宣稱 MRA 使用者獲益更大。KRT P-interaction 0.027 同時標出僅 11 事件、名目且未校正。
- [ ] CKD 嚴重度之死亡率交互作用、UACR≥2,000 死亡結果，以及 SOUL 階層失敗後的斜率，都標明 post hoc／exploratory 或形式上探索性。
- [ ] 「一組顯著、另一組不顯著」不等於兩組效果顯著不同，只有 interaction test 回答異質性問題。

### 加成性禁語

- [ ] 不使用「已證明 semaglutide 加在 SGLT2i 上有額外硬腎臟效益」。正確用語是「增量效益與傷害均未解」。
- [ ] 不使用「FLOW 證明 semaglutide＋finerenone」。FLOW 基線 finerenone 為 0，MRA 次族群主要是 spironolactone／eplerenone。
- [ ] 不使用「四重治療已由 RCT 證明」或把模型化 NNT 當成真實治療效果。
- [ ] 不把「未偵測到交互作用」改寫成「協同」、「加成」、「相容性已證明」或「所有背景治療下效果相同」。

### 圖像、數字與公開 repo

- [ ] 每張圖都能追到 source ID、Table／Figure／Results locator、DOI／PMID 與證據層級。
- [ ] 原始來源未報告的值標 `NR`，不自行從像素、粗事件比例或不同時點反推 ARR、NNT、斜率或 HR。
- [ ] NEJM、ADA、AHA、仿單、protocol／SAP 與未核實授權來源的截圖不進公開 repo。
- [ ] CC BY 4.0 原圖保留完整 attribution、授權連結與修改聲明，並檢查第三方 credit line。
- [ ] 公開重繪保留單位、比較方向、95% CI、P-interaction 與推論層級，避免以版面設計弱化限制語。
