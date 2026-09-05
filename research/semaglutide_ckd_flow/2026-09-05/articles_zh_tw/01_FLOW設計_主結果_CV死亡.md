# 01｜FLOW 到底證明了什麼？從試驗設計、主要結果到 CV death

> 範圍：依 SHA-256 `75368cba…98cd56` 的凍結總論精煉；證據截止 2026-09-05。本文是臨床學術整理，不是個人化醫療建議。

## 一句話先說結論

FLOW 把 semaglutide 從「已有腎臟訊號的降血糖／體重／心血管藥物」，推進為在 **T2D 合併白蛋白尿性 CKD** 中具有隨機結果證據的治療；但它證明的是「重大腎臟事件與心血管死亡」複合終點下降，不能縮寫成「腎衰竭下降 24%」。

## 為什麼 FLOW 必須做

FLOW 之前，SUSTAIN-6 的腎病複合終點 HR 0.64（0.46–0.88），主要由新發持續性巨量白蛋白尿帶動；PIONEER-6 則沒有專屬腎病複合終點。這些結果足以建立假說，卻不足以回答 semaglutide 是否能在高腎臟風險族群中減緩 eGFR 流失或降低重大腎臟事件。

定位：`SUSTAIN6-2016` PubMed structured abstract／Results；`PIONEER6-2019` PubMed structured abstract／Results；`SUSTAIN6-PIONEER6-EGFR-NDT-2025` Results／Figures 1–3。

## FLOW 收了哪些病人

FLOW 是國際、雙盲、隨機、安慰劑對照、事件驅動試驗，共隨機分派 3,533 人（semaglutide 1,767；安慰劑 1,766）。受試者須有 T2D，並循兩條腎功能／白蛋白尿路徑收案：

1. eGFR ≥50–≤75 mL/min/1.73m²，UACR >300 且 <5,000 mg/g；或
2. eGFR ≥25–<50，UACR >100 且 <5,000 mg/g。

HbA1c 上限為 10%，並原則上使用最大可耐受或標籤劑量 ACEi／ARB。平均 eGFR 47.0，UACR 中位數 567.6 mg/g；68.3% 為 KDIGO 極高風險。基線 SGLT2i 使用率只有 15.6%，MRA 7.3%，且沒有 finerenone 使用者。介入為皮下注射 semaglutide，每週 1.0 mg。

定位：`FLOW-PRIMARY-2024` Table 1、Methods，journal pp.110–113；`FLOW-SUPPLEMENT-2024` Eligibility Criteria pp.11–13；`FLOW-PROTOCOL-2021` synopsis pp.6–7；MRA 組成見 `FLOW-MRA-2025` Figure 1／Supplementary Tables 1–2。

這個族群邊界很重要：FLOW 不是「所有 CKD」試驗，也不是透析、腎移植、第一型糖尿病、非糖尿病 CKD 或低／無白蛋白尿 CKD 的直接療效試驗。

## 主要終點不是純腎臟終點

主要終點採首次事件時間分析，由五項組成：

1. 持續性（≥28 天）eGFR 自基線下降 ≥50%；
2. 持續性（≥28 天）eGFR <15 mL/min/1.73m²；
3. 開始慢性腎替代治療；
4. 腎因性死亡；
5. **心血管死亡。**

因此最精確的名稱是「重大腎臟事件與心血管死亡五項複合終點」。排除心血管死亡後，才是支持性的四項腎臟專屬複合終點。

定位：`FLOW-PRIMARY-2024` Methods／Table 2，journal pp.110–116；`FLOW-SUPPLEMENT-2024` Table S2。

## 核心結果：應該成對報告

| 結果 | Semaglutide | 安慰劑 | 效果估計 | 推論地位 |
|---|---:|---:|---:|---|
| 五項主要複合終點（含 CV death） | 331/1,767（18.7%） | 410/1,766（23.2%） | HR 0.76（0.66–0.88） | 確認性主要結果 |
| 四項腎臟專屬複合終點 | 218（12.3%） | 260（14.7%） | HR 0.79（0.66–0.94） | 支持性；階層之外、未校正多重比較 |
| 總 eGFR 斜率 | −2.19／年 | −3.36／年 | 差異 +1.16（0.86–1.47） | 通過確認性階層 |
| MACE | 212（12.0%） | 254（14.4%） | HR 0.82（0.68–0.98） | 通過確認性階層 |
| 全因死亡 | 227（12.8%） | 279（15.8%） | HR 0.80（0.67–0.95） | 通過確認性階層 |

主要複合終點三年 NNT 為 20（95% CI 14–40）。這是主要論文直接報告、**含心血管死亡的主要複合終點 NNT**，不是「預防一例透析」的 NNT。本專案取得的來源沒有明示其計算方法，也沒有另報可核對的精確三年 RD；因此不能用 18.7% 對 23.2% 這組未定時點、未處理截尾的粗比例自行重算 ARR／NNT。

定位：`FLOW-PRIMARY-2024` Results「Primary Outcomes」journal p.115、Table 2 p.116、Discussion pp.119–120；`FLOW-SUPPLEMENT-2024` Tables S2–S3。MACE／全因死亡的第 156 週 RD 與 NNT 另見 `FLOW-CKDSEVERITY-2025` Methods／Statistical Analysis 與 Table 2 後 Results，journal pp.1103–1106；其方法不能回填為主要終點三年 NNT 的未明示方法。

## 個別腎衰竭事件沒有被單獨證明

慢性腎替代治療 HR 0.84（0.63–1.12），持續性 eGFR<15 HR 0.80（0.61–1.06），腎因性死亡 HR 0.97（0.27–3.49；5 對 5 例）。前兩者點估計方向有利，腎因性死亡近中性；三者均未個別顯著，也不在確認性檢定階層內。原始論文同樣指出，試驗沒有足夠檢定力分別偵測腎衰竭組成。持續性 eGFR 下降 ≥50% 的 HR 0.73（0.59–0.89）雖排除 1，也在階層之外；它是 nominal／支持性組成，不得另下「降低 27%」標題，更不是腎衰竭本身。各組成事件會重疊，不能據此判定哪一項驅動複合結果。

所以可說：「FLOW 降低包含腎衰竭在內的複合終點。」不可說：「FLOW 已單獨證明透析、eGFR<15 或腎因性死亡下降。」

定位：`FLOW-PRIMARY-2024` Table 2／Discussion，journal pp.116、119–120。

## CV death 到底貢獻多少

心血管死亡為 123 對 169 例，HR 0.71（0.56–0.89），但這個個別組成也位於確認性階層之外。補充資料的原句概念是：心血管死亡約占主要終點「各組成事件」的 35%。它不是精確的首次事件占比，更不是「24% 治療效果中有 35% 來自 CV death」。

原因在於各組成事件會重疊：同一人可以先後符合 eGFR<15、KRT 與死亡，但主要複合終點只計第一次事件。把 Table 2 的組成數相加，再除以 331 或 410，會製造不存在的「效果分解」。正確做法只有一個：**並列 HR 0.76 的五項主要終點與 HR 0.79 的四項腎臟專屬終點，並標明後者的支持性地位。**

定位：`FLOW-SUPPLEMENT-2024` Table S2 註記，supplement p.24；`FLOW-PRIMARY-2024` Table 2，journal p.116。

## eGFR 斜率提供另一條腎臟證據線

總斜率差異為 +1.16 mL/min/1.73m²/年。兩組從基線至第 12 週都下降約 1.06，組間差僅 −0.03（−0.56 至 0.51），也就是**至第 12 週**沒有 semaglutide 特異的額外 acute dip；本證據庫沒有更早 FLOW 時點，不能排除此前已消退的短暫變化。第 12 週至試驗結束的慢性斜率差為 +0.94（0.62–1.26）。第 104 週以 creatinine 與 cystatin-C 估算的差異相近，降低「只是體重／肌肉量改變造成肌酸酐生成假象」的疑慮；但兩估計差值的 CI 未報告，不能量化一致性強度，也不是生物學中介或體重獨立性證明。斜率是速率，不能換算成「延後洗腎幾年」。

定位：`FLOW-PRIMARY-2024` Table 2、Results／Discussion，journal pp.116、119–120。

## 提前終止如何影響信心

FLOW 原計畫至少累積 854 例主要事件；在約 570 例事件的預先設定期中分析越過療效邊界後，DMC 建議提前終止，至最終資料庫鎖定時共累積 741／854 例事件。主要終點使用群組序貫方法調整，最終雙側名義顯著水準為 0.0322；三項確認性次要終點依階層通過，但未各自重新做群組序貫調整。臨床解讀仍須保留「提前終止可能高估長期效應量」的一般性警語。

定位：`FLOW-SAP-2023` §2.1 pp.6–7、§2.3.1 p.12、§2.4.1 pp.17–18；`FLOW-SUPPLEMENT-2024` PDF pp.16–17。

## 臨床帶走三件事

1. 對符合 FLOW 表現型的 T2D＋白蛋白尿性 CKD，semaglutide 已不只是改善血糖、體重與 CV 風險的藥物。
2. 「24%」必須永遠和「主要終點含 CV death」一起出現；腎臟專屬 HR 0.79 應並列，但不能升格為確認性結果。
3. SGLT2i 仍有更廣泛的專屬 CKD／HF 證據範圍；FLOW 支持的是互補定位，不是替代關係。

## 投影片用 reference 快速索引

| 文章主題 | 原始來源定位 | 投影片使用方式 | 一句講者提醒 |
|---|---|---|---|
| 收案與背景治療 | `FLOW-PRIMARY-2024` Table 1，journal pp.112–113；`FLOW-PROTOCOL-2021` synopsis pp.6–7 | 重繪兩條 eGFR／UACR 收案路徑；Table 1 原頁只作本機核對 | FLOW 是 T2D＋白蛋白尿性 CKD 富集族群，不是所有 CKD。 |
| 五項 endpoint anatomy | `FLOW-PRIMARY-2024` Methods，journal p.111；Table 2，journal p.116；`FLOW-SUPPLEMENT-2024` Table S2，PDF p.24 | 重繪五項環形圖，CV death 用不同色 | HR 0.76 的確認性主要終點包含 CV death。 |
| 主要與腎臟專屬結果 | `FLOW-PRIMARY-2024` Figure 1，pp.114–115；Table 2，p.116 | 重繪兩列 forest：0.76 與 0.79 | HR 0.79 是支持性、階層外，不可升格。 |
| 個別 kidney-failure components | `FLOW-PRIMARY-2024` Table 2，p.116；Discussion pp.119–120 | 重繪 KRT、eGFR<15、腎因性死亡三列 | 三者未被單獨確認，不能說已證明預防透析。 |
| eGFR 三段軌跡 | `FLOW-PRIMARY-2024` Table 2／Discussion，pp.116、119–120 | 三欄呈現 0–12 週、慢性、總斜率 | 只可說至第 12 週沒有 semaglutide 特異性 differential dip；不是完全沒有下降，也不能排除更早且已消退的 transient dip。 |
| 提前停止 | `FLOW-SAP-2023` §§2.1/2.3.1/2.4.1；`FLOW-SUPPLEMENT-2024` PDF pp.16–17 | 重繪 854→約570→741 的時間線 | 約 570 事件跨界；741 是停試建議後最終鎖庫累積數。 |

完整圖說、30 秒口述與授權模板見 [`../presentation_zh_tw/ARTICLE_REFERENCE_GUIDE.md`](../presentation_zh_tw/ARTICLE_REFERENCE_GUIDE.md)。

## 權利與再利用界線

本文為依凍結總論撰寫的原創精煉綜整，只提供必要數字、短篇幅轉述與來源定位，不重製任何論文、補充資料、PDF、全文解析或 protocol／SAP 原檔。正式登錄取得的 FLOW protocol／SAP 帶有贊助者專有／保密文字，只用於核實設計與統計架構。
