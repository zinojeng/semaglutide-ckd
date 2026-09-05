# 03｜FLOW 之外：SELECT、SOUL、類別效應與腎臟機轉

> 範圍：依 SHA-256 `75368cba…98cd56` 的凍結總論精煉；證據截止 2026-09-05。本文是臨床學術整理，不是個人化醫療建議。

## 一句話先說結論

SELECT、SOUL 與彙總分析讓 semaglutide 的腎臟訊號跨出 FLOW 單一情境，但三個試驗的族群、劑量、途徑與終點不同。它們支持「整體證據方向一致」，不能證明 1.0 mg 皮下注射、2.4 mg 皮下注射與 14 mg 口服具有相同腎臟療效，也不能證明效果與血糖或體重完全無關。

## 三個試驗，其實在問三個不同問題

| 試驗 | 主要族群 | 劑量／途徑 | 腎臟結果在試驗中的位置 | 核心腎臟估計 |
|---|---|---|---|---:|
| FLOW | T2D＋白蛋白尿性 CKD | 1.0 mg SC／週 | 主要五項複合終點，含 CV death | HR 0.76（0.66–0.88） |
| SELECT | 過重／肥胖＋ASCVD，無糖尿病診斷 | 2.4 mg SC／週 | 預先設定次要複合終點，含新發巨量白蛋白尿 | HR 0.78（0.63–0.96） |
| SOUL | T2D＋ASCVD 及／或 CKD | 14 mg oral／日 | MACE 後的五項 kidney/CV-death composite（含 CV death） | HR 0.91（0.80–1.05），P=0.19 |

FLOW 的精確定位見 `FLOW-PRIMARY-2024` Table 2／Discussion，journal pp.116、119–120。SELECT 見 `SELECT-KIDNEY-2024` Table 1、Figures 1–5、Methods／Results。SOUL 見 `SOUL-PRIMARY-2025` 與 `SOUL-KIDNEY-2026` PubMed structured abstracts／Results。

## SELECT：沒有糖尿病，不等於沒有代謝路徑

SELECT 共 17,604 人，入組時 HbA1c<6.5%，使用 2.4 mg SC semaglutide。預先設定次要腎臟複合終點 HR 0.78（0.63–0.96，P=0.02）。第 104 週 eGFR 組間差為 +0.75（0.43–1.06）mL/min/1.73m²；總斜率差 +0.39（0.30–0.48）mL/min/1.73m²/年；第 104 週 UACR 相對差 −10.7%（−13.2% 至 −8.2%）。

這些數字不能直接變成「非糖尿病 CKD 硬終點療效」，理由有五個：

1. 66.4% 參與者為糖尿病前期，只有 33.5% 為正常血糖；沒有糖尿病診斷不等於排除所有葡萄糖相關機轉。
2. 腎臟複合終點主要由新發巨量白蛋白尿與持續性 eGFR 下降 ≥50% 帶動；排除巨量白蛋白尿後未達顯著。
3. SELECT 不是專屬 CKD 試驗，只有約五分之一世代具 eGFR<60 或 UACR≥30 的合併條件。
4. eGFR<60 次族群兩組 eGFR 都數值上改善，作者提出均值迴歸的可能，不能稱為腎功能「恢復」。
5. 所謂體重中介 81%（95% CI 41–120%），只針對**第 104 週 eGFR 變化**，不是 eGFR 斜率或硬腎臟複合終點；模型只使用基線與第 104 週兩個時間點。

定位：`SELECT-KIDNEY-2024` Table 1、Figures 1–5、Methods「Correlation and mediation analysis」及相應 Results，PMCID PMC11271413；糖尿病前期比例見 `SELECT-GLYCEMIA-2024` PubMed structured abstract／Results，PMID 38907683。

校準解讀：SELECT 使「腎臟訊號可能不完全依賴 T2D 診斷」更有可信度，但仍只屬提示性至假說生成；它沒有取代一項專為非糖尿病 CKD 設計的硬終點試驗。

## SOUL：腎臟複合未顯著，不等於口服型無效

SOUL 共 9,650 名 T2D 合併 ASCVD 及／或 CKD 參與者，使用口服 semaglutide 14 mg／日。主要 MACE 結果 HR 0.86（0.77–0.96，P=0.006）。五項 kidney/CV-death composite（含 CV death）為 403/4,825 對 435/4,825，HR 0.91（0.80–1.05，P=0.19）；排除 CV death 的四項腎臟專屬終點 HR 0.86（0.66–1.10，P=0.22）。

總 eGFR 斜率差為 +0.40（0.27–0.53）mL/min/1.73m²/年，名義 P<0.0001；但因階層中第一項腎臟複合終點未達顯著，斜率必須標為形式上探索性。

SOUL 平均基線 eGFR 73.8，沒有收集 UACR；其安慰劑組腎臟複合事件率約 2.3／100 病人年，約為 FLOW 的三分之一。這種風險與事件密度差異，是合理但非因果分解的解釋。不能把兩試驗的差異簡化為「注射有效、口服無效」，因為劑量、途徑、族群風險與事件組成同時改變。

定位：`SOUL-PRIMARY-2025` PubMed structured abstract Methods／Results，PMID 40162642；`SOUL-KIDNEY-2026` PubMed structured abstract Research Design and Methods／Results 及 Discussion 的 FLOW–SOUL 比較段落，PMID 41380027。

## 彙總分析：可增加精確度，不能消除異質性

預先設定的 SELECT＋FLOW＋SOUL 參與者層級彙總共 30,787 人。結構化摘要將兩個 aggregate outcome 標示為含 CV death 的主要彙總複合終點（973 對 1,134 例，HR 0.84〔0.77–0.91〕），以及排除 CV death 的腎臟專屬複合終點（347 對 416 例，HR 0.80〔0.69–0.92〕）。

本專案取得的摘要未列舉 pooled composite 的完整組成，全文、表格與附錄也未取得，因此 component-by-component matching 尚未核實。兩個 pooled HR 可各自報告，但不可把 pooled 0.84／FLOW 0.76／SOUL 0.91 或 pooled 0.80／FLOW 0.79／SOUL 0.86 排成看似 like-for-like 的三數。各試驗估計應分開呈現並附自己的已核實定義。彙總結果提高整體估計精確度，卻沒有把三個不同族群、劑量與途徑變成同一個介入，也不是血糖／體重中介分析。

定位：`SELECT-FLOW-SOUL-POOLED-2026` PubMed structured abstract／Findings，PMID 42567173；全文未取得，因此不推論摘要未報告的試驗間異質性，也不假定完整 endpoint matching 已完成。

## 是 semaglutide 效應，還是 GLP-1RA 類別效應

10 項 T2D RCT 的統合分析共 67,769 人；事後加入 SELECT 後為 11 項、85,373 人。排除 CV death 的腎臟複合終點 HR 0.82（0.73–0.93），腎衰竭 HR 0.84（0.72–0.99），MACE HR 0.87（0.81–0.93），全因死亡 HR 0.88（0.83–0.93）。

這支持類別層級的整體訊號，卻不代表每一分子具有相同效果：

- semaglutide 有專屬硬腎臟結果 RCT（FLOW）；
- liraglutide 與 dulaglutide 的腎臟複合效益主要來自 CVOT 次要／探索性結果，且白蛋白尿成分較突出；
- exenatide、lixisenatide 的資料更偏向事後或白蛋白尿訊號；
- tirzepatide 是 GIP／GLP-1 雙重促效劑，不能直接當成傳統單一 GLP-1RA 證據。

因此最精確的說法是：類別效應受到支持，但分子間的證據厚度不均；FLOW 的結果首先是 semaglutide 專屬證據，不自動授權整類藥物共享同一效果。

定位：`GLP1-CLASSMETA-BADVE-2025` PubMed structured abstract Methods／Findings，PMID 39608381；分子來源見 `LEADER-RENAL-2017`、`REWIND-RENAL-2019`、`AMPLITUDEO-SGLT2-2022`、`EXSCEL-EGFR-2020`、`ELIXA-RENAL-2018`、`SURPASS4-KIDNEY-2022` 各自 Results。

## 腎臟保護可能怎麼發生

### 代謝與全身路徑：很可能有貢獻，但比例未在 FLOW 確立

FLOW 的組間差異包括 HbA1c −0.81 個百分點、體重 −4.10 kg、收縮壓 −2.23 mmHg。非 FLOW 的中介分析估計 HbA1c 中介約 25–26%、收縮壓約 9–22%，但信賴區間寬或無法計算，且使用不同族群與複合終點。

SUSTAIN-6 的 semaglutide 體重中介點估計為 0%，但 CI 無法計算，因此不具資訊量；SELECT 的 81%（41–120%）針對不同替代結果。兩者方法、族群與結果不同，不能平均，也不能用其中任一數字宣告「完全與體重無關」或「幾乎全由體重造成」。FLOW 中 creatinine 與 cystatin-C 結果相近，只降低純體重／肌肉量改變造成肌酸酐生成假象的疑慮；未報兩估計差值 CI，且不能證明體重獨立或一般測量誤差已排除。

定位：`FLOW-PRIMARY-2024` Table 2／Results「Other Outcomes」，journal p.116；`SUSTAIN6-MEDIATION-2021` Methods／Figure 1A–F；`SELECT-KIDNEY-2024` Methods／Results「Correlation and mediation analysis」。

### 腎臟血流動力學與鈉處理：具合理性，尚不能指定主路徑

人體急性輸注生理研究顯示，GLP-1 相關鈉排泄增加可被受體拮抗劑阻斷，但沒有同時量到腎血漿流量或 GFR 改變；這較支持腎小管鈉處理，而不是已證明的主要腎絲球血流動力學效應。FLOW **至第 12 週**未見 semaglutide 特異的額外 acute dip，慢性斜率才逐步分離；沒有更早時點，故不排除先前已消退的短暫變化，也不能據此指定唯一機轉。

動物與細胞研究支持抗發炎、抗氧化、抗纖維化與腎絲球回饋假說；FLOW 本身沒有腎切片、腎血流鉗夾或完整纖維化標記研究，這些機轉仍屬假說生成。

### 「直接作用在腎元 GLP-1 receptor」仍未確立

嚴謹的人體組織定位把可驗證的 GLP-1 receptor 訊號置於腎絲球前小動脈血管平滑肌，而非腎絲球、腎小管或靜脈；其他報告不一致，可能涉及抗體特異性。現階段不能無保留地寫成「semaglutide 直接刺激腎小管／腎絲球細胞上的受體而保護腎元」。

定位：`GLP1R-LOCALIZATION-2014` Methods／Results，PMID 24467746；`GLP1-RENAL-CROSSTALK-2024` human renal physiology／receptor-localization sections，PMID 38105752。

## 臨床帶走三件事

1. FLOW 是最直接的白蛋白尿性糖尿病 CKD 結果證據；SELECT 與 SOUL 主要提供外延與一致性，不取代 FLOW 的族群邊界。
2. 劑量、途徑與族群不能合併成等效主張；SOUL 未顯著也不能單獨歸因於口服途徑。
3. 最合理的機轉結論是「多因子」；血糖、體重、血壓、鈉處理、血管與發炎路徑可能共同參與，但直接腎元 GLP-1 receptor 路徑未確立。

## 投影片用 reference 快速索引

| 文章主題 | 原始來源定位 | 投影片使用方式 | 一句講者提醒 |
|---|---|---|---|
| FLOW／SELECT／SOUL | `FLOW-PRIMARY-2024` Table 2，p.116；`SELECT-KIDNEY-2024` Table 1/Figs.1–5；SOUL PubMed Results | 自製三欄 population／dose／endpoint matrix | 三個 HR 不能按大小排序，也不能推成 route 勝負。 |
| SELECT continuous outcomes | `SELECT-KIDNEY-2024` Table 1；Figs.4–5；PMCID PMC11271413 | 重繪 week-104 eGFR、total/chronic slope、UACR | SELECT 不是專屬非糖尿病 CKD hard-outcome trial。 |
| SELECT weight mediation | `SELECT-KIDNEY-2024` Methods「Correlation and mediation analysis」／Results | 畫估計對象框：week-104 eGFR change | 81%（41–120%）不適用於 slope 或 hard composite。 |
| SOUL hierarchy | `SOUL-KIDNEY-2026` PubMed Methods／Results；`SOUL-PROTOCOL-2021` §10.3.2.1 p.50 | 自製 gate 圖，不使用受限原圖 | 五項複合未顯著後，斜率僅名目顯著、形式上探索性。 |
| 三試驗 pooled | `SELECT-FLOW-SOUL-POOLED-2026` PubMed Findings，PMID 42567173 | 只重繪兩個 pooled aggregate；不與 FLOW／SOUL 排成 matched triplet | 完整 component definitions 未由摘要核實；提高精確度不代表 endpoint、族群、劑量或途徑等效。 |
| 類別與機轉 | `GLP1-CLASSMETA-BADVE-2025` PubMed Findings；`GLP1R-LOCALIZATION-2014` Methods／Results | 自製 evidence ladder | 類別訊號受支持；直接腎元 GLP-1R 路徑未確立。 |

完整圖說、30 秒口述與授權模板見 [`../presentation_zh_tw/ARTICLE_REFERENCE_GUIDE.md`](../presentation_zh_tw/ARTICLE_REFERENCE_GUIDE.md)。

## 權利與再利用界線

本文只重組凍結總論中已核實的數字、短篇幅轉述與來源定位，不散布全文或 PDF。SOUL kidney 的數字依 PubMed 結構化摘要與凍結總論已核實內容呈現；受限快取解析不作唯一來源，也不在本 repo 再利用。
