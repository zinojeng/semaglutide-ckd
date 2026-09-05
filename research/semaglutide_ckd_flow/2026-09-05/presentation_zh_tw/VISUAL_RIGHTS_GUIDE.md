# Semaglutide、CKD 與 FLOW 簡報：視覺素材與重製權利計畫

**版本：** 2026-09-05 evidence cutoff<br>
**用途：** 25 張繁體中文學術簡報之圖表選材、重繪與公開發布閘門<br>
**原則：** 可閱讀／可引用不等於可重製；數值事實可用全新設計重繪，但不得描摹受保護之版面、配色、圖示或表格編排<br>
**注意：** 本文件是保守的編輯與發布風險計畫，不是法律意見；權利不明時一律採較窄權限

## 一、判定圖例與共通規則

### 動作標籤

- **SCREENSHOT：** 只在文章明示相容的 Creative Commons 授權、目標圖無另列第三方權利、且署名與修改說明完整時使用。
- **REDRAW：** 只抽取必要事實／數值，用本專案自己的資訊階層、幾何、字型與配色重新設計；不逐格描摹、不複製整張表。
- **NO-USE：** 不把原圖、原表、裁切圖、PDF 頁面或解析衍生圖放入簡報或公開 Git；若仍需表達內容，改採經獨立核實的事實重繪。

### 頁碼與來源定位

- `PDF p.X` 指本機 PDF 的實體頁序；`journal p.X` 指文章印刷頁碼。兩者同列時，製作與 QA 必須同時核對。
- 補充資料只有 PDF 頁序時，以 `supplement PDF p.X` 為準。
- Europe PMC XML 沒有穩定頁碼時，以 **Figure/Table 編號＋DOI＋PMCID** 作精確定位，不虛構頁碼。
- 授權連結固定使用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 與 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)；最終投影片不能只寫縮寫而省略連結。

### 全域發布閘門

1. **不得提交來源 PDF、全文解析、快取或裁切暫存圖。** 公開 Git 只收最終自製圖，或經逐圖確認可重製且已內嵌署名的 CC 圖。
2. **截圖必須在投影片同頁署名。** 僅放在尾頁參考文獻不足；CC 圖還須列授權連結與是否有裁切、翻譯、標色或註記。
3. **CC BY-NC 圖只限明確非商業版本。** 若投影片可能用於收費課程、業配、商業醫學教育或無法控制下游用途，改用事實重繪或另取權利。
4. **CC 授權文章中的第三方素材不是自動安全。** 圖說若有 `adapted from`、另列 credit line、商標、地圖底圖或量表，須另外核對；未核對即 NO-USE。
5. **非 CC 來源不因「私人演講」自動取得截圖權。** 本計畫不預設合理使用／合理處理；需 publisher permission 才重製。
6. **受限解析事件不得繞道使用。** `SOUL-KIDNEY-2026`、`FLOW-DIALYSIS-SAFETY-2026`、`CKM-GUIDELINE-2026`、歷史 FDA label 與 quarantined misfetch 的雲端解析皆不得成為圖像來源或唯一證據。
7. **數字 QA 高於視覺便利。** Mann SGLT2i 原始 Markdown 曾有欄位錯置風險；Mahaffey 本機衍生圖曾有錯位事件。這兩項只能以出版圖像／官方頁面重新核對，不能從未核准的解析表格直接繪圖。
8. **NEJM Table 3 的正確定位為 journal p.120／PDF p.12。** 既有講稿與部分衍生文字中的 `p.117` 不得沿用；此頁碼已由 PDF 版面直接核實。

## 二、15 項優先視覺資產

以下以 `P0`（核心）、`P1`（重要）與 `P2`（可依篇幅取捨）排序。

### VR-01｜P0｜FLOW 試驗設計時間軸

- **精確來源：** `FLOW-DESIGN-2023`，Figure 2，`PDF p.4 / journal p.2044`；本機來源 `sources/retrieved/cache/pdfs/FLOW-DESIGN-2023_RossingNDT2023.pdf`。
- **投影片目的：** 說明雙盲、事件驅動、每週皮下注射 semaglutide 1.0 mg、基線 SGLT2i 分層，以及期中分析／提前結束的架構。
- **動作：** **REDRAW（首選）**。只保留隨機分派、劑量、追蹤與終點順序；不照搬原 Figure 2 的幾何與圖示。
- **權利證據：** 文章 `PDF p.1` 明示 **CC BY-NC 4.0**。非商業簡報可依授權重製／改作；商業情境不在授權內。
- **公開 Git：** **可以，限本專案全新重繪。** 若實質沿用原圖表達方式，整項資產須標明 CC BY-NC 4.0 且不得進入商業版本。不要提交來源 PDF。
- **私人學術演講：** 非商業、附署名時可用原圖；仍建議重繪以統一中文與避免下游用途不明。
- **裁切指引：** 如確需原圖，保留 Figure 2 全部流程、圖例與註腳；裁切頁眉／翻譯標籤均屬修改，署名須寫 `Adapted` 與修改內容。不可只截半條時間軸而移除分層或終點資訊。
- **建議圖說：** 「FLOW 為事件驅動之腎臟結果試驗；設計論文報告 N=3,534，主要結果論文報告 N=3,533，原因未明，兩者不得自行協調。」
- **署名模板：** `Data redrawn from Rossing et al., Nephrol Dial Transplant 2023;38:2041–2051, Fig. 2, DOI 10.1093/ndt/gfad009; original figure not reproduced.` 若使用／改作原圖，再加 `CC BY-NC 4.0; adapted with zh-TW labels.`

### VR-02｜P0｜FLOW 收案雙路徑＋KDIGO 風險輪廓

- **精確來源：** `FLOW-DESIGN-2023`，Table 1，`PDF p.5 / journal p.2045`；Figure 4，`PDF p.9 / journal p.2049`。收案邊界另由 `FLOW-SUPPLEMENT-2024` Eligibility Criteria，`supplement PDF pp.11–13` 核對。
- **投影片目的：** 讓腎臟科一眼看見 eGFR 與 UACR 必須成對判讀，也讓內分泌科知道 FLOW 不是所有 T2D 或所有 CKD 的縮影。
- **動作：** **REDRAW；Figure 4 原圖 NO-USE。** 製作兩列 eligibility matrix：`eGFR 50–75 + UACR >300–<5,000` 與 `eGFR 25–<50 + UACR >100–<5,000`；旁列 68.3% 為 KDIGO very high risk 的文字／自製比例條。
- **權利證據：** 設計文章為 CC BY-NC 4.0，但 Figure 4 圖說明載 **adapted from KDIGO Diabetes Work Group (2020)**，存在內嵌第三方權利；文章授權不能取代原 KDIGO 素材的核對。
- **公開 Git：** **可以，僅限全新資料圖。** 不放 Figure 4 截圖，也不仿製 KDIGO 色塊矩陣。
- **私人學術演講：** 同樣不建議截 Figure 4；除非另行確認 KDIGO 原始授權與正確 credit line。
- **裁切指引：** 不裁 Figure 4。自製 eligibility matrix 必須保留 `>`、`<` 與單位，不把基線再分類的 UACR `<100` 次族群誤寫成前瞻性收案路徑。
- **建議圖說：** 「FLOW 富集的是 T2D 合併白蛋白尿性 CKD；eGFR<25、維持性透析及低／正常白蛋白尿族群不能直接套用其療效結論。」
- **署名模板：** `Original project graphic; eligibility data from FLOW-DESIGN-2023 Table 1 (journal p.2045) and FLOW Supplement Eligibility Criteria (PDF pp.11–13). No KDIGO figure reproduced.`

### VR-03｜P0｜五項主要終點與四項腎臟專屬終點成對呈現

- **精確來源：** `FLOW-PRIMARY-2024`，Figure 1A–B，`PDF p.6 / journal p.114`（圖說延續至 `PDF p.7 / journal p.115`）；Table 2，`PDF p.8 / journal p.116`；DOI `10.1056/NEJMoa2403347`。
- **投影片目的：** 以同一視覺層級呈現 HR `0.76 (0.66–0.88)` 與 HR `0.79 (0.66–0.94)`，但清楚區分確認性主要結果與支持性、位於階層之外的四項結果。
- **動作：** **REDRAW；NEJM 原圖／原表 NO-USE。** 建議用兩張並排結果卡或全新 forest，不複製 Kaplan–Meier 曲線。
- **權利證據：** `FLOW.pdf PDF p.1` 與各頁頁腳載明 Massachusetts Medical Society copyright、`For personal use only`、`No other uses without permission`；無重製授權。
- **公開 Git：** **可以，僅限原創資料重繪。** 不得提交原圖、裁切、描摹版或整張 Table 2。
- **私人學術演講：** **原圖不使用，除非另取 NEJM permission。** 投影片可用經核對的數字與自製視覺。
- **裁切指引：** 無可授權裁切。重繪時兩張卡須同時保留終點組成、HR、95% CI 與推論層級，不能只留「24%」大字。
- **建議圖說：** 「FLOW 證明的是含 CV death 的五項複合終點下降；排除 CV death 的四項結果方向一致，但屬支持性、未受確認性階層保護。」
- **署名模板：** `Data redrawn from Perkovic et al., N Engl J Med 2024;391:109–121, Fig. 1 and Table 2, DOI 10.1056/NEJMoa2403347; original graphic/table not reproduced.`

### VR-04｜P0｜eGFR 總斜率、acute phase 與慢性斜率

- **精確來源：** `FLOW-PRIMARY-2024`，Figure 1D，`PDF p.6 / journal p.114`；Table 2，`PDF p.8 / journal p.116`；Discussion，`journal pp.119–120`。
- **投影片目的：** 將總斜率差 `+1.16 mL/min/1.73m²/year`、0–12 週組間差約 `−0.03`、第 12 週後慢性斜率差 `+0.94` 分開，避免說成「沒有 acute dip」或個人保證可延後透析若干年。
- **動作：** **REDRAW；原曲線 NO-USE。** 用自製三段式 slope diagram 或三欄數值，不描摹原 Figure 1D 折線位置。
- **權利證據：** 同 VR-03；NEJM 僅個人使用，未授權重製。
- **公開 Git：** **可以，僅限全新資料圖。** 每一數值須回查 Table 2／Discussion，不從像素估值。
- **私人學術演講：** 自製圖可；原 Figure 1D 須 publisher permission。
- **裁切指引：** 不裁原圖。自製圖須保留單位、時間窗與「試驗層級平均」標記；若加 cystatin-C 訊號，只能說降低肌肉量造成量測假象的疑慮，不得說已證明與減重無關。
- **建議圖說：** 「兩組早期皆下降；關鍵是沒有明顯 semaglutide 專屬 acute-phase 差異，而後續慢性 eGFR 流失較慢。」
- **署名模板：** 同 VR-03，將 locator 改為 `Fig. 1D, Table 2 and Discussion, journal pp.114, 116, 119–120`。

### VR-05｜P0｜複合終點拆解：哪些硬腎臟組成尚未單獨確認

- **精確來源：** `FLOW-PRIMARY-2024`，Table 2，`PDF p.8 / journal p.116`；主要終點次族群 Figure 2，`PDF p.10 / journal p.118`；Discussion，`journal pp.119–120`。
- **投影片目的：** 以全新 forest／endpoint ladder 顯示 eGFR<15、KRT、kidney death 等個別組成 CI 跨 1，並教導「一側顯著、另一側不顯著」不等於交互作用成立。
- **動作：** **REDRAW；原 Table 2／Figure 2 NO-USE。** 只選回答臨床問題的 4–6 列，不複製整張表或森林圖排序。
- **權利證據：** 同 VR-03 的 NEJM 限制。
- **公開 Git：** **可以，僅限原創重繪。** 頁腳必須標出 Table 2 與 Figure 2 的不同角色。
- **私人學術演講：** 自製圖可；原圖無 permission 時不用。
- **裁切指引：** 不裁原圖。重繪必須保留事件數、95% CI、無效線與 `not powered for individual components`；不得以紅／綠燈暗示「無效」或「有害」。
- **建議圖說：** 「FLOW 成功降低包含腎衰竭的複合終點，但未個別證明透析／移植、eGFR<15 或腎因性死亡下降。」
- **署名模板：** `Data redrawn from FLOW-PRIMARY-2024 Table 2 and Fig. 2, journal pp.116 and 118; original NEJM material not reproduced.`

### VR-06｜P0｜UACR 與代謝軌跡小多圖

- **精確來源：** `FLOW-SUPPLEMENT-2024`，Figure S2A–D，`supplement PDF p.19`；Figure S2 圖說與模型說明同頁。UACR 的正式第 104 週估計另見主文 Table 2，`journal p.116`。
- **投影片目的：** 以 UACR 為主圖，體重、HbA1c、血壓作小型輔圖，說明多面向同向改變，但不暗示 UACR、體重或血糖已被證明為因果中介。
- **動作：** **REDRAW；supplement 原圖 NO-USE。** 優先只畫預先指定時間點與區間，不逐點臨摹完整曲線。
- **權利證據：** 補充檔為 NEJM 主文附件，未見獨立 CC 授權；依主文限制保守處理。
- **公開 Git：** **可以，僅限全新資料圖。** 原 supplement PDF、Figure S2 或裁切不得提交。
- **私人學術演講：** 自製圖可；原圖仍需權利人許可。
- **裁切指引：** 不裁原圖。若顯示第 208 週，必須同時標出僅約 `216/201` 人貢獻 UACR 資料，避免以尾端波動作強解讀。
- **建議圖說：** 「第 104 週 UACR ratio-of-ratios 0.68（約相對下降 32%）；這是支持性結果，不是已完成的 FLOW 中介分析。」
- **署名模板：** `Data redrawn from FLOW Supplement Fig. S2 (PDF p.19) and FLOW-PRIMARY-2024 Table 2 (journal p.116); original figures not reproduced.`

### VR-07｜P0｜安全性平衡表：SAE、停藥、GI 與腎前性風險

- **精確來源：** `FLOW-PRIMARY-2024`，Table 3，**`PDF p.12 / journal p.120`**；`FLOW-SUPPLEMENT-2024`，Table S4，`supplement PDF pp.28–31`，Table S5，`supplement PDF pp.32–33`。
- **投影片目的：** 同時顯示整體 SAE `49.6% vs 53.8%`、因任何 AE 永久停藥 `13.2% vs 11.9%`、GI 特定永久停藥 `4.5% vs 1.1%`、AKI preferred term `7.0% vs 7.0%`，避免把不同分母／子集合混在一起。
- **動作：** **REDRAW；原表 NO-USE。** 建議用四列 dumbbell／paired bars，加一列「臨床仍須處理 GI loss→volume depletion→prerenal AKI」。
- **權利證據：** 主文與補充資料均無可用重製授權；見 VR-03、VR-06。
- **公開 Git：** **可以，僅限全新資料圖。** 資料列須逐列標記 source table；不得整張複製 Table 3、S4 或 S5。
- **私人學術演講：** 自製圖可；原表需 NEJM permission。
- **裁切指引：** 不裁原表。任何視覺都須把 `AE-driven discontinuation` 與 `GI-specific discontinuation (subset)` 分開；不可把 `26%`／`28.8%` 的未解 any-reason discontinuation 當成 Table 3 數字。
- **建議圖說：** 「平均試驗資料未顯示 AKI 數值增加，但 GI 耐受不佳仍可透過攝取下降與體液流失造成個別病人的腎前性 AKI。」
- **署名模板：** `Data redrawn from FLOW-PRIMARY-2024 Table 3 (journal p.120) and FLOW Supplement Tables S4–S5 (PDF pp.28–33); original tables not reproduced.`

### VR-08｜P0｜基線 SGLT2i 次族群：不能證明加成性

- **精確來源：** `FLOW-SGLT2-2024`，Figure 1，`journal p.2851`；Figure 2，`journal p.2852`；Figure 3，`journal p.2853`；DOI `10.1038/s41591-024-03133-0`。授權文字在 `journal p.2856`，本機全文定位為 `fulltext/glp1_cardiorenal_Mann_2024.md` 末段 Open Access notice。
- **投影片目的：** 顯示基線 SGLT2i 使用者僅 `N=550`、主要五項 HR `1.07 (0.69–1.67)`、四項腎臟專屬 HR `1.18 (0.71–1.98)`，以及單一 ≥50% eGFR decline 的名目 interaction `P=.023`，明確阻止「已證明加成」或「已證明無效／有害」兩種過度解讀。
- **動作：** **REDRAW（首選）**。法律上可依 CC BY 4.0 截圖，但原 Figure 2 密集，且本機 Markdown 曾有表格欄位錯置風險；只從正式出版圖重新核對後畫 3–5 列。
- **權利證據：** 文章明示 **CC BY 4.0**；授權涵蓋圖片，除非個別 credit line 另有註明。重製／改作需署名、授權連結及變更說明。
- **公開 Git：** **可以。** 首選原創重繪；若直接使用圖像，只能從官方 Nature Medicine／PMC 來源重新取得，並逐圖檢查 credit line。
- **私人學術演講：** 可截圖或改作，條件同 CC BY 4.0。
- **裁切指引：** 若截圖，保留 panel label、無效線、95% CI、事件數與 interaction P；裁掉列、翻譯或加框都須標 `Adapted`。不可從 raw Markdown 生成 forest。
- **建議圖說：** 「未偵測到主要／四項複合終點的統計異質性不等於證明加成；基線 SGLT2i 次族群事件少，CI 同時容許效益、無效與傷害。」
- **署名模板：** `Adapted from Mann et al., Nat Med 2024;30:2849–2856, Figs. 1–2, DOI 10.1038/s41591-024-03133-0, CC BY 4.0. Changes: selected rows, zh-TW labels and emphasis.`

### VR-09｜P0｜基線 MRA 次族群：不是 finerenone 組合證據

- **精確來源：** `FLOW-MRA-2025`，Figure 2；DOI `10.2337/dc25-0472`；PMCID `PMC12583412`。本機來源為 Europe PMC XML 轉錄 `fulltext/glp1_cardiorenal_Rossing_2025.md`，無穩定印刷頁碼；**Figure 2＋DOI＋PMCID 即精確 locator**。
- **投影片目的：** 顯示 MRA 使用者 `N=257`、主要終點 HR `0.51 (0.30–0.86)`、interaction `P=.12`，並附 `spironolactone 218 / eplerenone 38 / esaxerenone 1 / finerenone 0`；KRT 名目 interaction `P=.027` 僅 11 事件。
- **動作：** **REDRAW；原 Figure 2 公開 NO-USE。** 用完全不同的四列證據卡，不仿原 forest。
- **權利證據：** 官方 XML 的使用聲明為：可在正確引用、教育及非營利、且**不改作**的條件下使用；不是 CC 授權。翻譯、裁切或重排原圖不符合「not altered」條件。
- **公開 Git：** **原圖不可。** 可提交只含已核實事實的全新圖，並明確標示原圖未重製；若欲公開原 Figure 2，需 ADA／權利人明確許可。
- **私人學術演講：** 只有在確定是教育、非營利、完整不改作並正確引用時，才可能原樣使用；本計畫仍首選資料重繪。不得裁切、翻譯或加色。
- **裁切指引：** 原圖 **不得裁切**。重繪不得把 steroidal MRA 次族群標成 finerenone subgroup，也不得把 interaction 不顯著說成效果相等。
- **建議圖說：** 「FLOW 的 MRA 次族群幾乎全為 spironolactone／eplerenone，沒有 finerenone；結果只能支持『未偵測到異質性』，不能證明 semaglutide＋finerenone 加成。」
- **署名模板：** `Data redrawn from Rossing et al., Diabetes Care 2025, Fig. 2, DOI 10.2337/dc25-0472, PMCID PMC12583412; original ADA figure not reproduced.`

### VR-10｜P1｜CKD 嚴重度下的心血管結果森林圖

- **精確來源：** `FLOW-CKDSEVERITY-2025`，Figure 2，**`PDF p.8 / journal p.1103`**；DOI `10.1093/eurheartj/ehae613`；本機 PDF `sources/retrieved/cache/pdfs/FLOW-CKDSEVERITY-2025_Mahaffey_EHJ2025_PMC11931213.pdf`。
- **投影片目的：** 以出版圖作為 eGFR、UACR、KDIGO 分層之 CV death/nonfatal MI/nonfatal stroke 複合結果數值權威，說明未偵測到主要 CV 複合效應修飾。
- **動作：** **SCREENSHOT（建議的兩項直接圖像重製之一）**，但製作時須從官方 PMC／期刊圖像重新取得；不得使用曾發生錯位的本機衍生圖。
- **權利證據：** 文章 `PDF p.1 / journal p.1096` 明示 **CC BY 4.0**，允許 unrestricted reuse、distribution、reproduction，條件為適當引用。Figure 2 未在已檢視圖說中另列第三方 credit；製作時仍須再檢查一次。
- **公開 Git：** **可以。** 最終圖片須在圖內或同頁附 CC BY 4.0 署名；不要提交完整文章 PDF。
- **私人學術演講：** 可以，條件同 CC BY 4.0。
- **裁切指引：** 優先保留整張 forest、列名、事件／分母、95% CI、無效線與 interaction P。若去除頁眉、翻譯或高亮，改標 `Adapted` 並列出變更；不能只截有利列。
- **建議圖說：** 「相對效果在預先設定 CKD 嚴重度分層未見明顯異質性；這不提供各分層 ARR／NNT，也不能以點估計大小排名誰獲益最多。」
- **署名模板：** `Adapted from Mahaffey et al., Eur Heart J 2025;46:1096–1108, Fig. 2 (p.1103), DOI 10.1093/eurheartj/ehae613, CC BY 4.0. Changes: crop/zh-TW labels/highlight.` 若完全未改作，將 `Adapted` 改為 `Reproduced` 並刪除 changes。

### VR-11｜P1｜SELECT：無糖尿病肥胖／ASCVD 族群的腎臟次要結果

- **精確來源：** `SELECT-KIDNEY-2024`，Figure 1，**`PDF p.2 / journal p.2059`**；Figure 4，`PDF p.6 / journal p.2063` 可作斜率備用；DOI `10.1038/s41591-024-03015-5`。授權文字在 `PDF p.9 / journal p.2066`。
- **投影片目的：** 將 SELECT 的 2.4 mg SC、overweight/obesity＋ASCVD、無已診斷糖尿病族群，與 FLOW 的 1.0 mg SC、T2D＋白蛋白尿性 CKD 分開；顯示五項腎臟複合（不含 CV death、包含新發巨量白蛋白尿）HR `0.78 (0.63–0.96)` 為跨族群支持而非 FLOW 複製。
- **動作：** **SCREENSHOT（Figure 1，可直接重製）**；若投影片版面無法保留 number-at-risk 與完整定義，改用 REDRAW。
- **權利證據：** 文章明示 **CC BY 4.0**；圖片原則上包含在授權內，除非另有 credit line。
- **公開 Git：** **可以。** 逐圖確認無第三方 credit，嵌入完整署名。不要把 PDF pp.13–21 的 Nature Reporting Summary 當成研究結果素材。
- **私人學術演講：** 可以，條件同 CC BY 4.0。
- **裁切指引：** Kaplan–Meier 圖保留兩組曲線、HR/CI、時間軸與 number-at-risk；裁切、翻譯或重著色均標 `Adapted`。不可裁掉 endpoint 定義，因 SELECT 複合終點含新發巨量白蛋白尿。
- **建議圖說：** 「SELECT 擴大了 semaglutide 的腎臟訊號，但族群、劑量與終點結構均不同；不能用此圖支持非糖尿病 CKD 的普遍硬腎臟適應。」
- **署名模板：** `Adapted from Colhoun et al., Nat Med 2024;30:2058–2066, Fig. 1 (p.2059), DOI 10.1038/s41591-024-03015-5, CC BY 4.0. Changes: crop/zh-TW labels.`

### VR-12｜P1｜開始透析後持續用藥：描述性安全邊界

- **精確來源：** `FLOW-DIALYSIS-SAFETY-2026`，原文 Figure 1 `PDF p.4`、Table 1 `PDF p.5`、Table 2 `PDF p.6`、Figure 2 `PDF p.7`；DOI `10.2337/dc26-0112`；PMID `41893299`。**但數值製圖只採已獨立核實的 PubMed structured abstract／official page，不採受限 PDF 解析。**
- **投影片目的：** 以 cohort waterfall 顯示來源報告分母 `34,064 → 307` 於試驗中開始透析 → `165` 開始透析後仍持續原分派用藥（semaglutide 71、placebo 94），並把「繼續用」與「在維持性透析中新開始」切開。
- **動作：** **原 Figure/Table NO-USE；由官方摘要事實 REDRAW。** 不從快取 PDF 截圖、不從 LlamaParse Markdown擷取。
- **權利證據：** ADA／NIH public-access deposit **不是 CC 授權**，license 為 NOASSERTION；文內另有 TDM/ML 限制，且本專案已記錄第三方解析權利事件。
- **公開 Git：** **只可放全新 waterfall 與短篇幅事實轉述。** 快取 PDF、解析、原 Figure 1／2、Table 1／2 均不可。
- **私人學術演講：** 不使用快取圖。若堅持使用原圖，須重新從官方頁面確認當次教育用途權限，且不得把先前受限解析當作授權；最安全仍是摘要事實重繪。
- **裁切指引：** 原圖無裁切方案。自製 waterfall 必須保留 survivor/selection conditioning，並另註四母試驗名目 N 相加為 `34,084`、與來源分母相差 20、原因未明。
- **建議圖說：** 「這是事後、條件於存活至透析且持續用藥的描述性分析；可提供初步耐受／安全訊號，不能證明在維持性透析中起始 semaglutide 的療效。」
- **署名模板：** `Original project graphic based on independently verified PubMed abstract data: Klein et al., Diabetes Care 2026, DOI 10.2337/dc26-0112, PMID 41893299; original figures/tables and restricted parse not reproduced.`

### VR-13｜P1｜FLOW vs SOUL：風險富集而非注射／口服勝負

- **精確來源：** 本專案原創比較表 `16_FINAL_SYNTHESIS_ZH_TW.md` §12「SOUL——為何……」，特別是該節 FLOW／SOUL 表與 exact-locator 註記。底層 FLOW：Table 1 `journal pp.112–113`、Results `pp.113, 115`、Supplement Table S2 `PDF p.24`；SOUL：PubMed structured abstract，PMID `41380027`。
- **投影片目的：** 比較族群、劑量／途徑、基線 eGFR/UACR、事件率與終點組成，阻止「SC 有效、oral 無效」的單因果敘事。
- **動作：** **REDRAW／沿用本專案原創表格；SOUL 原圖 NO-USE。** 建議改成 6 列、兩欄對照，不複製任何出版表格。
- **權利證據：** 比較表是本專案對已核實事實的原創選擇與編排；SOUL 全文為 ADA NOASSERTION 且有受限解析事件，故只採官方摘要與短篇幅轉述。
- **公開 Git：** **可以。** 頁腳保留逐欄 source ID／locator；不得納入 SOUL PDF、解析或原圖。
- **私人學術演講：** 可以使用原創表；SOUL 出版圖仍不使用。
- **裁切指引：** 不要只保留 HR；至少同時保留族群、劑量／途徑、基線腎風險、事件率與複合終點差異。FLOW 的「約 35% of components」與 SOUL 約 71% 複合事件組成定義不同，不得計算比值。
- **建議圖說：** 「FLOW 與 SOUL 同時改變了族群、基線腎風險、劑量與途徑；SOUL 未達顯著不能被因果分解為口服途徑失敗。」
- **署名模板：** `Original project comparison; FLOW locators: Table 1 and Results, journal pp.112–115, Supplement Table S2 p.24; SOUL data: official structured abstract, PMID 41380027. No publisher table/figure reproduced.`

### VR-14｜P1｜內分泌科 vs 腎臟科：同一證據的優先問題矩陣

- **精確來源：** 本專案 `16_FINAL_SYNTHESIS_ZH_TW.md` §16「內分泌科與腎臟科：同一證據，優先提問不同」及其 exact-locator 註記；亦對應 `13_CLINICAL_DECISION_FRAMEWORK.md` 的雙專科視角。
- **投影片目的：** 左欄呈現內分泌科常先問的 HbA1c、體重、ASCVD、低血糖與劑型；右欄呈現腎臟科常先問的 endpoint construction、eGFR/UACR 邊界、KRT、容量／營養與組合加成性；中央欄寫共同落點。
- **動作：** **REDRAW／本專案原創視覺。** 建議用三欄 bridge matrix，不取用任何期刊圖。
- **權利證據：** 這是本專案建立的分析框架；外部來源只支撐其中的事實，沒有重製外部圖表或大段文字。
- **公開 Git：** **可以。** 每列在講者 notes 或頁腳連到最接近的原始證據 locator。
- **私人學術演講：** 可以。
- **裁切指引：** 不可只顯示單一專科欄；若因版面拆成兩張，兩張都保留「共同、受證據限制的落點」，避免把它做成專科對立。
- **建議圖說：** 「內分泌科整合多面向治療價值；腎臟科守住腎終點、收案邊界與生理儲備。共同決策要先確認 FLOW 表現型，再排序殘餘風險。」
- **署名模板：** `Original synthesis by this project; evidence locators listed in 16_FINAL_SYNTHESIS_ZH_TW.md §16 and 13_CLINICAL_DECISION_FRAMEWORK.md.`

### VR-15｜P0｜表現型導向治療演算法與證據邊界

- **精確來源：** 本專案 `16_FINAL_SYNTHESIS_ZH_TW.md` §20，尤其「證據分級之表現型導向演算法」與該節 direct-locator index；安全監測另見同文 §§14、17–18。
- **投影片目的：** 形成結尾臨床流程：先確認 T2D、eGFR/UACR、ASCVD/HF、肥胖／血糖需求、血鉀、容量與營養；再以 RASi／SGLT2i 為基礎，依殘餘風險與適應性考慮 finerenone／semaglutide；最後以 established／suggestive／unknown 標示證據。
- **動作：** **REDRAW／本專案原創流程圖。** 不借用 AHA CKM guideline 圖、KDIGO heat map 或藥廠演算法。
- **權利證據：** 流程是本專案的原創臨床綜整，底層數值與邊界逐項引用；沒有外部圖像重製。
- **公開 Git：** **可以。** 必須保留來源索引、非個人醫療建議聲明與超界療效標籤。
- **私人學術演講：** 可以。
- **裁切指引：** 不可裁掉三個安全出口：`eGFR<25／維持性透析＝FLOW efficacy unknown`、`baseline SGLT2i/MRA subgroup ≠ additive proof`、`1.0 mg SC FLOW claim ≠ 2.4 mg SC SELECT or 14 mg oral SOUL equivalence`。
- **建議圖說：** 「不是硬排第 3、4 線，而是依表現型與殘餘風險分流；每一藥物只在其相符族群與終點上承擔已證實主張。」
- **署名模板：** `Original clinical synthesis by this project; primary locators indexed in 16_FINAL_SYNTHESIS_ZH_TW.md §20. No guideline or publisher figure reproduced.`

## 三、備選與明確禁用清單

| 來源／候選圖 | 精確 locator | 決定 | 理由與可接受替代 |
|---|---|---|---|
| `SUSTAIN6-PIONEER6-EGFR-NDT-2025` Figure 1 | `PDF p.4 / journal p.355` | **備選；REDRAW 優先** | CC BY-NC 4.0（證據在 PDF p.1）；只適合非商業版，且為 pooled post hoc slope，不是硬腎終點。若用，畫一張全新 slope summary 並標示 `post hoc`，不要塞入三張相似 forest。 |
| `FLOW-DESIGN-2023` Figure 4 | `PDF p.9 / journal p.2049` | **原圖 NO-USE** | 圖說載明 adapted from KDIGO，嵌套權利未清。改用 VR-02 的原創 eligibility matrix／比例條。 |
| `CKM-GUIDELINE-2026` 任何表圖 | cached PDF 共 208 頁 | **NO-USE** | AHA author manuscript 明確限制 copying、modification、distribution；另有受限解析事件。只從官方 AHA 頁面重新核實後短篇幅轉述，不仿製 guideline algorithm。 |
| `SOUL-KIDNEY-2026` Figures 1–3 | cached `PDF pp.5–7` | **NO-USE** | ADA NOASSERTION＋TDM/ML 權利事件。只用官方 PubMed／期刊頁面的已核實摘要事實，依 VR-13 全新重繪。 |
| `FDA-LABEL-OZEMPIC-PI-2025` 原標籤圖／表 | cached 57-page 10/2025 label | **NO-USE** | Sponsor-authored proprietary、NOASSERTION、已被 2026 S-038 supersede，且曾錯誤以 government-work 假設解析。法規投影片改用三法域純文字比較，並以現行官方頁面核實。 |
| `COMBO-MODEL-NEUEN-2024` 本機衍生圖／表 | `fulltext/glp1_cardiorenal_Neuen_2024.md` | **NO-USE 原衍生圖** | Front matter 雖聲稱 accepted manuscript CC BY 4.0，但取得／授權鏈未獨立登錄。需要模型概念時，只用 PubMed structured abstract 核實的事實做全新示意，並標示 modeled、非 semaglutide 專屬、FLOW 未納入模型。 |
| `MISFETCH-GRADE-CGM-2026` | quarantine PDF/Markdown | **永久 NO-USE** | 文件身分錯誤且另有 ADA 權利事件；與 semaglutide CKD 主題無關，不可引用、索引或出現在簡報。 |
| `FLOW-HF-2024`／`FLOW-CVPHENOTYPE-2026` | abstract only；Crossref CC BY-NC-ND 4.0 | **不製作改作圖** | ND 不允許改作；全文圖未取得。可用正式摘要數值做極簡原創文字卡，但不聲稱為原圖改作，亦不推論摘要未報告的表格內容。 |

## 四、製作時的署名與 QA 清單

### CC BY 4.0 截圖／改作

同頁至少包含：作者、期刊、年份、Figure 編號、DOI、`CC BY 4.0`、授權連結、變更說明。建議句型：

> Adapted from [authors], [journal/year/pages], Fig. X, DOI […], CC BY 4.0. Changes: cropped, zh-TW labels, highlighting.

完全未裁切、未翻譯、未著色才可用 `Reproduced from`；只要有任何改動即用 `Adapted from`。

### CC BY-NC 4.0

在上述欄位之外加 `Non-commercial use only`。簡報匯出前由負責人確認該版本不會進入商業課程、收費活動、贊助內容或其他營利用途；若無法確認，換成不描摹原圖的事實重繪。

### 非 CC 的數據重繪

同頁明寫 `Data redrawn from …; original figure/table not reproduced.`，並做到：

- 只選臨床問題需要的列，不搬整表；
- 使用本專案字型、配色、排序與資訊階層；
- 不沿用原刊圖示、線型、圖例位置或 panel 配置；
- HR、95% CI、事件數、interaction P、endpoint definition 與推論層級皆逐一核對；
- 對未校正、post hoc、exploratory、not powered、unknown 加明顯標籤。

### 最終逐圖檢查

- [ ] 圖檔是從官方來源重新取得，或是本專案原創；不是快取解析／舊裁切。
- [ ] exact locator 同時寫 Figure/Table 與頁碼；XML 來源寫 DOI＋PMCID。
- [ ] license evidence 已在來源頁面／PDF 重新查看，且沒有被個別 credit line 排除。
- [ ] 投影片同頁已有 attribution、license、link 與 changes statement。
- [ ] 公開 Git eligibility 與實際發布情境一致；CC BY-NC 未被帶入商業版本。
- [ ] 沒有來源 PDF、全文 Markdown、快取、報表尾端噪音或受限解析被打包。
- [ ] NEJM Table 3 使用 `journal p.120 / PDF p.12`，未沿用錯誤的 p.117。
- [ ] SGLT2i 與 MRA 次族群皆寫成「未偵測到異質性／加成性未知」，不是「證明一致／證明加成」。
- [ ] 透析圖明寫 selected survivor/continuation cohort，沒有轉成起始用藥療效。
- [ ] 內分泌科與腎臟科觀點並列，沒有以視覺階層把任一方貶為次要。
