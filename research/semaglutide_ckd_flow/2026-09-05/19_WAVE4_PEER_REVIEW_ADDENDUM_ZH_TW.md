# 19｜Wave 4 多角色跨會話同儕校讀增補

> 證據截點：2026-09-05。本文記錄的是三個不同專業角色之 Claude Code 會話所做的證據校讀，不是人類腎臟科、內分泌科或統計方法學專家的正式同儕審查，也不取代個別病人的臨床判斷。

## 為何需要這份增補

第一輪 Wave 4 曾嘗試讓腎臟科、內分泌科與方法學角色進行跨會話討論，但訊息未真正送達或未獲核准，因此沒有形成可採用的真實對話；第一輪也沒有提供任何被本文採納的同儕意見。

第二輪改以全新、可接受跨會話訊息的角色會話重做。腎臟科、內分泌科與方法學三個角色，針對五個預先指定的爭點，完成五條「提問 → 挑戰 → 回應 → 方法檢查／反方意見 → 再回應 → 主編裁決」的完整鏈。所有影響裁決的實質訊息最終均已送達、被回應並納入結論；早期遺漏的轉送亦在封案前補正。五個爭點皆完成明確裁決，沒有留下未處理的專業異議。

本輪的功能是檢查「現有整理是否說得比證據更堅定」，不是重新做一次原始資料擷取。三個角色在本輪無法直接開啟私有原文資料夾，也沒有重新讀取受限制的全文或附件；所有討論均以本專案已完成來源核對與調和的證據表、來源帳本及 01–15 號文件為基礎。因此，下列結論屬於對**已調和證據的獨立角色交叉詰問**，不能宣稱為三次獨立的原始論文全文重現。

## 分級用語

| 分級 | 本增補中的意義 |
|---|---|
| **已確立（established）** | 有直接且與問題相符的隨機證據，並符合該分析原先設定的推論層級。 |
| **支持性／高度支持（supportive / strongly supported）** | 訊號可信，但未受確認性階層或多重比較保護，或只能回答較窄的問題。 |
| **提示性／描述性（suggestive / descriptive）** | 可協助形成假說或床邊監測策略，不能作因果療效結論。 |
| **未確立（not established）** | 現有資料不足以支持該肯定句。 |
| **未知（unknown）** | 對應族群、終點或因果問題沒有可用的直接證據。 |

## 爭點一｜FLOW 到底證明了腎臟什麼結果？

### 問題與不同觀點

- **腎臟科角色**要求將含心血管死亡的主要複合終點、排除心血管死亡的腎臟專屬複合終點、eGFR 斜率與個別腎衰竭組成拆開，尤其不能把「複合終點下降」改寫成「已證實降低腎衰竭」。
- **內分泌科角色**重視 FLOW 同時帶來腎臟、心血管與存活結果，但接受每一個臨床敘述都必須交代終點是否含心血管死亡。
- **方法學角色**指出四項腎臟專屬複合終點位於確認性檢定階層之外；其 95% CI 雖未跨 1，仍是未經多重比較保護的 nominal 結果，不能只寫成「達統計顯著」。個別組成也不能承接整體複合終點的確認性地位。

### 最終裁決與證據分級

| 可說的主張 | 裁決 |
|---|---|
| 五項主要複合終點（包含心血管死亡）下降 24%，HR 0.76（0.66–0.88） | **已確立**；FLOW 的預設主要結果。 |
| 總 eGFR 斜率差 +1.16 mL/min/1.73m²/年 | **已確立**；確認性次要結果，表示平均下降速率減緩。 |
| 四項腎臟專屬複合終點（排除心血管死亡）HR 0.79（0.66–0.94） | **支持性**；nominal 95% CI 未跨 1，但位於階層外、沒有多重比較保護，且來源未公布對應 P 值；不屬確認性結果。 |
| semaglutide 已單獨證實降低腎衰竭 | **未確立**；KRT、持續 eGFR<15 與腎因死亡各組成都未被個別確認，試驗也未為腎衰竭單項充分設計檢定力。 |
| 持續 ≥50% eGFR 下降 HR 0.73（0.59–0.89）可單獨寫成確認性的百分比降低 | **不成立**；它是複合終點中的個別組成且位於確認性階層外，只能以有標記的支持性組成結果呈現。 |
| 心血管死亡占治療效果的固定比例 | **不可推導**；來源所述約 35% 是「終點各組成事件」的近似描述，不是首發事件占比，也不是治療效果占比。 |
| 三年 NNT 20 是腎臟專屬 NNT | **不成立**；NNT 20 對應含心血管死亡的五項主要複合終點，本證據庫沒有 FLOW 腎臟專屬四項複合終點的可用 ARR／NNT。 |

### 建議採用的繁中表述

> 在 FLOW 試驗中，semaglutide 使「主要腎臟事件合併心血管死亡」的預設五項主要複合終點風險降低 24%（HR 0.76，95% CI 0.66–0.88），並以確認性分析顯示總 eGFR 下降速率減緩。排除心血管死亡的四項腎臟專屬複合終點 HR 為 0.79（0.66–0.94），但這是檢定階層外、未經多重比較保護的支持性分析，其 95% CI 為 nominal，不宜逕稱為確認性統計顯著。正確結論是「降低了包含腎衰竭在內的複合終點，並減緩 eGFR 下降速率」，而不是「已證實降低腎衰竭」或把斜率換算成延後洗腎若干年。

### 穩定來源與精確定位

- `FLOW-PRIMARY-2024`：Table 2，journal p.116（主要五項與支持性四項複合終點、個別組成、總／慢性 eGFR 斜率）；Results「Primary Outcomes」，journal p.115（事件率與三年主要複合終點 NNT）；Methods「Statistical Analysis」，journal p.111（檢定策略）；Discussion，journal pp.119–120（未為腎衰竭單項提供充分檢定力）。[DOI 10.1056/NEJMoa2403347](https://doi.org/10.1056/NEJMoa2403347)；[PubMed 38785209](https://pubmed.ncbi.nlm.nih.gov/38785209/)。
- `FLOW-SUPPLEMENT-2024`：Statistical Methods Relating to the Interim Analysis and Hierarchical Testing，supplement p.16；Table S2 note，supplement p.24（「approximately 35% of the components」的來源語境）；Tables S2–S3，supplement pp.24–27。

### 受影響的文章與投影片

- 文章 01：「主要終點不是純腎臟終點」、「核心結果：應該成對報告」、「個別腎衰竭事件沒有被單獨證明」、「CV death 到底貢獻多少」、「eGFR 斜率提供另一條腎臟證據線」。
- 投影片 5–9、11、25：五項組成、成對報告、個別腎衰竭、CV death、eGFR 斜率、MACE／死亡與最終證據分層。

## 爭點二｜已用 SGLT2i、MRA 或 finerenone 時，能否宣稱加成與固定排序？

### 問題與不同觀點

- **內分泌科角色**重視病人仍有肥胖、血糖與心血管殘餘風險時，不應因缺乏理想的組合試驗而忽略 semaglutide 的多面向適應性；臨床可依表現型逐步疊加治療。
- **腎臟科角色**要求把「整體 FLOW 有效」與「在已使用腎臟基礎治療者仍有增量硬腎臟療效」分開；尤其 FLOW 的 MRA 次族群沒有任何 finerenone 使用者。
- **方法學角色**強調 FLOW 不是藥物疊加的因子設計。基線用藥不是隨機分派，SGLT2i 次族群事件少、信賴區間寬；不同腎功能估算標記得到不同點估計，也不能挑選、平均或拼成「真實效果範圍」。

### 最終裁決與證據分級

| 可說的主張 | 裁決 |
|---|---|
| 已用 SGLT2i 者的增量硬腎臟療效 | **未知／未被辨識**。基線 SGLT2i 使用者 550 人，只有 79 個主要事件；creatinine-based 五項與四項複合終點 HR 分別為 1.07（0.69–1.67）及 1.18（0.71–1.98），資料同時容許獲益、無效或傷害，應稱「檢定力不足」，不是「中性」。 |
| post hoc cystatin-C 五項修正版終點 HR 0.74（0.47–1.16）可推翻前述結果 | **不成立**。它反映估算標記與終點定義依賴性，不能被挑作唯一估計，也不能和 1.07 平均。 |
| SGLT2i 次族群的持續 ≥50% eGFR 下降交互作用 P=.023 可作獨立效益或傷害標題 | **不成立**。這是未經多重比較校正的個別組成訊號，不能證明真正效果修飾，也不能承接整體試驗的確認性結論。 |
| semaglutide＋finerenone 已證實有加成硬腎臟效益 | **未確立**。FLOW 基線 finerenone 使用者為 0；steroidal MRA 次族群不能替代 finerenone 組合試驗。 |
| RASi、SGLT2i、finerenone、semaglutide 有隨機試驗證實的固定先後順序或等值「四支柱」 | **未確立**。可做表現型導向的臨床排序，但不能包裝成已證實的加成性或固定階序。 |

### 建議採用的繁中表述

> FLOW 已證實 semaglutide 對整體收案族群的效果，但對基線已使用 SGLT2i 的小型次族群，現有資料不足以確認額外的硬腎臟效益；creatinine-based 與 post hoc cystatin-C 分析的差異提示標記／終點定義依賴性，而不是提供一個可任選的「正確」效果值。FLOW 沒有 finerenone 使用者，因此 semaglutide＋finerenone 的硬終點加成性仍未確立。臨床可依白蛋白尿、心衰竭、ASCVD、肥胖、血糖、血鉀、容量與耐受性分層加藥，但不應宣稱已有隨機試驗證實的固定四藥順序。

這個不確定性也不能反向改寫成「已使用 SGLT2i 的病人不需要 semaglutide」；是否使用仍應依已成立的血糖、體重與心血管適應性及個別病人風險決定，但不得把整體試驗的 MACE／死亡結果冒充成該 550 人次族群的增量估計。

### 穩定來源與精確定位

- `FLOW-SGLT2-2024`：Figures 1–2、Table 1、Extended Data Figures 4–7 及 Results（基線 SGLT2i 次族群人數、79 個主要事件、creatinine-與 cystatin-C-based 結果、交互作用檢定及治療中 SGLT2i 使用）。[DOI 10.1038/s41591-024-03133-0](https://doi.org/10.1038/s41591-024-03133-0)；[PubMed 38914124](https://pubmed.ncbi.nlm.nih.gov/38914124/)。
- `FLOW-MRA-2025`：Figures 1–2、Supplementary Tables 1–2 及 Results（MRA 使用者 257 人、spironolactone／eplerenone／esaxerenone 組成、finerenone 0 人、次族群 HR 與交互作用）。[DOI 10.2337/dc25-0472](https://doi.org/10.2337/dc25-0472)；[PubMed 40730031](https://pubmed.ncbi.nlm.nih.gov/40730031/)。

### 受影響的文章與投影片

- 文章 02：「已使用 SGLT2i：最容易被過度解讀的 550 人」、「Cystatin-C 分析補的是測量疑慮，不是加成性證明」、「MRA 次族群不是 finerenone 次族群」、「合併治療的實際決策方式」。
- 文章 05：「表現型導向的分層演算法」，尤其「依殘餘風險分流，不硬排成第 3、4 名次」與「需要多藥時，把未知一起開出去」。
- 投影片 12、14、15、23、24：次族群規則、SGLT2i、MRA／finerenone、共同分層與病例決策。

## 爭點三｜eGFR<25、維持性透析與透析後持續用藥，可以說到哪裡？

### 問題與不同觀點

- **內分泌科角色**指出「無須依腎功能調整劑量」對晚期 CKD 的處方實務有價值，也關心病人進入透析後是否能繼續原治療。
- **腎臟科角色**要求把藥物動力學可行性、耐受性與臨床療效拆成三個問題，並優先處理胃腸道攝取、容量、衰弱、肌少症與營養儲備。
- **方法學角色**指出透析後分析先後以「存活至開始透析」、「確實開始透析」及「仍留在原分派治療」為條件；這是高度選擇的事後族群，無法保留可回答透析療效的原始隨機比較。

### 最終裁決與證據分級

| 可說的主張 | 裁決 |
|---|---|
| eGFR<25 的療效 | **未知**。FLOW 收案下限為 eGFR 25；eGFR<30 次族群不是 eGFR<25 的替代資料，也不能回答低於 25 的停藥或持續治療效果。 |
| 隨機後有多少人降至 eGFR<25，以及其後實際曝藥多久 | **未報告／不可由現有整理判定**；不能用基線 eGFR<30 分層補算。 |
| 對已接受維持性透析者起始 semaglutide 的療效 | **未知**。FLOW 在設計上排除目前或近期透析者。 |
| 開始透析後持續原分派用藥的安全性 | **描述性／初步提示性**。來源報告 34,064 人中 307 人開始透析，只有 165 人持續原分派治療；其中嚴重不良事件為 45% 對 57%。這可提供有限的 continuation-safety 安心，但不能說 semaglutide 比安慰劑更安全。 |
| 透析後 MACE 9.7 對 16.1、死亡 13.8 對 18.1 事件／100 病人年 | **假說生成**。不可換算成 40% 或 24% 的風險降低，也不能作因果療效結論。 |
| 「不需腎功能劑量調整」可證明 eGFR<25 或透析中的療效／耐受性 | **明確否決**。這是 PK／標籤事實，沒有療效或個別耐受性的內容。 |
| 衰弱、肌少症與營養風險已被 FLOW 排除 | **未知／未測量**；creatinine 與 cystatin-C 結果一致也不能回答身體組成或營養結局。 |
| 透析分析中的「持續原分派治療」必然代表全程不中斷 | **未能由 structured abstract 判定**；其中是否容許暫停後重新開始，不能自行補成連續曝藥。 |

### 建議採用的繁中表述

> FLOW 的隨機療效證據止於收案下限 eGFR 25，不能把 eGFR<30 次族群外推成 eGFR<25 的證據；對已接受維持性透析者，也沒有起始 semaglutide 的隨機療效資料。事後彙總分析僅對「試驗中開始透析且之後仍持續原分派治療」的選定病人提供初步、描述性的 continuation-safety 訊號，不能證明透析療效或安全優越性。「不需腎功能劑量調整」只回答 PK，不回答療效、營養承受度或衰弱病人的耐受性。

### 穩定來源與精確定位

- `FLOW-PROTOCOL-2021`：[ClinicalTrials.gov NCT03819153](https://clinicaltrials.gov/study/NCT03819153) 所附 trial protocol synopsis pp.6–7（兩條 eGFR／UACR 收案路徑與 eGFR 下限）；`FLOW-SUPPLEMENT-2024`：Eligibility Criteria—Exclusion，supplement pp.11–13（透析與移植排除）。
- `FLOW-CKDSEVERITY-2026-CJASN`：Figure 1 及 Results（eGFR<30 次族群 n=400，HR 0.81〔0.58–1.13〕，仍含心血管死亡）；[DOI 10.2215/CJN.0000000974](https://doi.org/10.2215/CJN.0000000974)；[PubMed 41706532](https://pubmed.ncbi.nlm.nih.gov/41706532/)；[PMCID PMC13143484](https://pmc.ncbi.nlm.nih.gov/articles/PMC13143484/)。
- `FLOW-DIALYSIS-SAFETY-2026`：PubMed structured abstract「Research Design and Methods」、「Results」及「Conclusions」（34,064、307、165、嚴重不良事件／停藥／MACE／死亡事件率，以及需正式療效試驗的限制）；[DOI 10.2337/dc26-0112](https://doi.org/10.2337/dc26-0112)；[PubMed 41893299](https://pubmed.ncbi.nlm.nih.gov/41893299/)。
- `FDA-OZEMPIC-USPI-S038-2026`：[DailyMed 現行 Ozempic 標籤](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=adec4fd2-6858-4c99-91d4-531f5f2a2d79)之 Renal Impairment §8.6 與 Clinical Pharmacology（腎功能劑量調整／PK 陳述）；此定位不得用來支持超出試驗邊界的療效。

### 受影響的文章與投影片

- 文章 04：「低血糖、胃腸與營養：晚期 CKD 的真正取捨」、「晚期 CKD 的床邊清單」、「洗腎證據：延續用藥與新開始用藥是不同問題」、「內分泌科與腎臟科」。
- 文章 05：病例 C、22 問第 16–18 題、「先確認是否站在 FLOW 證據內」及證據邊界族群。
- 投影片 3、19–21：收案族群、整體安全性、晚期 CKD 風險與透析 continuation safety。

## 爭點四｜腎臟保護是否獨立於體重／血糖？creatinine–cystatin C 一致性排除了什麼？

### 問題與不同觀點

- **內分泌科角色**認為體重、血糖與血壓改善很可能是整體腎臟效益的一部分，反對把它們貶為與腎臟無關的「雜訊」。
- **腎臟科角色**重視 creatinine 與 cystatin-C 的方向一致，因為它降低「體重／肌肉量下降只讓 creatinine 看起來改善」的疑慮；同時要求把 UACR、斜率、硬終點與機轉分開。
- **方法學角色**指出標記一致性只能處理特定測量偏誤，不能區分完全由體重中介、部分中介或與體重無關。不同試驗、不同終點的中介比例也不能相加、平均或互相否決。

### 最終裁決與證據分級

| 可說的主張 | 裁決 |
|---|---|
| FLOW 的主要臨床結果與總 eGFR 斜率改善 | **已確立**。 |
| UACR 降低 | **高度支持／支持性**；是預設分析但位於確認性階層外，不是已證實的因果中介。 |
| week 104 creatinine-based 3.30 與 cystatin-C-based 3.39 mL/min/1.73m² 的近似一致 | **高度支持「不是純粹由體重／肌肉量流失造成的 creatinine 假象」**；未報兩者差值的 CI，不能量化一致強度，也不能泛稱「排除所有測量假象」。 |
| FLOW 已證實療效獨立於體重或血糖 | **未確立**。FLOW 沒有正式中介分析；一致性檢查對「是否由體重中介」沒有辨別力。 |
| 以 FLOW 已有體重資料重算中介比例即可得到因果答案 | **不成立**。數值上也許可擬合模型，但治療造成的減重與疾病惡化造成的減重可能具有相反預後意義，且缺少身體組成資料，因果解讀仍不可識別。 |
| SUSTAIN-6 的體重中介 0% | **資訊不足以證明零中介**；CI 無法計算。 |
| SELECT 的體重中介 81%（41–120%） | **提示性**；估計的是 week-104 eGFR change，不是 FLOW 硬終點或斜率，且是不同族群與模型。不得與 0% 平均。 |
| week 12 無差異 dip 可排除任何早期血流動力效應 | **不成立**；兩組從 baseline 到 week 12 都下降，且只在該區間未見組間差異，不能排除更早且短暫的變化。 |

### 建議採用的繁中表述

> FLOW 的 creatinine 與 cystatin-C 結果近似一致，支持觀察到的腎功能差異不是單純由體重／肌肉量下降造成的 creatinine 測量假象；它不能排除所有測量問題，也不能證明效果獨立於體重、血糖或血壓。現有中介研究來自不同試驗、族群與終點，結果不精確且不可合併；FLOW 內部的體重、血糖、血壓與 UACR 中介比例仍未知。因此，合理說法是「機轉可能多重且尚未完成因果分解」，而不是「只靠體重／血糖」或「完全獨立於體重／血糖」。

### 穩定來源與精確定位

- `FLOW-PRIMARY-2024`：Table 2，journal p.116（總／慢性 eGFR 斜率、week-12 變化）；Results「Other Outcomes」，journal p.116，及 Discussion，journal pp.119–120（week-104 creatinine-與 cystatin-C-based 對照）。[DOI 10.1056/NEJMoa2403347](https://doi.org/10.1056/NEJMoa2403347)；[PubMed 38785209](https://pubmed.ncbi.nlm.nih.gov/38785209/)。
- `FLOW-SUPPLEMENT-2024`：Figure S2A，supplement p.19（UACR 時序）；Table 2／主要論文 p.116 為 week-104 UACR 正式估計。
- `SUSTAIN6-MEDIATION-2021`：Methods §2.2／「Mediation analysis」、Results、Tables 2–3 及 Figure 1A–F（各候選中介分開估計與無法計算的 CI）；[DOI 10.1111/dom.14443](https://doi.org/10.1111/dom.14443)；[PubMed 34009708](https://pubmed.ncbi.nlm.nih.gov/34009708/)；[PMCID PMC8453827](https://pmc.ncbi.nlm.nih.gov/articles/PMC8453827/)。
- `SELECT-KIDNEY-2024`：Methods「Correlation and mediation analysis」、Results「Correlation and mediation between eGFR change and changes in body weight, blood pressure and glycated hemoglobin」、Table 1 及 Figures 1–5；[DOI 10.1038/s41591-024-03015-5](https://doi.org/10.1038/s41591-024-03015-5)；[PubMed 38796653](https://pubmed.ncbi.nlm.nih.gov/38796653/)；[PMCID PMC11271413](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271413/)。

### 受影響的文章與投影片

- 文章 03：「SELECT」、「腎臟保護可能怎麼發生」及三個機轉子節；文章 01：「eGFR 斜率提供另一條腎臟證據線」。
- 投影片 9、10、18：eGFR 時序、UACR 與中介界線、機轉證據階梯。

## 爭點五｜哪一種表現型絕對獲益最大？FLOW、SELECT、SOUL 與 pooled analysis 能否直接對齊？

### 問題與不同觀點

- **內分泌科角色**希望用 ASCVD、HF、肥胖、血糖與 CKD 表現型找出最具臨床價值的使用情境，並把 FLOW、SELECT 與 SOUL 放入同一個多風險照護框架。
- **腎臟科角色**要求「最大絕對腎臟獲益」必須有同一定義終點、同一時間窗與各 eGFR／UACR／KDIGO 分層的 ARR 或 NNT；只有 CV 表現型 NNT 不能回答 CKD 嚴重度問題。
- **方法學角色**強調沒有偵測到交互作用不等於各層效果相同；不同 NNT 可只由不同基線風險在數學上產生，但目前沒有完成實證分解。跨試驗比較還必須逐項核對複合終點組成，不能只看名稱或「含／不含 CV death」。

### 最終裁決與證據分級

| 可說的主張 | 裁決 |
|---|---|
| FLOW 收案表現型接受 1.0 mg SC semaglutide 的五項主要複合終點、MACE 與全因死亡結果 | **已確立**於 FLOW 的整體試驗族群；不能自動外推到不同劑量、途徑或未收案族群。 |
| 哪個 eGFR、UACR 或 KDIGO 表現型有最大絕對腎臟獲益 | **未知**；沒有已發表的分層 ARR／NNT。 |
| HF 13、高風險但無已確立 CVD 17、ASCVD 22 的三年 NNT | **描述性 CV 表現型結果**，終點仍是含 CV death 的 FLOW 五項複合終點；三數差異在數學上可完全由設計上不同的基線風險造成，但現有資料未完成實證分解，不能由此宣稱 HF 是「最佳腎臟反應者」。 |
| 沒有顯著交互作用證明所有表現型療效等同 | **未確立**；現有結果只表示未偵測到差異，也不能反向聲稱已證實同質性。 |
| SELECT、FLOW、SOUL pooled HR 代表三個可獨立排名的試驗估計 | **否**。PubMed structured abstract Methods 已核實 pooled endpoint 定義：主要複合含持續 ≥50% eGFR 下降、腎衰竭、腎因性死亡或 CV death；次要較窄複合排除 CV death。但 pooled HR 已包含 FLOW、SELECT、SOUL 資料，與母試驗統計相依，不能與 FLOW 0.76／0.79、SOUL 0.91／0.86 當成三個獨立數值比較或排名。 |
| pooled analysis 證明跨劑量、途徑、糖尿病狀態的等效性 | **未確立**；pooled aggregate 估計本身可視為**已確立**，但異質性消失、機轉獨立與劑量／途徑等效都不是由該 aggregate HR 證明。 |
| SELECT 與 SOUL 可分別如何讀 | SELECT 為不同族群、2.4 mg SC，複合終點包含新發持續性 macroalbuminuria，效果主要來自 macroalbuminuria 與 ≥50% eGFR decline，移除 macroalbuminuria 後的複合分析未達顯著；SOUL 的硬腎臟複合終點未達顯著，且在階層閘門失敗後的斜率屬正式探索性。兩者都不能單獨歸因於劑量或途徑。 |

**來源校正（2026-09-06）：** Wave 4 對 pooled endpoint 的原始「組成未核實」判斷已被官方 PubMed structured abstract 的 Methods 取代；上表保留跨試驗推論護欄，但把理由改為 pooled estimate 與母試驗的統計相依性及臨床異質性。這是來源層級的更正，不是新的同儕共識。

FLOW 的四項腎臟專屬結果與 SOUL 的腎臟結果都不是確認性陽性結論，但原因不同：前者是 nominal CI 未跨 1、卻位於確認性階層外的支持性分析；後者是第一個確認性腎臟複合終點未達顯著，令後續斜率正式降為探索性。不能只用「都不是 confirmatory」抹平兩者差異。

每個 NNT 都必須同時標明：所屬終點、是否包含心血管死亡、時間範圍，以及是全試驗估計或探索性次族群估計。本證據庫目前可用的 NNT 均對應含 CV death 的複合終點或 CV／死亡終點，沒有可作為 semaglutide 腎臟專屬效果標題的 NNT。

### 建議採用的繁中表述

> 對符合 FLOW 收案條件的 T2D＋albuminuric CKD 病人，1.0 mg 皮下注射 semaglutide 的整體試驗效益已確立；但目前無法指出哪個 eGFR、UACR 或 KDIGO 層級具有最大絕對腎臟獲益。已發表的 NNT 13、17、22 只對應三種 CV 表現型與含 CV death 的五項複合終點，其差異在數學上可完全由不同基線風險造成，現有資料並未完成對三個數值的實證分解。Pooled endpoint 定義已由 PubMed Methods 核實，但 pooled HR 包含各母試驗資料，與之統計相依；因此 FLOW、SELECT、SOUL 應各自按族群、劑量、途徑、終點組成與檢定階層解讀，pooled HR 作整合估計，不與母試驗當成三個獨立數值排名，也不能證明劑量或途徑等效性。

### 穩定來源與精確定位

- `FLOW-CVPHENOTYPE-2026`：PubMed structured abstract「Results」（ASCVD、HF、高風險但無已確立 CVD 的 HR、P-interaction 與三年 NNT）；[DOI 10.1016/j.jacc.2026.02.5125](https://doi.org/10.1016/j.jacc.2026.02.5125)；[PubMed 42233552](https://pubmed.ncbi.nlm.nih.gov/42233552/)。
- `FLOW-CKDSEVERITY-2026-CJASN`：Figures 1–2 及 Results（eGFR／UACR 分層 HR 與交互作用；未提供對應 ARR／NNT）；[DOI 10.2215/CJN.0000000974](https://doi.org/10.2215/CJN.0000000974)；[PubMed 41706532](https://pubmed.ncbi.nlm.nih.gov/41706532/)；[PMCID PMC13143484](https://pmc.ncbi.nlm.nih.gov/articles/PMC13143484/)。
- `SELECT-KIDNEY-2024`：Abstract；Results「Effect of semaglutide on the main kidney endpoint」；Methods；Table 1 與 Figures 1–5（不同終點組成及 macroalbuminuria 驅動性）；[DOI 10.1038/s41591-024-03015-5](https://doi.org/10.1038/s41591-024-03015-5)；[PubMed 38796653](https://pubmed.ncbi.nlm.nih.gov/38796653/)；[PMCID PMC11271413](https://pmc.ncbi.nlm.nih.gov/articles/PMC11271413/)。
- `SOUL-KIDNEY-2026`：PubMed structured abstract「Research Design and Methods」及「Results」（五項／四項複合終點與 eGFR 斜率）；[DOI 10.2337/dc25-1080](https://doi.org/10.2337/dc25-1080)；[PubMed 41380027](https://pubmed.ncbi.nlm.nih.gov/41380027/)。檢定階層另見 `SOUL-PROTOCOL-2021` §10.3.2.1，p.50（[ClinicalTrials.gov NCT03914326](https://clinicaltrials.gov/study/NCT03914326) 所附 protocol）。
- `SELECT-FLOW-SOUL-POOLED-2026`：PubMed structured abstract「Methods」（兩個 pooled endpoint 定義）與「Findings」（事件數、HR）；[DOI 10.1016/S2213-8587(26)00134-8](https://doi.org/10.1016/S2213-8587%2826%2900134-8)；[PubMed 42567173](https://pubmed.ncbi.nlm.nih.gov/42567173/)。全文、表格與附錄未取得，故未擴張至摘要未報告之 component-level treatment effects 或試驗間異質性。

### 受影響的文章與投影片

- 文章 02：「CKD 嚴重度：沒有異質性，不等於知道誰絕對獲益最大」。
- 文章 03：「三個試驗，其實在問三個不同問題」、「SELECT」、「SOUL」、「彙總分析」。
- 文章 05：五個病例、22 問及表現型分層演算法。
- 投影片 13、16、17、23–25：絕對效益空白、三試驗差異、pooled／類別訊號、共同表現型與結論。

## 兩個專科觀點如何互相校正

| 臨床問題 | 內分泌科較常優先追問 | 腎臟科較常優先追問 | 合併後的較佳表述／流程 |
|---|---|---|---|
| 為何使用 semaglutide | HbA1c、體重、ASCVD／MACE、死亡與整體代謝風險能否一起改善？ | 終點是否真正反映腎臟；是否降低腎衰竭、減緩 eGFR、降低 UACR？ | 先說清楚目標是五項 cardiorenal composite、eGFR slope、體重／血糖或 CV outcome；不可用一個目標替代另一個。 |
| 已有 RASi／SGLT2i／MRA | 病人仍有多重殘餘風險時，如何務實加藥與提高可接受度？ | 是否有在背景治療上隨機證實的增量硬腎臟效益；血鉀、容量與腎功能能否承受？ | 採表現型導向排序並公開未知，不宣稱固定順序、加成性或等值「支柱」。 |
| 晚期 CKD | 低內在低血糖風險、PK 不需腎功能調整與持續治療的實務性。 | 是否已越過 eGFR 25 的療效邊界；GI 攝取、腎前性 AKI、衰弱／肌少與營養風險。 | 把 PK、療效、耐受性分三欄；低 eGFR／透析需慢滴定、容量與營養監測，且明示療效 unknown。 |
| 機轉 | 體重、血糖、血壓與發炎等多路徑可能共同作用。 | creatinine 是否受肌肉量干擾；UACR 是否只是標記；是否有直接腎元證據。 | 將 outcome、surrogate、measurement check 與 causal mediation 分層，不寫成單一路徑或「完全獨立」。 |
| 誰最有利 | 依肥胖、血糖、ASCVD／HF 與 CKD 的多風險表現型整合治療。 | 需要同終點、同時間窗的腎臟 ARR／NNT，並關心 eGFR／UACR／KDIGO 絕對風險。 | 可確認 FLOW eligible phenotype，不可宣布全域最佳表現型；所有 NNT 都附終點、CV death 與時間窗。 |

方法學角色在兩者之間提供第三層護欄：未偵測到交互作用不等於等效；nominal CI 不等於確認性結果；事後選定族群不保留原始因果比較；跨試驗 pooled estimate 不會自動消除終點、族群、劑量與途徑差異。

## 本輪仍未解答的問題

1. eGFR<25、已接受維持性透析、移植後、第一型糖尿病、絕大多數非糖尿病 CKD、持續性低 UACR／正常白蛋白尿 CKD，以及衰弱／肌少症 CKD 的臨床療效。
2. semaglutide 在已使用 SGLT2i 者的增量硬腎臟效益，以及與 finerenone 併用的隨機硬終點加成性。
3. 哪一個 eGFR、UACR 或 KDIGO 分層具有最大絕對腎臟獲益；目前沒有相應的 ARR／NNT。
4. FLOW 族群內體重、HbA1c、血壓與 UACR 對臨床結果的正式因果中介比例，以及直接人類腎臟細胞／組織機轉。
5. pooled SELECT／FLOW／SOUL 中摘要未報告的 component-level treatment effects、trial-level heterogeneity，以及各劑量／途徑的獨立效應；後兩者不能由一個包含母試驗的 pooled HR 推導。
6. 透析後持續治療的真正療效與長期耐受性；現有小型、事後且經選擇的資料不足以回答。

## 使用這份增補時的底線

- 第二輪確實完成了跨會話對話；第一輪失敗不得再被描述成第二輪也沒有對話。
- 這次校讀證實了多個原本方向正確但可能「多說一步」的風險：確認性與支持性混淆、次族群加成性、PK 外推療效、測量一致性外推機轉，以及 NNT／pooled endpoint 的過度對齊。
- 所有公開文章與簡報應採用上述校準語句；若未來取得 pooled 全文／附錄、eGFR<25 或透析隨機資料、或正式組合治療試驗，應另行更新，而不是回填成這一輪已經知道。
