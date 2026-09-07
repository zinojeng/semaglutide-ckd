# 20｜Semaglutide × CKD：腎臟科演講 Cross Sessions 辯論整合

> 證據截點：2026-09-05；角色對話完成日：2026-09-07。本文以公開分支 commit `2a11a82` 的已調和證據包為共同底稿，由主編、腎臟科、臨床試驗方法學、CKM 臨床與演講者五個獨立 Claude Code 角色會話，完成六條「提問 → 挑戰 → 回應 → 方法檢查 → 演講轉譯 → 再答辯 → 裁決」鏈。這是 AI 角色交叉詰問，不是人類專家同儕審查，也不是本輪重新擷取或重新閱讀受限制原始全文。

## 這份文件要解決什麼

既有[完整繁中總論](./16_FINAL_SYNTHESIS_ZH_TW.md)回答「證據全貌」，[Wave 4 同儕校讀增補](./19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md)回答「哪些句子說得比證據更遠」。本篇再向前一步，把腎臟科聽眾最可能追問的爭點，整理成可直接排進演講的主軸、投影片、30–60 秒講稿與 Q&A。

本輪沒有把內部 session UUID、傳輸紀錄或逐字對話公開，也沒有把角色共識當成新證據。所有定量句仍回到來源 ID、分析層級與 exact locator；角色對話的作用，是找出值得辯論之處並收緊措辭。

## 一頁先講完：六項裁決

| 腎臟科會問的問題 | 最終裁決 | 演講證據標籤 |
|---|---|---|
| FLOW 是否已證明降低腎衰竭／洗腎？ | 已確立的是「含 CV death 的五項主要複合終點」與總 eGFR slope；排除 CV death 的四項腎臟專屬複合為支持性，個別 KRT／eGFR<15 未被單獨確認。 | **Established + supportive；不是 kidney-failure proof** |
| 已用 SGLT2i 或 finerenone，semaglutide 是否已證實加成？ | FLOW 整體效益成立；但基線 SGLT2i 次族群事件少、CI 寬，且基線 finerenone 使用者為 0，無法證明增量硬腎臟效益或固定四藥順序。 | **Incremental hard-kidney benefit unknown** |
| eGFR 20 或透析病人能否使用？ | FLOW 的起始療效證據下限是 eGFR 25。低於此界線或維持性透析起始用藥，須依現行標籤、指引、治療目標與個別判斷；透析後資料只提供高度選定續用者的描述性安全訊號。 | **PK／可處方性 ≠ efficacy** |
| eGFR、UACR 與 cystatin C 是否證明直接腎臟作用或獨立於減重？ | 多條腎臟訊號相互支持，但 UACR 不是已證實中介；marker concordance 只減少純 creatinine-generation artifact 疑慮，不能證明與體重／血糖無關。 | **Outcome strong；causal decomposition unknown** |
| 人體腎臟 GLP-1R 在哪裡、作用在哪一段 nephron？ | 人體受體定位文獻仍無共識。單一 validated-antibody 研究的 preglomerular vascular smooth-muscle 結果不可升格為全領域定論。 | **Mechanism suggestive／unsettled** |
| 哪一種 CKD 病人應優先使用？ | 證據最直接的對象是符合 FLOW 收案條件的 T2D＋albuminuric CKD；肥胖、血糖或 ASCVD 可增加使用 semaglutide 的臨床理由，但不證明腎臟效果更大。排序須由表現型、風險與耐受性決定，不由一個 HR 自動決定。 | **Phenotype-first；no universal ranking** |

## 全場最值得辯論的一題

> 對已接受最大可耐受 RASi＋SGLT2i、仍有 albuminuric CKD 的 FLOW-like 病人，semaglutide 是否已是「標準下一層腎臟保護」？

### 正方最強版本

- FLOW 是第一個以 T2D＋CKD 為目標族群、直接證實 semaglutide cardiorenal outcome 與 eGFR slope 的專屬結果試驗。
- 病人常同時具有肥胖、血糖、ASCVD 與死亡風險；只以單一 kidney-failure component 評價，會低估其整體臨床價值。
- 「組合硬終點證據未完成」不等於「臨床不應加藥」；可依病人仍存在的多面向風險作個別化選擇。

### 反方最強版本

- FLOW 招募年代只有 15.6% 於基線使用 SGLT2i；該 550 人次族群只有 79 個主要事件，不能把整體 HR 直接當成 RASi＋SGLT2i 上的增量效果。
- FLOW 的 baseline MRA 使用者主要是 steroidal MRA，finerenone 使用者為 0；沒有 semaglutide＋finerenone 的隨機硬終點加成證明。
- 主要終點含 CV death；若說成「第三層／第四層腎臟保護」，容易讓聽眾誤認已證實額外降低 KRT 或 kidney failure。

### 主編裁決

可以把 semaglutide 稱為 **FLOW-like 表現型中具 outcome evidence 的 cardiorenal 選項**，也可以依肥胖、血糖與 ASCVD 等共同目標提早使用；但不能稱為已由隨機試驗證實、在 RASi＋SGLT2i 或 finerenone 之上的固定下一層，也不能宣稱組合後的增量 hard-kidney benefit 已知。

**可直接講的 35 秒版本：**

> 「我會把 semaglutide 放進 CKM 治療工具箱，但不把它硬排成第三或第四名。FLOW 證實的是整體 FLOW-like 族群的 cardiorenal benefit；對已用 SGLT2 抑制劑的 550 人次族群，事件數少、信賴區間很寬，而 FLOW 沒有任何 baseline finerenone 使用者。因此，今天的加藥順序應由白蛋白尿、心衰竭、ASCVD、肥胖、血糖、血鉀、容量與耐受性共同決定，並公開說明組合的增量硬腎臟效益仍未知。」

## 主軸一｜先拆 endpoint：FLOW 證明的是什麼？

### 為何腎臟科聽眾會在意

「腎臟事件下降 24%」若不說終點組成，會把 CV death、eGFR decline、KRT 與 kidney death 混成同一件事。這是全場最應先處理的語言風險。

### 建議用一張圖講清楚

使用既有 [FLOW endpoint forest 重繪圖](./presentation_zh_tw/public_assets/redrawn/01_flow_endpoints_forest_zh_tw@2x.png)，依序指出：

1. 五項主要複合：331/1,767 對 410/1,766；HR 0.76（95% CI 0.66–0.88），**包含 CV death**。
2. 四項腎臟專屬複合：218/1,767 對 260/1,766；HR 0.79（0.66–0.94），**排除 CV death、支持性且位於確認性階層外**。
3. 個別慢性 KRT：HR 0.84（0.63–1.12）；持續 eGFR<15：HR 0.80（0.61–1.06）。個別腎衰竭組成未被單獨確認。
4. 三年 NNT 20（14–40）只屬含 CV death 的五項主要複合終點，不能改名為「預防一次透析的 NNT」。

### 方法學加值頁

主要比較的 HR 來自分層 Cox model；累積發生率以 Aalen–Johansen 方法處理未被該終點納入的死亡競爭事件。五項主要終點已把 CV death 定義為事件，因此不能再把 CV death 稱為該五項終點的 competing event。提前停止也值得放入 appendix：原規劃 854 個主要事件，約 570 事件時跨越預設 efficacy boundary，最終資料鎖定累積 741 事件。這不推翻結果，但限制較長期與稀少個別組成的精確度。

### 可直接講的 45 秒版本

> 「FLOW 的 headline 要完整念：semaglutide 降低的是『重大腎臟事件合併心血管死亡』的五項主要複合終點，HR 0.76。排除心血管死亡後，四項腎臟專屬複合 HR 0.79，方向一致，但它在確認性階層外，屬支持性結果。再往下拆，KRT 與持續 eGFR 低於 15 的信賴區間都跨 1。因此，我會說 FLOW 建立了 cardiorenal composite 與 eGFR slope 效益，不會把它縮寫成『已證實降低洗腎 24%』；NNT 20 也不是洗腎 NNT。」

### 聽眾挑戰與回答

**問：四項腎臟專屬終點的 CI 沒跨 1，為何不能說顯著？**

答：可以說 nominal 95% CI 未跨 1、結果支持腎臟效益；但它不在預設確認性階層中，也未受多重比較保護，所以推論標籤必須是 supportive，而不是 confirmatory。

**來源定位：** `FLOW-PRIMARY-2024`，Figure 1A–B，journal p.114；Results「Primary Outcomes」，p.115；Table 2，p.116；Methods「Statistical Analysis」，p.111；Discussion，pp.119–120。[DOI](https://doi.org/10.1056/NEJMoa2403347)／[PubMed](https://pubmed.ncbi.nlm.nih.gov/38785209/)。提前停止與檢定階層見 `FLOW-SUPPLEMENT-2024`，supplement pp.16–17、24–27；`FLOW-SAP-2023` §§2.1、2.3.1、2.4.1。

## 主軸二｜疊加治療：SGLT2i 與 finerenone 之後還知道多少？

### 必須並排的四個背景數字

FLOW 基線約 95% 使用 ACEi／ARB，但只有 15.6% 使用 SGLT2i、7.3% 使用 MRA，且 baseline finerenone 為 0。這不是否定 FLOW，而是界定它回答「整體標準照護上的療效」與「現代多藥疊加後的增量療效」之差別。

### SGLT2i 次族群的正確讀法

共同分母：baseline SGLT2i users n=550（277/273）；non-users n=2,983（1,490/1,493）。

| 分析 | Baseline SGLT2i users | Non-users | Interaction |
|---|---:|---:|---:|
| 五項主要複合，creatinine-based | HR 1.07（0.69–1.67）；41/277 vs 38/273 | HR 0.73（0.63–0.85）；290/1,490 vs 372/1,493 | P=.109 |
| 四項腎臟專屬複合 | HR 1.18（0.71–1.98）；32/277 vs 27/273 | HR 0.75（0.61–0.90）；186/1,490 vs 233/1,493 | P=.100 |
| Post hoc modified cystatin-C 五項終點 | HR 0.74（0.47–1.16）；事件數未於本公開證據表重列 | HR 0.70（0.60–0.82）；事件數未於本公開證據表重列 | P=.844 |

Users 層不是「證明無效」，而是 **效果未被辨識**：事件少、CI 同時容許獲益、無效與傷害。Creatinine-based 1.07 與 post hoc cystatin-C 0.74 使用不同 marker／endpoint estimand，不能平均、挑選或拼成範圍。持續 ≥50% eGFR decline component 的 nominal interaction P=.023 也不能單獨證明傷害或效果修飾。

### MRA 不等於 finerenone

Baseline MRA 次族群共 257 人、59 個主要事件，藥物以 spironolactone／eplerenone 為主，finerenone 為 0。即使點估計方向看似有利、interaction 未顯著，也不能改寫為「semaglutide＋finerenone 已證實加成」。

### 可直接講的 50 秒版本

> 「FLOW 不是 factorial add-on trial。基線 SGLT2 抑制劑使用者只有 550 人，主要事件 79 件；creatinine-based HR 1.07 的區間從 0.69 到 1.67，應讀成資訊不足，不是中性，也不是傷害。事後 cystatin-C 修正版 HR 0.74 回答的是不同 estimand，不能拿來覆蓋 1.07。MRA 分析也不能替 finerenone 背書，因為 baseline finerenone 使用者是零。最誠實的結論是：各藥生物學與臨床目標可能互補，但 semaglutide 加在 SGLT2i 或 finerenone 上的增量硬腎臟效益尚未被直接隨機證明。」

### 視覺與來源

- 投影：[SGLT2i forest 重繪圖](./presentation_zh_tw/public_assets/redrawn/03_flow_sglt2_subgroup_forest_zh_tw@2x.png)與 [MRA forest 重繪圖](./presentation_zh_tw/public_assets/redrawn/04_flow_mra_subgroup_forest_zh_tw@2x.png)。
- `FLOW-SGLT2-2024`，Figures 1–2、Table 1、Extended Data Figures 4–7、Results。[DOI](https://doi.org/10.1038/s41591-024-03133-0)／[PubMed](https://pubmed.ncbi.nlm.nih.gov/38914124/)。
- `FLOW-MRA-2025`，Figures 1–2、Supplementary Tables 1–2、Results。[DOI](https://doi.org/10.2337/dc25-0472)／[PubMed](https://pubmed.ncbi.nlm.nih.gov/40730031/)。

## 主軸三｜進階 CKD 與透析：把 PK、療效、耐受性拆開

### 三個不能互相替代的問題

| 問題 | 現有答案 |
|---|---|
| 腎功能差時是否需要依 eGFR 調整劑量？ | 這是標籤／PK 問題；「不需腎功能劑量調整」本身不含療效或耐受性答案。 |
| eGFR<25 起始是否有 FLOW efficacy evidence？ | 沒有。FLOW 收案下限為 eGFR 25；eGFR<30 subgroup 不能替代 eGFR<25。 |
| 進入維持性透析後起始或持續是否有效、安全？ | 起始療效未知；續用只有高度選定病人的事後描述性資料。 |

若台下問「eGFR 20 能不能用」，不應只回答絕對的「可以」或「不可以」。較好的回答是：**FLOW 沒有 eGFR 20 起始療效證據；實際可否使用應核對當地現行標籤與指引，再依治療目標、GI／容量／營養風險與個別判斷決定。**

### 透析資料要先畫出 selection funnel

來源報告的 pooled denominator 為 34,064 人，其中 307 人於追蹤中開始透析，只有 165 人在透析起始後仍持續原分派治療（semaglutide 71、placebo 94）。這個 34,064 → 307 → 165 漏斗依序條件化於存活、開始透析與繼續治療，無法保留用來回答透析療效的原始隨機比較。

在這 165 名續用者中，嚴重不良事件為 45% 對 57%，永久停藥 8.5% 對 10.6%。可說「未見明顯安全災難、提供有限 continuation-safety 安心」，不可說 semaglutide 比 placebo 安全，也不可外推成維持性透析起始治療的療效。

### 可直接講的 45 秒版本

> 「晚期 CKD 最容易把三件事混在一起：藥物動力學、療效與病人能不能承受。FLOW 的 efficacy boundary 止於入組 eGFR 25；透析後 pooled analysis 又只剩 165 名開始透析後仍持續原分派藥物者。45% 對 57% 的嚴重不良事件可以作描述性 reassurance，不能恢復成透析族群的隨機安全優越性。我的實務重點會是慢滴定、食慾與蛋白熱量攝取、體重與功能、容量狀態，以及利尿劑／SGLT2i／GI loss 疊加造成的腎前性 AKI。」

### 建議新增的演講圖

- **Inside／adjacent／outside FLOW evidence map：** FLOW-like albuminuric T2D CKD／eGFR 低於 25／維持性透析與移植。
- **34,064 → 307 → 165 selection funnel：** 圖下直接寫 `descriptive continuation-safety cohort; not a dialysis efficacy trial`。
- **GI loss → reduced intake／volume depletion → prerenal AKI pathway：** 加上 frailty、sarcopenia 與 diuretic／SGLT2i 的臨床監測點。

**來源定位：** `FLOW-PROTOCOL-2021`，synopsis pp.6–7；`FLOW-SUPPLEMENT-2024`，Eligibility Criteria pp.11–13；`FLOW-DIALYSIS-SAFETY-2026`，structured abstract「Research Design and Methods」「Results」「Conclusions」，[DOI](https://doi.org/10.2337/dc26-0112)／[PubMed](https://pubmed.ncbi.nlm.nih.gov/41893299/)；`FDA-OZEMPIC-USPI-S038-2026`，Renal Impairment §8.6、Clinical Pharmacology，以及 volume-depletion AKI warning。

## 主軸四｜三條腎臟訊號：eGFR slope、UACR、marker concordance

### 數據應如何分層

1. **確認性結果：** total eGFR slope 為 −2.19 對 −3.36 mL/min/1.73m²/year，組間差 +1.16（0.86–1.47）。
2. **時序判讀：** baseline 到 week 12 的絕對 eGFR 變化差 −0.03（−0.56–0.51）；只能說「至 week 12 未見 semaglutide-specific differential dip」，不能排除更早、短暫且已消退的變化。Week 12 至試驗結束的 chronic slope 差 +0.94（0.62–1.26）。
3. **支持性 surrogate：** week 104 UACR ratio-of-ratios 0.68（0.62–0.75），即相對低約 32%；不是 32 percentage-point absolute reduction，也不是已證實中介。
4. **測量敏感度檢查：** creatinine 與 cystatin-C 方向近似一致，降低「只有減重／肌肉量下降改變 creatinine generation」的單一解釋可信度；它不能證明效果獨立於體重、HbA1c、血壓或其他路徑。

### 可直接講的 50 秒版本

> 「我會把 eGFR、UACR 與 marker concordance 畫成三層，不把它們混成一條機轉。總 eGFR slope 差每年 1.16，是確認性次要結果；week 104 的 UACR 相對低約 32%，是支持性 surrogate；creatinine 與 cystatin-C 方向一致，讓純粹 creatinine-generation artifact 比較不可能。但 FLOW 沒有正式完成體重、血糖、血壓與 UACR 的因果中介分解，所以不能說效果已證實獨立於減重，也不能把 UACR 下降直接說成 hard outcome 的原因。」

### 視覺與來源

- 投影：[eGFR 三階段重繪圖](./presentation_zh_tw/public_assets/redrawn/02_flow_egfr_phases_zh_tw@2x.png)。
- 建議 appendix 再畫一個 **marker → surrogate → mediator → clinical outcome** ladder，讓聽眾把 measurement robustness 與 causal mechanism 分開。
- `FLOW-PRIMARY-2024`，Figure 1D、Results pp.114–116、Table 2 p.116、Discussion pp.119–120；`FLOW-SUPPLEMENT-2024`，Figure S2A，supplement pp.19–20。[DOI](https://doi.org/10.1056/NEJMoa2403347)。

## 主軸五｜機轉可以講多深：Outcome 比 receptor map 更可靠

### Cross Sessions 的核心分歧

臨床角色希望用 natriuresis、RAAS、發炎、氧化壓力、代謝與體重路徑，解釋多面向效益；方法學角色要求每一條路徑都標示證據層級，避免把合理機轉寫成已在人類 FLOW 中完成驗證的 causal chain。

### 裁決後的證據階梯

| 層級 | 可說到哪裡 |
|---|---|
| FLOW clinical outcomes／eGFR slope | outcome evidence 最強，可直接作臨床結論。 |
| UACR、代謝與血壓變化 | 支持多路徑作用；尚未證實各自中介多少 outcome effect。 |
| 人體短期生理研究 | 可支持 natriuresis／RAAS 等候選路徑；不能等同長期 CKD outcome mechanism。 |
| 人體腎臟 GLP-1R 定位 | 尚無共識。Pyke 等 validated-antibody 研究在其樣本中定位於 preglomerular artery／arteriole vascular smooth muscle；這是 study-specific finding，不是全領域定論。 |
| 動物、細胞、影像或 surrogate 研究 | 用來建立 plausible pathway 與研究問題，不能升格為 FLOW hard-outcome 的直接原因。 |

SMART、REMODEL 或後續 imaging／omics／surrogate 研究若納入演講，應放在「機轉假說如何變得更可檢驗」，而不是「已證明直接腎臟作用」。尤其不能把人體受體位置簡化成一個已確定的 generic vascular／tubular site；目前最準確的表述仍是 **human renal GLP-1R localization remains unsettled**。

### 可直接講的 40 秒版本

> 「臨床結果比受體地圖更確定。FLOW 告訴我們 outcome 與 eGFR slope 改善；UACR、血壓、血糖與體重提供多路徑線索，但沒有完成因果分解。人體腎臟 GLP-1 receptor 的定位至今沒有共識；Pyke 的 validated-antibody 研究得到 preglomerular vascular smooth-muscle 的結果，只能稱為該研究的發現。因此機轉頁的標題應是『可能如何發生』，不能是『已證實直接作用在哪一段腎元』。」

**來源定位：** `GLP1R-LOCALIZATION-2014`，PubMed abstract／本證據庫摘要層級二手擷取；全文未獨立取得，因此 preglomerular vascular smooth-muscle 僅列為該研究之提示性發現。[DOI](https://doi.org/10.1210/en.2013-1934)／[PubMed](https://pubmed.ncbi.nlm.nih.gov/24467746/)；`GLP1-RENAL-CROSSTALK-2024`，human renal physiology 與 receptor-localization sections（機轉回顧；底層 infusion studies 未於本證據包逐篇重新核實）。[DOI](https://doi.org/10.1152/ajpcell.00476.2023)／[PubMed](https://pubmed.ncbi.nlm.nih.gov/38105752/)。兩者是定位／機轉來源，不是 FLOW outcome evidence。

## 主軸六｜從「哪個藥最好」改成「哪個病人的哪個問題最重要」

### 三個病例比一張固定階梯更能引發討論

| 病例 | 演講決策焦點 | 可說與不可說 |
|---|---|---|
| A：eGFR 42、UACR 800 mg/g、T2D、肥胖，已使用最大可耐受 RASi | 高度 FLOW-like；同時有腎臟、體重、血糖與可能 CV 目標。 | 可引用整體 FLOW 結果；仍須把五項含 CV death 與四項支持性終點拆開。 |
| B：eGFR 35、UACR 150 mg/g、ASCVD，已用 RASi＋SGLT2i | 有 semaglutide 的多面向臨床理由，但增量 hard-kidney effect 未被辨識。 | 不說「SGLT2i 上再降 24% 腎風險」，改說依 ASCVD／肥胖／血糖與殘餘 CKD 風險共同選擇。 |
| C：eGFR 23、衰弱、食慾差、使用 insulin、既有 retinopathy | 位於 FLOW initiation-efficacy 邊界外；營養、低血糖、GI／容量與眼科風險優先。 | 不用單一 eGFR 作絕對禁令；核對標籤／指引與目標，若使用則採更密集的個別監測。 |

### 腎臟科安全性清單

- **容量與 AKI：** 嘔吐、腹瀉、進食下降若疊加利尿劑與 SGLT2i，可能造成 volume depletion／prerenal AKI；滴定期安排 sick-day plan 與腎功能／容量複查。
- **營養與功能：** 不只量體重；記錄食慾、蛋白熱量攝取、肌力／功能與 frailty，尤其晚期 CKD 或透析病人。
- **低血糖：** semaglutide 內在低血糖風險低，但與 insulin／sulfonylurea 併用時須主動調整與監測。
- **胃排空與程序：** 先詢問 symptomatic gastroparesis、持續性 GI 症狀與預定麻醉／內視鏡，依現行在地規範處理。
- **眼部風險：** 對既有 diabetic retinopathy 與快速降糖風險作個別監測。**NAION 在本專案凍結證據庫中是尚未完成 hard sourcing 的開放缺口；不可由 FLOW 的 retinopathy 資料推論 NAION 風險或安全性。**

### 可直接講的 45 秒結尾

> 「我不會用一張固定四支柱階梯結束，而會用 phenotype map。對 FLOW-like 的 albuminuric T2D CKD，semaglutide 已有強的整體 outcome 理由；若已用 SGLT2i、低於 eGFR 25、進入透析，或具有衰弱與營養風險，就把已知與未知一起開給聽眾。真正的精準治療不是替藥物排永遠不變的名次，而是先說明此刻要降低哪一種風險、證據是否直接、病人是否承受得住。」

**主要來源定位：** phenotype 與安全性整合見 `FLOW-PRIMARY-2024` Table 1、Table 3；`FLOW-SUPPLEMENT-2024` Tables S4–S5；`FDA-OZEMPIC-USPI-S038-2026` 的 diabetic retinopathy、hypoglycemia、severe GI、volume-depletion AKI 與 peri-procedural warnings；臨床決策框架另見 [`13_CLINICAL_DECISION_FRAMEWORK.md`](./13_CLINICAL_DECISION_FRAMEWORK.md)。NAION 此處只登錄為來源缺口，不作實證主張。

## 20 分鐘版本：12 張投影片

| Slide | 標題 | 核心任務 |
|---:|---|---|
| 1 | Semaglutide 在 albuminuric T2D CKD：證明了什麼，留下什麼？ | 先交代聽眾與 evidence boundary。 |
| 2 | 病例 A：你會在何時加入 semaglutide？ | 投票，先揭露臨床直覺。 |
| 3 | FLOW 收了誰、沒收誰？ | eGFR／UACR eligibility 與背景 RASi。 |
| 4 | Endpoint anatomy | 五項含 CV death、四項排除 CV death。 |
| 5 | 結果 forest | HR 0.76、0.79 與個別組成。 |
| 6 | NNT 20 不是 dialysis NNT | 防止最常見 headline error。 |
| 7 | eGFR 三段＋UACR | slope、week-12 boundary、surrogate。 |
| 8 | 已用 SGLT2i 還知道多少？ | 550 人／79 事件、CI 與 estimand dependence。 |
| 9 | MRA 不等於 finerenone | baseline finerenone=0；不宣稱加成。 |
| 10 | eGFR<25／透析 | inside–outside map＋34,064→307→165 funnel。 |
| 11 | 三病例 phenotype map | FLOW-like、adjacent、outside。 |
| 12 | 三句帶走 | Outcome 成立；組合與晚期族群未知；安全性由容量與營養落地。 |

## 40 分鐘版本：增加 10 張深挖頁

在上述 12 張之間加入：試驗 854→570→741 時間軸、competing-risk 示意、KRT／eGFR<15 個別組成、MACE／死亡、CKD severity subgroup、creatinine vs cystatin-C、marker／mediator ladder、人體機轉 evidence ladder、GI／volume-depletion／AKI pathway，以及完整 audience Q&A。詳細 25 張既有編排可直接沿用 [`presentation_zh_tw/SLIDE_STORYBOARD_ZH_TW.md`](./presentation_zh_tw/SLIDE_STORYBOARD_ZH_TW.md)與[`逐張講稿`](./presentation_zh_tw/SPEAKER_NOTES_ZH_TW.md)。

## 建議保留的六張 appendix 圖

1. **Endpoint／hierarchy anatomy：** confirmatory、supportive、component 三層。
2. **854 → 570 → 741 stopping timeline：** 解釋提前停止與長期精確度。
3. **Background therapy matrix：** RASi、SGLT2i、steroidal MRA、finerenone。
4. **Combination-evidence matrix：** overall outcome、subgroup consistency、incremental hard-kidney benefit、direct factorial evidence 四欄。
5. **Marker／surrogate／mediator ladder：** creatinine、cystatin C、UACR、eGFR slope、clinical events。
6. **Dialysis selection funnel：** 34,064 → 307 → 165，清楚標示 post-randomization selection。

## 高機率 Q&A：短答版本

**Q1：所以 semaglutide 降低洗腎 24% 嗎？** 不是。24% 對應含 CV death 的五項主要複合；慢性 KRT 單項 HR 0.84（0.63–1.12），未被單獨確認。

**Q2：已用 SGLT2i 的 HR 1.07，是否代表不要合併？** 不是。該層只有 79 個主要事件且 CI 很寬，結果是不確定，不是證明無效或傷害；臨床可因其他已成立目標使用，但不能承諾增量 hard-kidney benefit。

**Q3：P-interaction 不顯著，是否證明兩組效果一樣？** 不是。未偵測到異質性不等於等效，尤其次族群小且檢定力不足。

**Q4：eGFR 20 能否開始？** FLOW 沒有該範圍的 initiation-efficacy evidence。請核對現行標籤與指引，並依適應目標、容量、GI、營養與 frailty 個別判斷；PK 可行性不能補成療效證明。

**Q5：透析後 45% 對 57% 是否代表更安全？** 不能。這是經過三層選擇的 165 名續用者描述性比較，只能提供有限 reassurance。

**Q6：UACR 降 32% 是否解釋全部腎臟效益？** 未知。UACR 是支持性 surrogate，FLOW 沒有完成因果中介分析。

**Q7：creatinine 與 cystatin-C 一致，是否證明與減重無關？** 不能。它減少純 creatinine-generation artifact 的疑慮，但無法區分體重、血糖、血壓、發炎或其他路徑的中介比例。

**Q8：腎臟 GLP-1 receptor 到底在哪裡？** 人體定位沒有共識；最安全的講法是 unresolved，而不是指定單一 nephron／vascular site 已獲證實。

**Q9：有 retinopathy 資料，能否順便回答 NAION？** 不能。兩者不是可互換終點；本凍結證據庫對 NAION 尚缺 hard sourcing。

**Q10：那臨床到底怎麼排序？** 先確立 RASi／SGLT2i 等直接 CKD 基礎證據，再依 albuminuria、HF、ASCVD、肥胖、血糖、血鉀、容量、營養與耐受性選擇額外治療；把每項未知與治療理由一起說明。

## 發布與使用底線

- 本篇只公開對話後的可核查裁決，不公開內部 transcript、session identifier 或傳輸紀錄。
- 本輪 cross-session dialogue 沒有重新取得原始全文；若引用定量結果，仍以既有來源帳本與原始 Table／Figure locator 為準。
- 受限制出版社的 PDF 頁面或截圖不得因本文而公開；投影片優先使用[既有重繪圖與授權素材](./presentation_zh_tw/README.md)。
- 所有 NNT 必須同列 endpoint、是否含 CV death、時間窗與分析層級；所有 subgroup 投影片必須同列 N、可核實之事件數、CI 與 interaction；若來源未報或本公開證據包尚未核實事件數，須明示「未報／未核實」。
- 本文是學術研究與演講準備材料，不構成個人化醫療建議。
