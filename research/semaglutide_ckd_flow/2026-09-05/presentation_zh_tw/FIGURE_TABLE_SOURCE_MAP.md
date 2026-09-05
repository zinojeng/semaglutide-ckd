# 01｜演講投影片數據定位與證據矩陣（繁體中文）

> 核對日期：2026-09-05（Asia/Taipei）<br>
> 用途：將五篇主文與 `16_FINAL_SYNTHESIS_ZH_TW.md` 中的主要數字，逐一連回可驗證的表格、圖、頁碼與本機定位，供後續投影片、圖說、演講稿與文章交叉引用使用。<br>
> 本工作項目只做證據定位與視覺規劃；**未擷取、未生成任何截圖，也未改動來源全文、PDF、主文或證據總表**。

## 一、定位與引用規則

1. 「本機 PDF 頁」一律採 PDF 閱讀器顯示的 **1-based page**；「期刊頁」則是頁面印刷頁碼，兩者不可混寫。
2. 複合終點必須在投影片上明列組成，特別是 FLOW 的五成分主要終點含 **CV death**；四成分腎臟專一終點則不含 CV death。
3. 證據狀態固定分為：主要／確認性、預先指定支持性、預先指定次族群、探索性／事後、摘要層級、模型推估。沒有顯著交互作用只代表「未偵測到異質性」，不等於等效或加成已證實。
4. ARR/NNT 僅使用原始研究在相同終點、相同時間點正式報告者；不從不相容的事件比例自行回推。
5. 跨試驗表只用來說明族群、終點與背景治療差異；**不得以 HR 或 eGFR slope 大小排名藥物**。
6. 外部簡報建議以「依原研究數值重繪」為主。SOUL 與 dialysis pooled analysis 的本機 Diabetes Care PDF 有明確著作權／TDM 限制，**不可直接截圖或重製原圖**；其他來源仍應在使用前再核對授權條款。

## 二、先修正的來源定位問題

### FLOW 安全性 Table 3 頁碼

- 正確位置：`FLOW-PRIMARY-2024` **Table 3，期刊 p.120，本機 `fulltext/FLOW.pdf` 第 12 頁**。
- 早期工作稿曾標成「期刊 p.117」；直接檢查 PDF 後確認，p.117／本機第 9 頁是 Safety Outcomes 敘述，**不是 Table 3**。
- `14_MASTER_EVIDENCE_TABLE.md`、文章索引、storyboard、speaker notes 與 chart data 現均已同步採 p.120／PDF p.12。

### CKD 嚴重度 Figure 2 數值

- `FLOW-CKDSEVERITY-2025` 的權威數值是期刊 **Figure 2，p.1103**；本機已於 2026-09-05 從 Europe PMC 重新取得官方 PMCID `PMC11931213` 的 JATS／PDF、記錄 SHA-256 並完成 Figure 2 視覺複核。早期 `fulltext/` 衍生檔只保留為歷史事件，不再作有效來源。
- 舊有快取轉錄曾誤置 eGFR≥60 與部分 KDIGO 分層估計值；投影片不得從舊稿複製，應使用本檔下列矩陣。

## 三、FLOW：研究設計、納入條件與基線

| 建議投影片／數據主張 | source_id | 精確來源定位 | 終點／時間／證據狀態 | 建議視覺 | 限制與講稿提醒 |
|---|---|---|---|---|---|
| **研究輪廓：N=3,533；semaglutide 1 mg SC weekly 1,767、placebo 1,766；中位追蹤 3.4 年** | `FLOW-PRIMARY-2024` | Table 1 與 Results—Trial Participants，期刊 pp.112–113；`fulltext/FLOW.pdf` pp.4–5 | 試驗族群／最終主要報告 | 16:9 試驗流程：篩選→1:1 隨機→事件驅動追蹤 | 設計論文早期版本報 N=3,534；最終主要報告為 3,533，無來源可證明差異原因，不要自行解釋成 enrolled／dosed 差異。 |
| **雙路徑 CKD 納入條件**：eGFR 50–75 且 UACR >300–<5,000，或 eGFR 25–<50 且 UACR >100–<5,000 mg/g；HbA1c≤10%；最大耐受／標示劑量 RASi | `FLOW-DESIGN-2023`; `FLOW-SUPPLEMENT-2024` | Design Table 1，期刊 p.2045／`research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/cache/pdfs/FLOW-DESIGN-2023_RossingNDT2023.pdf` p.5；Supplement Eligibility Criteria pp.12–13；primary Methods，期刊 p.110／`fulltext/FLOW.pdf` p.2 | 試驗資格／設計 | 兩條水平 eligibility lanes，右側加 RASi prerequisite | eGFR≥60 受試者上限為全體 20%；結果不可外推至未符合 UACR 條件的一般低蛋白尿 CKD。 |
| **排除透析／腎移植等族群，且 GLP-1RA 近期使用受限** | `FLOW-DESIGN-2023`; `FLOW-SUPPLEMENT-2024` | Design Table 1，期刊 p.2045／本機 PDF p.5；Supplement pp.12–13 | 研究外推範圍 | 「研究有涵蓋／未涵蓋」兩欄 | 不可把 FLOW 當成 dialysis efficacy trial；透析後證據另見 post hoc safety pool。 |
| **主要終點五成分**：持續 ≥50% eGFR 下降、持續 eGFR<15、慢性 KRT、腎死、CV death；確認性次要依序 total eGFR slope→MACE→全因死亡 | `FLOW-PRIMARY-2024`; `FLOW-DESIGN-2023`; `FLOW-SUPPLEMENT-2024` | Primary Methods，期刊 p.111／`fulltext/FLOW.pdf` p.3；Design Table 2，期刊 p.2046／本機 design PDF p.6；Supplement Trial Outcomes p.14 | 主要＋階層式確認性終點 | 五瓣構成環＋右側階層箭頭 | 五成分列是重疊事件列，不能當互斥的 first-event partition；CV death 約占「components」35% 也不是治療效果占比。 |
| **基線腎臟負荷**：平均 eGFR 47.0；eGFR ≥60／45–<60／30–<45／<30 為 20.4%／29.9%／38.4%／11.3%；中位 UACR 567.6 mg/g；A1/A2/A3 3.1%／28.4%／68.5%；KDIGO very high 68.3%、high 24.9%、low/moderate 6.8% | `FLOW-PRIMARY-2024`; `FLOW-DESIGN-2023`; `FLOW-CKDSEVERITY-2025` | Primary Table 1，期刊 pp.112–113／`fulltext/FLOW.pdf` pp.4–5；Design Table 3 與 Fig.4，期刊 pp.2048–2049／design PDF pp.8–9；Mahaffey Results/Table 1，PMCID PMC11931213 | 基線描述 | 重新繪製 KDIGO heat map＋右側三個大數字 | A1 的少數個案是 baseline reclassification，不代表依 protocol 招募了持續低 UACR 族群。 |
| **基線代謝／人口**：平均 66.6 歲、女性 30.3%、HbA1c 7.8%、BMI 32 kg/m² | `FLOW-PRIMARY-2024` | Table 1，期刊 pp.112–113／`fulltext/FLOW.pdf` pp.4–5 | 基線描述 | 四張 demographic stat cards | 族群以白人為主，外部效度要在講稿交代。 |
| **背景藥物**：ACEi 35.1%、ARB 60.2%、SGLT2i 15.6%、MRA 7.3%（finerenone 0）、insulin 61.4%、lipid-lowering 80.2% | `FLOW-PRIMARY-2024`; `FLOW-MRA-2025` | Primary Table 1，期刊 pp.112–113／PDF pp.4–5；MRA paper local lines 73–79／Table 1；`fulltext/glp1_cardiorenal_Rossing_2025.md` lines 75–79 | 背景治療 | RASi 作底座、SGLT2i/MRA 疊層的 stacked therapy diagram | 低 SGLT2i 使用率反映招募年代；0 位 baseline finerenone 使用者，不能宣稱 semaglutide＋finerenone 的硬終點加成已驗證。 |
| **基線 CV 負荷**：既往 MI 或 stroke 22.9%、heart failure 19.2%；另依 2026 CV phenotype 定義之 ASCVD 1,198/3,533（33.9%） | `FLOW-PRIMARY-2024`; `FLOW-CVPHENOTYPE-2026` | Primary Table 1，期刊 pp.112–113／PDF pp.4–5；CV phenotype structured abstract，PMID 42233552 | 基線描述；ASCVD 為後續預先指定 phenotype 定義 | kidney/CV overlap Venn diagram | 「既往 MI/stroke」與「ASCVD phenotype」定義不同，不可視為分母或事件完全相同。 |
| **事件驅動與提前停止**：原定 854 events；約 570 events 時中期分析；最終 741 events；主要終點 nominal two-sided α=0.0322 | `FLOW-SUPPLEMENT-2024` | Interim-analysis／hierarchy pp.16–17；SAP §2.1 pp.6–7、§2.3.1 p.12、§2.4.1 pp.17–18；primary Results p.113／PDF p.5 | 統計設計／主要終點有 group-sequential adjustment | 854→570→741 的水平時間軸 | 只有主要終點使用 group-sequential 調整；確認性次要階層未另作 GSD adjustment。早停可能限制長期估計精度。 |

## 四、FLOW：主要、腎臟、UACR、心血管結果

| 建議投影片／數據主張 | source_id | 精確來源定位 | 終點／時間／證據狀態 | 建議視覺 | 限制與講稿提醒 |
|---|---|---|---|---|---|
| **五成分主要終點**：331/1,767（18.7%）vs 410/1,766（23.2%）；5.8 vs 7.5/100 patient-years；HR 0.76（0.66–0.88），P=.0003；原文 3 年 NNT 20（14–40） | `FLOW-PRIMARY-2024` | Fig.1A，期刊 p.114／`fulltext/FLOW.pdf` p.6；Table 2，期刊 p.116／PDF p.8；NNT Results，期刊 p.115／PDF p.7 | 主要確認性；中位追蹤 3.4 年；NNT 時點 3 年 | 首選：重繪 cumulative-incidence curve；右側 HR＋NNT callout | 標題必須寫「含 CV death」。NNT 是來源報告值，不與其他試驗自行比較。 |
| **持續 ≥50% eGFR 下降**：165（9.3%）vs 213（12.1%）；HR 0.73（0.59–0.89） | `FLOW-PRIMARY-2024` | Table 2，期刊 p.116／PDF p.8；Supplement Table S2 p.24 | 主要終點成分；支持性 | 五成分 forest plot 第一列 | 不是獨立 multiplicity-protected confirmatory endpoint；不計算 component NNT。 |
| **持續 eGFR<15**：92（5.2%）vs 110（6.2%）；HR 0.80（0.61–1.06） | `FLOW-PRIMARY-2024` | Table 2，期刊 p.116／PDF p.8；Supplement Table S2 p.24 | 主要終點成分；支持性 | 同一張 component forest plot | CI 跨 1；不能宣稱單項顯著。 |
| **慢性 KRT**：87（4.9%）vs 100（5.7%）；HR 0.84（0.63–1.12）；**腎死** 5 vs 5，HR 0.97（0.27–3.49） | `FLOW-PRIMARY-2024` | Table 2，期刊 p.116／PDF p.8；Supplement Table S2 pp.24–25 | 主要終點成分；支持性 | 同一張 component forest plot，腎死用淡色 | 事件少且 CI 寬；不可說已證明降低 dialysis 或 kidney death。 |
| **CV death**：123（7.0%）vs 169（9.6%）；HR 0.71（0.56–0.89） | `FLOW-PRIMARY-2024`; `FLOW-SUPPLEMENT-2024` | Table 2，期刊 p.116／PDF p.8；Supplement Table S2 p.24 註記 CV death 約占 components 35% | 主要終點成分；支持性 | component forest 中以不同色框住 CV death；旁列「複合終點含 CV death」 | 約 35% 是 Table S2 對 component burden 的近似描述，不是互斥 first-event 比例，也不是 24% 效果中有 35% 由 CV death 驅動。 |
| **四成分腎臟專一終點（不含 CV death）**：218（12.3%）vs 260（14.7%）；HR 0.79（0.66–0.94） | `FLOW-PRIMARY-2024` | Fig.1B，期刊 p.114／PDF p.6；Table 2，期刊 p.116／PDF p.8 | 預先指定支持性；不在確認性階層 | 與五成分終點並排的兩列 dumbbell／forest | 不可稱「主要腎臟終點」；證據庫沒有已發表 NNT，禁止由粗略比例回推。 |
| **total eGFR slope**：−2.19 vs −3.36 mL/min/1.73m²/year；差 +1.16（0.86–1.47），P<.001 | `FLOW-PRIMARY-2024` | Fig.1D，期刊 p.114／PDF p.6；Table 2，期刊 p.116／PDF p.8 | 第一個階層式確認性次要終點；全追蹤期 | 重繪兩條 eGFR trajectory；右側 slope difference | slope 與 time-to-event HR 不可放在同一數值尺度比較。 |
| **至第 12 週無 semaglutide-specific differential acute dip**：baseline→week 12 絕對變化 −1.07 vs −1.05；差 −0.03（−0.56–0.51）；chronic week 12→end slope −2.36 vs −3.30，差 +0.94（0.62–1.26） | `FLOW-PRIMARY-2024` | Fig.1D／Results，期刊 pp.114–115／PDF pp.6–7；Table 2 p.116／PDF p.8 | 預先指定支持性 slope 分解 | 放大前 12 週 inset，再接 chronic slope | acute row 是「12 週絕對變化」，不是每年 slope；不可誤標 `/year`。本證據庫沒有更早時點，不能排除此前已消退的 transient dip。 |
| **week 104 cystatin-C eGFR 差** +3.39（2.63–4.15）；creatinine counterpart +3.30（2.43–4.17，post hoc） | `FLOW-PRIMARY-2024` | Table 2，期刊 p.116／PDF p.8；Results p.115／PDF p.7 | cystatin-C 為預先指定支持性；creatinine counterpart 事後 | 小型 concordance panel（creatinine vs cystatin C） | 差值 CI 未報，不能量化一致性；只降低 pure weight/muscle-loss creatinine-generation artifact 疑慮，不排除一般測量誤差，也不證明體重獨立。 |
| **UACR week 104**：ratio 0.60 vs 0.88；ratio-of-ratios 0.68（0.62–0.75），即相對低約 32%（25–38） | `FLOW-PRIMARY-2024`; `FLOW-SUPPLEMENT-2024` | Table 2，期刊 p.116／PDF p.8；Supplement Fig.S2A p.19（圖說延續 p.20） | 預先指定支持性 surrogate；week 104 | 重繪 log-scale UACR trajectory 或 32% 大數字＋CI | 不可稱 hard kidney outcome；ratio-of-ratios 不等於 32 percentage-point absolute reduction。 |
| **MACE**：212（12.0%）vs 254（14.4%）；HR 0.82（0.68–0.98），P=.029 | `FLOW-PRIMARY-2024` | Fig.1E，期刊 p.114／PDF p.6；Table 2，期刊 p.116／PDF p.8 | 第二個階層式確認性次要終點；中位 3.4 年 | 重繪 KM curve 或 CV outcomes 三格卡 | 次要終點未另作 group-sequential adjustment；P 值按原文呈現。 |
| **全因死亡**：227（12.8%）vs 279（15.8%）；HR 0.80（0.67–0.95），P=.01 | `FLOW-PRIMARY-2024` | Fig.1F，期刊 p.114／PDF p.6；Table 2，期刊 p.116／PDF p.8 | 第三個階層式確認性次要終點；中位 3.4 年 | 與 MACE 並排的 outcome card | 不可把全因死亡與 CV death 重複加總。 |
| **week 156 絕對效果**：MACE RD −0.02（−0.04, −0.002），NNT 45（23–623）；全因死亡 RD −0.03（−0.05, −0.004），NNT 39（21–238） | `FLOW-CKDSEVERITY-2025` | Methods—Statistical analysis 與 Table 2 後 Results，期刊 pp.1103–1106；PMCID PMC11931213 | 全試驗、week 156；預先指定分析 | 兩個 100-person icon arrays 或 RD/NNT cards | **不是** FLOW primary Table 2 的數值，也不是 CKD strata-specific NNT；CI 很寬，講稿要說不確定性。 |
| **week 104 其他代謝變化**：體重差 −4.10 kg、HbA1c 差 −0.81 percentage point、SBP 差 −2.23 mmHg | `FLOW-PRIMARY-2024` | Table 2，期刊 p.116／PDF p.8；Supplement Fig.S2 pp.19–20 | 支持性 mechanistic/context measures | 三張小卡，置於主結果後而非主結論頁 | 不能由同時改善直接推斷腎效益的中介比例或腎臟直接 GLP-1R 機轉。 |
| **主要結果穩健性**：敏感度分析 HR 約 0.75–0.77 | `FLOW-SUPPLEMENT-2024` | Table S3 pp.26–27 | 預先指定／支持性 sensitivity analyses | appendix forest／range bar | 只證明對分析假設相對穩健，不消除早停、外推性或 endpoint-composition 限制。 |

## 五、FLOW：CKD 嚴重度、SGLT2i、MRA 與 CV 次族群

| 建議投影片／數據主張 | source_id | 精確來源定位 | 終點／時間／證據狀態 | 建議視覺 | 限制與講稿提醒 |
|---|---|---|---|---|---|
| **MACE by CKD severity**：overall 0.82（0.68–0.98）；eGFR<60 0.87（0.71–1.06）vs ≥60 0.59（0.37–0.94），P-int=.13；UACR<300 1.04（0.72–1.51）vs ≥300 0.75（0.61–0.93），P-int=.13；KDIGO low/mod 0.67（0.27–1.67）、high 0.75（0.50–1.12）、very high 0.84（0.68–1.04），P-int=.79 | `FLOW-CKDSEVERITY-2025` | Published Fig.2，期刊 p.1103；PMCID PMC11931213；官方原圖另見 `public_assets/` | 預先指定 MACE 次族群 | 依原圖重繪 forest；把 P-interaction 放在每個 subgroup family 末端 | 多數單一層級 CI 跨 1；「一致」應講成未偵測到異質性，不是每層都各自顯著。 |
| **兩個名目交互作用**：全因死亡 UACR<300 HR 1.17（0.83–1.65）vs ≥300 0.70（0.57–0.85），P-int=.01；非致死 MI eGFR<60 0.94（0.63–1.39）vs ≥60 0.28（0.09–0.87），P-int=.04 | `FLOW-CKDSEVERITY-2025` | Figs.3–4／Results，期刊 pp.1104–1106；PMCID PMC11931213 | 探索性解讀；15 個未多重校正交互作用中的 2 個 | appendix「signal vs multiplicity」警示頁 | 作者認為可能是偶然；不可選擇性宣稱高 UACR 或高 eGFR 有確定更佳療效。 |
| **更低 eGFR**：eGFR<30 n=400，73/218 vs 67/182，HR 0.81（0.58–1.13）；全 eGFR strata P-int=.83 | `FLOW-CKDSEVERITY-2026-CJASN` | Fig.1；official PMC full text，PMCID PMC13143484；SOURCE_LEDGER 對應列 | 主要終點嚴重度分析預先指定；2026 paper | forest plot 的 eGFR<30 zoom-in | subgroup 未充分 power；CI 跨 1，不可說 advanced CKD 子群已獨立證實顯著。 |
| **baseline-reclassified UACR<100**：n=350，13/177 vs 17/173，HR 0.70（0.34–1.44）；全 UACR strata P-int=.42；UACR≥2,000 的全因死亡 HR 0.47（0.31–0.70），P-int=.02 | `FLOW-CKDSEVERITY-2026-CJASN` | Primary by UACR Fig.2；mortality Fig.5；PMCID PMC13143484 | 前者預先指定嚴重度分析；mortality-by-severity 事後 | 只放 appendix，使用虛線 CI | UACR<100 是 baseline reclassification，protocol screening 原要求 >100 或 >300；不是持續低蛋白尿前瞻性 cohort。mortality signal 為未校正事後結果。 |
| **baseline SGLT2i 使用者** n=550（277/273），primary 41 vs 38，HR 1.07（0.69–1.67）；非使用者 n=2,983（1,490/1,493），290 vs 372，HR 0.73（0.63–0.85）；P-int=.109 | `FLOW-SGLT2-2024` | Fig.1、Fig.2；`fulltext/glp1_cardiorenal_Mann_2024.md` lines 30–48、116–128、218–223、232–241 | 預先指定 baseline subgroup；中位 3.4 年 | forest＋事件數，不建議只放 HR | 使用者層只有 79 個 primary events；非 factorial randomization。1.07 的寬 CI 同時相容增益、無效或傷害；P-int 不顯著不證明加成。 |
| **SGLT2i subgroup 四成分**：users 32/277 vs 27/273，HR 1.18（0.71–1.98）；non-users 186/1,490 vs 233/1,493，HR 0.75（0.61–0.90）；P-int=.100 | `FLOW-SGLT2-2024` | Fig.1B／Supplementary Table 2；local lines 64–69、127–128、218–224 | 預先指定支持性 subgroup | 與五成分並排兩列 forest | 同樣 event-limited；不得宣稱 background SGLT2i 下硬腎臟效益已確立。 |
| **≥50% eGFR component by SGLT2i**：users 30/277 vs 23/273，HR 1.30（0.76–2.26）；non-users 135/1,489 vs 190/1,493，HR 0.66（0.53–0.83）；P-int=.023 | `FLOW-SGLT2-2024` | Fig.2；local lines 251–257 | 單一成分、名目交互作用；未校正 | appendix forest，標記「hypothesis-generating」 | 孤立且未校正的 component interaction，不能據此宣稱與 SGLT2i 併用有害或無效。 |
| **SGLT2i subgroup eGFR/UACR**：total slope difference +0.75（−0.01–1.50）users vs +1.25（0.91–1.58）non-users，P-int=.237；week-104 UACR 相對低 24%（4–39）vs 34%（26–40），P-int=.279 | `FLOW-SGLT2-2024` | Fig.3／Table 1；local lines 73–84、399–450；UACR Extended Data Fig.7，local lines 99–103、1091–1182 | 預先指定 continuous/supportive subgroup | 兩個並排 effect bars（slope、UACR） | 不是加成試驗；後續 SGLT2i 啟用不對稱且為非隨機。 |
| **SGLT2i subgroup cystatin-C analysis**：修改五項 HR 0.74（0.47–1.16）vs 0.70（0.60–0.82），P-int=.844；slope difference +0.92（0.16–1.68）vs +1.55（1.21–1.88），P-int=.142 | `FLOW-SGLT2-2024` | Results／Table 1；local lines 411–450；Extended Data／Supplement locators in local file | 事後 cystatin-C analysis | appendix marker/endpoint-dependence table | 基線 SGLT2i 使用者之預設 creatinine-based 五項 HR 1.07 與修改 cystatin-C HR 0.74 是不同 estimand、位於無效線兩側；不可平均、拼成範圍或由後者推翻前者，亦不能證明 drug additivity。 |
| **baseline MRA** n=257（136/121；spironolactone 218、eplerenone 38、esaxerenone 1、finerenone 0）；primary 23/136 vs 36/121，HR 0.51（0.30–0.86）；非使用者 308/1,631 vs 374/1,645，HR 0.79（0.68–0.92）；P-int=.12 | `FLOW-MRA-2025` | Table 1／Fig.1／Supplementary Table 2；`fulltext/glp1_cardiorenal_Rossing_2025.md` lines 75–79、201–209 | 預先指定 subgroup；作者分析註明 exploratory／無 multiplicity protection | forest＋MRA composition donut | 樣本小且不是 finerenone subgroup；無顯著 interaction 不能證明加成。 |
| **MRA subgroup 3 年絕對效果（含 CV death 五項主要終點）**：RD −0.11（−0.20, −0.01）、NNT 9 users；RD −0.04（−0.07, −0.02）、NNT 23 non-users；四成分 HR 0.38（0.15–0.84）vs 0.82（0.68–0.99），P-int=.068；RRT P-int=.027、users 僅 11 events | `FLOW-MRA-2025` | Results／Figs.1–2／Supplementary Table 2；local lines 203–213 | 探索性 subgroup estimates | appendix absolute-effect bars；NNT 明標「含 CV death 五項、3 年、探索性 MRA 基線次族群」 | NNT 不是 trial-level、不是 kidney-only，且不得接在 finerenone 敘述旁；RRT 交互作用事件極少、未校正，不能作臨床排序。 |
| **MRA subgroup slope/UACR**：creatinine total-slope difference +1.38（0.21–2.54）users vs +1.15（0.83–1.46）non-users，P-int=.71；week-104 UACR 相對低 15%（−41–31）vs 33%（26–39），P-int=.22 | `FLOW-MRA-2025` | Fig.3／Supplementary Fig.6；local lines 223–231、237–241 | 探索性 continuous subgroup | two-panel effect plot | MRA-user UACR CI 很寬且跨無效值；不應宣稱明確相同。 |
| **trial 中 finerenone 新啟用僅 50 人**：22 semaglutide、28 placebo | `FLOW-MRA-2025` | Supplementary Table 3／local lines 215–219 | 非隨機、post-randomization exposure | 只作講稿註解，不建議主圖 | 不可用這 50 人推論 semaglutide＋finerenone 硬終點療效。 |
| **HbA1c≤7.0% vs >7.0%**：主要終點 HR 0.69（0.54–0.89）vs 0.80（0.67–0.96） | `FLOW-PRIMARY-2024` | Fig.2，期刊 p.118／`fulltext/FLOW.pdf` p.10；caption p.119／PDF p.11 | 預先指定 subgroup；forest 未提供正式 P-interaction | appendix forest／講稿一句 | 支持效益不只見於基線血糖較高者，但缺正式 interaction P，不能證明效果與 glycemia 無關。 |
| **CV phenotype（皆為含 CV death 五項主要終點、3 年探索性次族群 NNT）**：ASCVD n=1,198，HR 0.80（0.63–1.02）vs complement 0.74（0.62–0.89），P-int=.62，NNT 22；HF n=678，0.67（0.49–0.93）vs 0.79（0.67–0.93），P-int=.40，NNT 13；high-risk/no established CVD n=1,329/2,000，0.73（0.58–0.91）vs 0.73（0.49–1.08），P-int=.99，NNT 17 | `FLOW-CVPHENOTYPE-2026` | Structured abstract Results；DOI 10.1016/j.jacc.2026.02.5125；PMID 42233552 | 預先指定 subgroup；摘要層級；NNT 為 3 年描述性／探索性估計 | 三列 phenotype forest＋各自 NNT，逐列保留「含 CV death」 | 不是 kidney-only NNT；只適用這三個 CV phenotype，不可套到 KDIGO／UACR strata。差異可由 baseline risk 數學上充分解釋，但無表型別基線率可實證分解；無 interaction 不是 equivalence。 |
| **HF event or CV death** HR 0.73（0.62–0.87），P=.0005；HF events 0.73（0.58–0.92），P=.0068；CV death 0.71（0.56–0.89），P=.0036 | `FLOW-HF-2024` | Structured abstract Results；DOI 10.1016/j.jacc.2024.08.004；PMID 39217553 | 預先指定 secondary analysis；摘要層級 | 三列 compact forest | FLOW 不是 dedicated HF trial；NYHA、HFrEF/HFpEF 細分未在已驗證來源取得。 |

## 六、SELECT、SOUL、pooled 與類別層級證據

| 建議投影片／數據主張 | source_id | 精確來源定位 | 終點／時間／證據狀態 | 建議視覺 | 限制與講稿提醒 |
|---|---|---|---|---|---|
| **SELECT 族群**：N=17,604（8,803/8,801），obesity＋ASCVD、無已知糖尿病；semaglutide 2.4 mg SC | `SELECT-KIDNEY-2024`; `SELECT-GLYCEMIA-2024` | Abstract，期刊 p.2058／`research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/cache/pdfs/SELECT-KIDNEY-2024_ColhounNatMed2024.pdf` p.1；Methods PDF pp.10–11；glycemia structured abstract Results，PMID 38907683 | CVOT 的預先指定腎臟分析 | 「不同於 FLOW」population card | 劑量、族群與糖尿病狀態不同，不能直接外推到 T2D+CKD 1 mg；66.4% 為 prediabetes、33.5% normoglycemia，故「無糖尿病診斷」不等於無任何 glycemic pathway。 |
| **SELECT 五成分腎臟終點**：155（1.8%）vs 198（2.2%），HR 0.78（0.63–0.96），P=.02 | `SELECT-KIDNEY-2024` | Fig.1，期刊 p.2059／local PDF p.2；Fig.2，期刊 p.2060／PDF p.3 | 預先指定 secondary；事件驅動項含 incident macroalbuminuria | 重繪 KM＋component bars | 所有 P 未作 multiplicity adjustment；複合終點主要由 macroalbuminuria 與 ≥50% eGFR decline 支撐，硬末期事件稀少。 |
| **SELECT components**：kidney death 0 vs 0；KRT 4 vs 6，HR 0.66（0.17–2.32）；eGFR<15 5 vs 4，HR 1.24（0.33–5.02）；≥50% decline 12/8,724 vs 21/8,742，HR 0.57（0.27–1.14）；macroalbuminuria 144 vs 179，HR 0.80（0.64–1.00） | `SELECT-KIDNEY-2024` | Fig.2，期刊 p.2060／PDF p.3 | Components；支持性 | component lollipop，硬終點用灰色 | 不可把 composite HR 描述成 dialysis 或 kidney-death benefit。 |
| **SELECT eGFR**：week 104 −0.86 vs −1.61，差 +0.75（0.43–1.06）；total slope −0.78 vs −1.17，差 +0.39（0.30–0.48）；chronic week20→end 差 +0.29（0.18–0.40） | `SELECT-KIDNEY-2024` | Table 1，期刊 p.2062／PDF p.5；Fig.4，期刊 p.2063／PDF p.6 | 預先指定 continuous outcomes；week 104 | 重繪 trajectory＋三個 slope labels | eGFR<60 subgroup 兩組 week104 均上升（+5.28 vs +3.09；差 +2.19），可能含 regression to mean。 |
| **SELECT acute slope**：baseline→week16 European subset −2.41 vs −1.08，差 −1.33（−2.68–0.02），exact P=.0535；**UACR week104** +0.3% vs +12.3%，差 −10.7%（−13.2–−8.2） | `SELECT-KIDNEY-2024` | Table 1 p.2062／PDF p.5；Figs.4–5 pp.2063–2064／PDF pp.6–7 | Acute slope／UACR supportive | acute inset＋UACR bar | 表中 P 四捨五入 .05，但 exact .0535，屬不顯著；acute estimate 僅 European subset。UACR≥300 subgroup CI 跨 0（−31.4%，CI −54.9–4.3；P=.08）。 |
| **SELECT weight mediation 81%（41–120）** | `SELECT-KIDNEY-2024` | Results／mediation section；Table/Figure context in primary PMC article | 事後／中介分析；week104 eGFR change | 不建議主圖；appendix causal diagram | 只針對兩時間點 eGFR change，不是 hard endpoint 或 longitudinal slope；CI 可超過 100%，不可說「81% 腎保護一定由體重造成」。 |
| **SOUL 族群與 MACE**：N=9,650（4,825/4,825），T2D＋ASCVD及／或 CKD，oral semaglutide 14 mg，平均 eGFR 73.8，追蹤 47.5 個月；MACE 579（12.0%）vs 668（13.8%），HR 0.86（0.77–0.96），P=.006 | `SOUL-PRIMARY-2025`; `SOUL-KIDNEY-2026` | SOUL kidney paper Abstract，期刊 p.257／`research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/cache/pdfs/SOUL-KIDNEY-2026_MannDiabetesCare2026.pdf` p.2；primary structured abstract | Primary MACE confirmatory；kidney analysis paper contextual | population card＋MACE outcome card | UACR 未收集；與 FLOW 的 dedicated CKD population、route、dose 不同。 |
| **SOUL 五成分 kidney/CV-death composite**：403（8.4%）vs 435（9.0%），HR 0.91（0.80–1.05），P=.19；**四成分不含 CV death**：112（2.3%）vs 129（2.7%），HR 0.86（0.66–1.10），P=.22 | `SOUL-KIDNEY-2026` | Results，期刊 p.259／local PDF p.4；Fig.1／Table 1，期刊 p.260／PDF p.5 | 第一個腎臟 secondary 未通過；四成分亦未顯著 | 兩個 endpoint composition bars＋HR | 五成分中 CV death 比例約 71%，結構和 FLOW 的約 35% component note 不同；不能將兩者視為相同腎臟終點。 |
| **SOUL components**：≥50% decline 71 vs 86，HR 0.81（0.59–1.11）；eGFR<15 23 vs 33，0.69（0.40–1.16）；KRT 40 vs 48，0.82（0.54–1.25）；CV death 301 vs 320，0.93（0.80–1.09）；kidney death 1 vs 7，0.14（0.01–0.79） | `SOUL-KIDNEY-2026` | Table 1，期刊 p.260／local PDF p.5 | Individual components；exploratory after hierarchy | component forest，kidney death標示 n=8 | 個別成分極少／未做確認性推論；kidney-death HR 不可作單獨療效宣稱。 |
| **SOUL total eGFR slope**：−1.67 vs −2.06，差 +0.40（0.27–0.53），nominal P<.0001；eGFR<60 subgroup 差 +0.55（0.31–0.80） | `SOUL-KIDNEY-2026` | Results p.259／PDF p.4；Fig.2 p.261／PDF p.6；Fig.3 p.262／PDF p.7 | 主要 kidney secondary 未通過後，正式屬探索性 | 重繪 eGFR trajectory；加 hierarchy gate icon | 不能用 nominal slope 顯著覆蓋未顯著的 hard composite；SOUL PDF 不可截圖重製。 |
| **baseline SGLT2i in SOUL** n=2,596；五成分 users 79/1,296 vs 71/1,300，HR 1.10（0.80–1.52）；non-users HR 0.88（0.75–1.02），P-int=.204 | `SOUL-KIDNEY-2026` | Fig.3，期刊 p.262／local PDF p.7 | Subgroup；exploratory | appendix forest | 同樣不是 factorial combination trial；不可宣稱與 SGLT2i 併用無效。 |
| **SELECT＋FLOW＋SOUL pooled**：N=30,787；來源標示為含 CV death composite 973 vs 1,134，HR 0.84（0.77–0.91）；來源標示為 kidney-specific／排除 CV death 347 vs 416，HR 0.80（0.69–0.92） | `SELECT-FLOW-SOUL-POOLED-2026` | Structured abstract Findings；PMID 42567173；電子出版 2026-08-07 | Pooled individual-/trial-level aggregate analysis；摘要層級、ahead of print at cutoff；完整 component definitions 未列 | 三試驗 Venn＋兩個 pooled aggregate；**不畫 endpoint composition matrix** | 完整組成尚未逐項核實；不得與 FLOW／SOUL 排成 matched triplet 或暗示 like-for-like。族群、劑量與 route 亦異質；不是新的隨機 cohort。不要用原文尚未取得的圖。 |
| **GLP-1RA class meta-analysis（T2D）**：10 RCTs、N=67,769；kidney composite excluding CV death HR 0.82（0.73–0.93）；kidney failure 0.84（0.72–0.99）；MACE 0.87（0.81–0.93）；全因死亡 0.88（0.83–0.93） | `GLP1-CLASSMETA-BADVE-2025` | Structured abstract Findings；PMID 39608381 | 類別層級 meta-analysis；摘要層級 | class-level forest，FLOW 用註記標出 | 混合不同分子與 endpoint definitions；不能把 class estimate 指派給 semaglutide 單一藥物；kidney 結果受 FLOW 權重影響。 |
| **Class safety（含 SELECT 的 11 RCT、N=85,373）**：SAE RR 0.95（0.90–1.01），I²=88.5%；AE discontinuation RR 1.51（1.18–1.94），I²=96.3% | `GLP1-CLASSMETA-BADVE-2025` | Structured abstract Findings；PMID 39608381 | Post hoc inclusion of SELECT／class safety | benefit–burden balance scale | 異質性極高；僅能作類別背景，不取代 FLOW trial-specific safety。 |
| **直接但短期的 semaglutide＋canagliflozin RCT**：N=120、四臂各 30、24 週；併用組 UACR 降幅較大，eGFR 組間差異不顯著 | `SEMA-CANA-EARLYDKD-2026` | PubMed abstract Methods／Results；PMID 42170981；DOI 10.36721/PJPS.2026.39.7.204.1 | 小型四臂 randomized surrogate trial；摘要層級 | combination evidence ladder，置於 hard-outcome evidence 下方 | 摘要未報可獨立驗證的 exact UACR estimate；無 hard outcomes、短期且方法品質未完整評讀，不能證明加成腎保護。 |
| **finerenone 間接 combination evidence**：FIDELITY baseline GLP-1RA users n=944；triple background SGLT2i＋GLP-1RA n=167；uncontrolled RWE n=51、約 27 週 UACR −51.3%、eGFR −3.92、K⁺ +0.34 mmol/L | `FIDELITY-GLP1-2023`; `FIDELITY-TRIPLE-2026`; `FINERENONE-TRIPLE-RWE-2025` | FIDELITY GLP-1RA Results／Discussion，PMCID PMC10092103；triple Results／Supplementary Tables S1–S2，PMCID PMC12860910；RWE PubMed abstract Methods／Results，PMID 41303244 | 探索性 subgroup／surrogate／uncontrolled observational | 三階 evidence ladder，不畫 pooled effect | 問題方向是 finerenone 加在背景 GLP-1RA 上，且多非 semaglutide；baseline drugs 未隨機、無 hard endpoint、RWE 無 control，不能填補 semaglutide＋finerenone RCT 空白。 |
| **模型化三藥／四藥組合**：MACE HR 0.65（0.55–0.76），3y ARR 4.4%（3.0–5.7），NNT 23（18–33） | `COMBO-MODEL-NEUEN-2024` | PubMed structured abstract；DOI 10.1161/CIRCULATIONAHA.123.067584；PMID 37952217 | 完全加成假設模型；非 RCT | 若一定要用，只能畫成虛線「modeled scenario」 | 非 semaglutide-specific、FLOW 未納入模型、不是觀察到的 combination benefit；不可放在主結論頁。 |

## 七、安全性與晚期 CKD／透析後資料

| 建議投影片／數據主張 | source_id | 精確來源定位 | 終點／時間／證據狀態 | 建議視覺 | 限制與講稿提醒 |
|---|---|---|---|---|---|
| **整體 SAE**：877/1,767（49.6%）vs 950/1,766（53.8%） | `FLOW-PRIMARY-2024`; `FLOW-SUPPLEMENT-2024` | **Table 3，期刊 p.120／`fulltext/FLOW.pdf` p.12**；Supplement Table S4 p.28 | Trial safety；participants with ≥1 event | 100-person pictogram 或 horizontal bars | 使用 participant counts，不是事件總數；不要沿用錯誤 p.117 locator。 |
| **serious GI disorders**：5.4% vs 5.3% | `FLOW-SUPPLEMENT-2024` | Table S4 p.29；primary Safety narrative p.117／`fulltext/FLOW.pdf` p.9 | Trial safety；serious events | 與 GI discontinuation 並列但分開標示 | serious GI event 與「GI AE 導致停藥」是不同分類；前者相近不表示後者沒有耐受性負擔。 |
| **AE 導致永久停藥**：233（13.2%）vs 211（11.9%）；其中 GI-specific 79（4.5%）vs 20（1.1%） | `FLOW-PRIMARY-2024`; `FLOW-SUPPLEMENT-2024` | Primary Table 3，p.120／PDF p.12；Supplement Table S5 pp.32–33 | Trial safety；永久停藥 | overall 與 GI subset 的 nested bars | GI 是 overall discontinuation 的子集，不能相加；另有「任何原因永久停藥 26%」與 SGLT2 paper 28.8% 的定義／分母差異尚未釐清。 |
| **serious AKI preferred term**：124（7.0%）vs 123（7.0%）；**dehydration** 10（0.6%）vs 10（0.6%） | `FLOW-SUPPLEMENT-2024` | Table S4：renal/GI p.29；dehydration／eye p.30 | Trial safety | risk table，避免誇張比例圖 | 必須寫明 preferred term／事件分類；不要與所有 renal-disorder SAE 混用。 |
| **severe hypoglycemia**：至少一次者 37（2.1%）vs 37（2.1%）；episodes 47 vs 46，episode-count ratio 1.02（0.62–1.67） | `FLOW-PRIMARY-2024`; `FLOW-SUPPLEMENT-2024` | Primary Table 3 p.120／PDF p.12；Supplement Table S4 pp.28–31 | Trial safety | 兩列分開：participants、episodes | 單位不同；ratio 不是 time-to-event HR，禁止與 37/37 放在同一列當同一分母。 |
| **眼部／視網膜**：systematic retinopathy events 402（22.8%）vs 398（22.5%）；serious eye SOC 53（3.0%）vs 30（1.7%） | `FLOW-PRIMARY-2024`; `FLOW-SUPPLEMENT-2024` | systematic retinopathy：primary Safety narrative p.117／PDF p.9 與 Table 3 p.120／PDF p.12；serious eye SOC：Supplement Table S4 p.30 | Trial safety；不同事件分類 | 兩層 taxonomy diagram | 這兩列不是同一定義，不能說「retinopathy 3.0 vs 1.7%」。FLOW 非專門眼科 progression trial。 |
| **SUSTAIN-6 retinopathy complication signal**：50/1,648（3.0%）vs 29/1,649（1.8%），HR 1.76（1.11–2.78），P=.02 | `SUSTAIN6-2016`; `SUSTAIN6-RETINOPATHY-2018` | Primary publication secondary outcome Results；retinopathy analysis Methods §2.1.4／Results，PMCID PMC5888154 | 預先指定、外部裁定 secondary；未 multiplicity protected | safety-history timeline：SUSTAIN-6→FLOW | 不與 FLOW systematic-retinopathy percentage直接比較；快速 HbA1c 改善與既存 DR 是重要脈絡，但不能宣稱因果已完全證實。 |
| **gallbladder／pancreatitis**：acute gallbladder disease 1.8% vs 2.2%；acute pancreatitis 10（0.6%）vs 7（0.4%） | `FLOW-SUPPLEMENT-2024` | Table S4 pp.29–31 | Trial safety | 小型 balanced safety table | 事件少，僅描述，不下「保護」或「風險增加」結論。 |
| **較高 KDIGO risk 的 SAE 負荷較高**：SAE low/mod 38.2% vs 43.7%、high 42.8% vs 47.1%、very high 47.3% vs 52.5%；AKI/failure low/mod 3.3% vs 3.4%、high 4.9% vs 5.8%、very high 10.6% vs 12.1% | `FLOW-CKDSEVERITY-2025` | Table 2，期刊 p.1105／`research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/cache/pdfs/FLOW-CKDSEVERITY-2025_Mahaffey_EHJ2025_PMC11931213.pdf` p.10；local Markdown lines 133–140 | Prespecified safety by CKD severity；descriptive | 依 KDIGO risk 分層的 grouped bars | 不是經多重校正的 safety efficacy comparison；重點是基礎風險隨 CKD 嚴重度升高。 |
| **透析後 on-treatment pooled cohort**：來源報告 34,064 人中 307 人開始 dialysis；僅 165 人仍用 assigned drug（71 semaglutide／94 placebo）；SAE 32/71（45.1%）vs 54/94（57.4%）；永久停藥 8.5% vs 10.6%；MACE 9.7 vs 16.1、死亡 13.8 vs 18.1/100 person-years | `FLOW-DIALYSIS-SAFETY-2026` | Fig.1 local PDF p.4／期刊 p.1001；Table 1 p.5／p.1002；Table 2 p.6／p.1003；Fig.2 p.7／p.1004；`research/semaglutide_ckd_flow/2026-09-05/sources/retrieved/cache/pdfs/FLOW-DIALYSIS-SAFETY-2026_KleinDiabetesCare2026.pdf` | Post hoc pooled descriptive safety after dialysis initiation | **依數值重繪** patient-flow funnel＋descriptive table；不可截原圖 | 強烈 survivor／selection bias，非新起始療效試驗。四母試驗 nominal N 加總 34,084，與來源 denominator 34,064 差 20 人，原因未解。不能把「無需腎劑量調整」等同透析 efficacy 已證實。 |

## 八、腎臟保護試驗比較：只做情境化，不排名

| Trial／核心數字 | source_id | 精確來源定位 | 建議投影片視覺 | 比較時必講限制 |
|---|---|---|---|---|
| **FLOW** N=3,533；T2D；eGFR 25–75＋UACR 路徑；五成分含 CV death HR 0.76（0.66–0.88）；KRT HR 0.84（0.63–1.12）；CV death 0.71（0.56–0.89）；total/chronic slope difference +1.16／+0.94 | `FLOW-PRIMARY-2024` | Table 1 pp.112–113、Table 2 p.116、Figs.1–2 pp.114/118；local PDF pp.4–5、8、6/10 | 以「族群／主要終點／CV death 是否納入／背景治療」四欄比較 | 唯一 dedicated semaglutide kidney outcomes trial；單項 KRT 未顯著。 |
| **CREDENCE** N=4,401；T2D；primary HR 0.70（0.59–0.82）；ESKD 0.68（0.54–0.86）；CV death 0.78（0.61–1.00）；baseline→week3 **absolute eGFR change difference** −3.17（−3.87–−2.47），chronic slope +2.74（2.37–3.11） | `CREDENCE-2019`; `CREDENCE-EGFR-SLOPE-2020` | Primary Methods/Results，DOI 10.1056/NEJMoa1811744；slope Table 1，PMCID PMC7217416 | 同一情境矩陣，不畫勝負箭頭 | acute 值不是 `/year`；endpoint、SGLT2 mechanism 與 FLOW 不同。 |
| **DAPA-CKD** N=4,304；67.5% T2D；primary HR 0.61（0.51–0.72）；kidney-specific 0.56（0.45–0.68）；ESKD 0.64（0.50–0.82）；CV death 0.81（0.58–1.12）；total/chronic slope +0.93／+1.92 | `DAPA-CKD-2020`; `DAPA-CKD-BASELINE-2020` | Primary Methods/Results，DOI 10.1056/NEJMoa2024816；baseline Results/Table 4，PMCID PMC7538235 | 同一情境矩陣 | 含非糖尿病 CKD；UACR/eGFR 納入路徑、follow-up 與 endpoint 不同。 |
| **EMPA-KIDNEY** N=6,609；46% diabetes；primary HR 0.72（0.64–0.82）；kidney progression 0.71（0.62–0.81）；kidney failure composite 0.69（0.56–0.85）；CV death 0.84（0.60–1.19）；total/chronic slope +0.75／+1.37 | `EMPA-KIDNEY-2023` | Primary PMC Tables 1–2、Figs.3/S6，PMCID PMC7614055 | 同一情境矩陣 | 納入較低 albuminuria、非糖尿病與不同 eGFR 範圍；不可用 HR 大小作 head-to-head 推論。 |
| **FIDELIO-DKD** N=5,734；primary kidney composite（不含 CV death）HR 0.82（0.73–0.93）；kidney failure 7.3% vs 8.3%；CV death 4.5% vs 5.3%（NS）；chronic slope −2.66 vs −3.97，差約 +1.31 | `FIDELIO-DKD-2020` | Primary Results＋prespecified slope；DOI 10.1056/NEJMoa2025845；PMID 33264825 | 同一情境矩陣 | finerenone 有 initial dip；FLOW baseline finerenone=0，不能由跨試驗拼出 combination efficacy。 |
| **FIDELITY** N=13,026；kidney composite（不含 CV death）HR 0.77（0.67–0.88）；CV composite 0.86（0.78–0.95）；ESKD 0.80（0.64–0.99）；CV death 0.88（0.76–1.02） | `FIDELITY-POOLED-2022` | PMC Tables 1–2、Figs.1–3，PMCID PMC8830527 | 同一情境矩陣 | pooled finerenone program；主要 pooled paper未提供本矩陣可用 slope。 |

### 比較投影片建議結構

- 橫向欄位：`Trial / 族群 / eGFR-UACR / 主要終點組成 / CV death 是否納入 / 背景 RASi-SGLT2i-GLP-1RA / follow-up`。
- HR、slope 可留在附錄，不要放置「第一名／最強」排序符號。
- 講稿固定句：**「這是 endpoint 與 population 的情境化比較，不是 head-to-head efficacy ranking。」**

## 九、後續影像／圖表製作清單（本輪未執行截圖）

| 優先度 | 候選原始位置 | 後續用途 | 建議處理 | 權利／品質提醒 |
|---|---|---|---|---|
| P0 | FLOW Fig.1，期刊 p.114／`fulltext/FLOW.pdf` p.6 | 主要終點、eGFR、MACE、死亡總覽 | 依數值重繪；可拆成 2–3 張，不把六 panel 塞同頁 | 外部使用前核對 NEJM 授權；維持 axis、risk table、competing-risk 說明。 |
| P0 | FLOW Table 2，期刊 p.116／PDF p.8 | 核心數據 source panel | 不直接貼整表；轉為一張 endpoint matrix＋一張 forest | 組成終點與 secondary status 要保留。 |
| P0 | FLOW Fig.2，期刊 p.118／PDF p.10（caption 延至 p.119／PDF p.11） | 主要終點 subgroup forest | 重新排版重繪；只保留演講需要的 strata | 原 caption 的 interaction test 與 censoring 說明不能遺失。 |
| P0 | FLOW Supplement Fig.S2 p.19（caption/method p.20） | UACR、weight、HbA1c、BP trajectories | 分拆重繪；UACR 以 log-compatible 表達 | 不可把 week104 ratio 畫成 absolute percentage points。 |
| P0 | FLOW Design Fig.2 p.2044／local design PDF p.4；Table 1 p.2045／p.5；Fig.4 p.2049／p.9 | 研究設計、eligibility、KDIGO heat map | 重繪成統一繁中資訊圖 | Design N=3,534 與 final N=3,533 的差異須另註。 |
| P1 | FLOW Supplement Tables S4–S5 pp.28–33 | safety appendix | 擷取數值後重製 compact safety table | participant/event/episode 單位逐列標示。 |
| P1 | Mahaffey Fig.2 p.1103 | CKD severity MACE forest | 可依 CC BY 4.0 來源規範做適當標示的 adaptation；仍建議統一風格重繪 | 必須使用已更正數值；caption 註明 adapted、作者、DOI、license。 |
| P1 | Mann SGLT2i Figs.1–3；local MD lines 218–315、399–450 | baseline SGLT2i subgroup | 重繪 forest＋slope，不貼滿版原圖 | 僅 79 primary events 的 caveat 要與圖同頁。 |
| P1 | Rossing MRA Figs.1–3；local MD lines 203–231 | MRA subgroup | 重繪，另加 MRA composition | 必須明示 finerenone=0。 |
| P1 | SELECT Figs.1–2／Table 1／Figs.4–5；期刊 pp.2059–2064／local PDF pp.2–7 | obesity/no-diabetes 對照證據 | 分成 composite、components、continuous 三張 | 外部使用前核對 license；所有 P 值未 multiplicity adjustment。 |
| P1 | SOUL Fig.1／Table 1／Fig.2；期刊 pp.260–261／local PDF pp.5–6 | oral semaglutide kidney context | **只依數值重繪，不截圖、不重製原圖** | Diabetes Care PDF 有著作權／TDM 限制；hierarchy failure 要在圖上標示。 |
| P2 | Dialysis pooled Fig.1／Table 2；期刊 pp.1001/1003／local PDF pp.4/6 | 透析後 selected on-treatment flow＋descriptive safety | **只重繪** patient funnel 與數值表 | 不可截圖；強調 post-randomization selection 與 denominator conflict。 |

## 十、文章內 reference 與投影片圖說範本

### 文章正文中的交叉引用

建議先在每篇文章內依出現順序編號，而不是沿用原論文圖號。正文可直接使用下列句型：

- 「FLOW 的五成分主要終點風險下降 24%，且該終點明確包含心血管死亡（見**圖 1**；`FLOW-PRIMARY-2024`, Fig.1A/Table 2）。」
- 「個別成分與不含心血管死亡的四成分腎臟終點整理於**表 1**（`FLOW-PRIMARY-2024`, Table 2）。」
- 「eGFR 全期與慢性斜率的差異見**圖 2**；基線至第 12 週未見 semaglutide-specific differential dip，但不能排除更早且已消退的 transient dip（`FLOW-PRIMARY-2024`, Fig.1D/Table 2）。」
- 「基線 SGLT2i 與 MRA 次族群的估計值見**表 2**；這些分析未證明組合治療的加成效果（`FLOW-SGLT2-2024`; `FLOW-MRA-2025`）。」
- 「SELECT、FLOW、SOUL 的族群與終點組成差異見**表 3**；此表只供情境化比較。」

### 表格 caption 範本

> **表 1．FLOW 主要與支持性腎臟終點。** 數值為 semaglutide 1.0 mg 每週皮下注射相對於 placebo；五成分主要終點包含心血管死亡，四成分腎臟專一終點則不含。資料來源：Perkovic et al., *N Engl J Med*. 2024;391:109–121，Table 2；Supplementary Tables S2–S3。DOI: 10.1056/NEJMoa2403347。重新整理／重繪；未自行計算未報告之 NNT。

> **表 2．FLOW 依基線 SGLT2i 或 MRA 使用分層的治療效果。** P-interaction 為異質性檢定；未顯著不等於等效或加成已確立。資料來源：Mann et al., *Nat Med*. 2024，Figs.1–3；Rossing et al., *Diabetes Care*. 2025，Figs.1–3。

### 圖片 caption 範本

> **圖 1．FLOW 五成分主要終點的累積發生率。** 主要終點由持續 ≥50% eGFR 下降、持續 eGFR<15 mL/min/1.73m²、慢性腎臟替代治療、腎因性死亡及心血管死亡組成。HR 0.76（95% CI 0.66–0.88）。依 Perkovic et al. 2024 Fig.1A/Table 2 數值重新繪製；非原圖截圖。

> **圖 2．FLOW 的 eGFR 全期與慢性斜率。** 前 12 週兩組 eGFR 絕對變化相近；week 12 至追蹤結束的 chronic-slope difference 為 +0.94 mL/min/1.73m²/year。依 Perkovic et al. 2024 Fig.1D/Table 2 重新繪製。

> **圖 3．MACE 效果依 CKD 嚴重度分層。** 點估計與 95% CI 取自 Mahaffey et al., *Eur Heart J*. 2025;46:1096–1108，Fig.2（p.1103），依 CC BY 4.0 條款標示為 adapted。P-interaction 未顯示顯著異質性；個別 strata 多數未具獨立統計顯著性。

### 投影片頁尾短引用

- 單一來源：`Source: Perkovic V, et al. N Engl J Med. 2024;391:109–121. Table 2. doi:10.1056/NEJMoa2403347.`
- 次族群：`Source: Mann JFE, et al. Nat Med. 2024;30:2849–2856. Figs 1–3. doi:10.1038/s41591-024-03133-0.`
- 重繪圖：`Adapted/replotted from [Author, Journal, Year, Figure/Table]; values unchanged.`
- 摘要層級：`Source: PubMed structured abstract, PMID XXXXXXXX; full-text figure not used.`

## 十一、建議的投影片敘事順序

1. **為何需要 FLOW**：殘餘腎臟與 CV 風險、過去 GLP-1RA 證據多由 albuminuria 驅動。
2. **誰進入 FLOW**：eligibility 雙路徑＋KDIGO heat map＋背景 RASi/SGLT2i/MRA。
3. **主要問題怎麼定義**：五成分含 CV death，另列四成分腎臟專一終點。
4. **主結果**：HR 0.76、3y NNT 20，配 cumulative-incidence 重繪圖。
5. **拆解結果**：components、eGFR acute/chronic、UACR，避免只講單一 24%。
6. **CV 與死亡**：MACE、全因死亡、CV death，另以 week156 NNT 呈現絕對效果。
7. **嚴重度與背景治療**：CKD severity、SGLT2i、MRA forest；每張同時顯示事件數與 P-interaction。
8. **semaglutide 證據全貌**：SELECT、SOUL、pooled、class meta；用 endpoint-composition matrix 解釋表面差異。
9. **安全與外推邊界**：GI discontinuation、眼部分類、AKI/dehydration、透析後 selected cohort。
10. **臨床定位**：以既有 RASi/SGLT2i/finerenone foundation 加上適應症與個別化考量；不宣稱未經驗證的組合加成。

## 十二、仍需保留為未解或不可越界的項目

- FLOW design paper N=3,534 vs primary report N=3,533：原因未由已核對來源建立。
- 任意原因永久停藥的 26% vs SGLT2i paper 28.8%：可能源於定義／分析集差異，但目前不可猜測。
- Dialysis pooled denominator 34,064 vs 四個母試驗 nominal N 合計 34,084：差 20 人，來源未說明。
- FLOW Supplement 的 CV death 約 35% 與 SOUL 約 71% 描述不同 endpoint structure；兩者都不是治療效果貢獻比例。
- 未出版的 kidney-specific NNT、CKD severity strata NNT、SGLT2i strata NNT 一律不自行計算。
- 任何「GLP-1RA 直接作用於腎臟 GLP-1 receptor」仍屬機轉不確定；視覺應用虛線標示假說，而非實線因果路徑。
- 所有截圖／圖片再利用在進入外部簡報前，需逐一做 license 與 attribution QA；本工作檔的頁碼只表示**精確可定位**，不自動代表有重製權。
