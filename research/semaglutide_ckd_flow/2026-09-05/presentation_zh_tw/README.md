# Semaglutide × CKD：繁體中文投影片證據包

這個資料夾把已完成的 FLOW／semaglutide CKD 證據綜述，轉成可直接準備學術演講的素材。除了 25 張 storyboard 與逐張講稿，現在另含 **6 組繁中與 6 組英文重繪圖（每組 SVG＋3840×2160 PNG）**、**5 張逐圖核實為 CC BY 4.0 的原始英文出版圖**，以及 **20 張僅供本機來源核對的 PDF 頁面／裁圖**。建議主版本為 **25 張、20–25 分鐘**；若只有 12–15 分鐘，可保留 Slide 1、3–7、9、11、14–16、19、21、23、25。

投影片中的五個高風險論述（終點、疊加治療、晚期 CKD／透析、機轉、表現型）已由腎臟科、內分泌科與方法學角色完成真實跨會話校讀；公開裁決與可直接使用的繁中措辭見 [`../19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md`](../19_WAVE4_PEER_REVIEW_ADDENDUM_ZH_TW.md)。

## 交付內容

- `SLIDE_STORYBOARD_ZH_TW.md`：每張投影片的單一訊息、視覺型態、來源與解讀警語。
- `SPEAKER_NOTES_ZH_TW.md`：每張 30–60 秒講稿、腎臟科／內分泌科視角、預期提問與轉場。
- [`VISUAL_ASSET_CATALOG_ZH_TW.md`](./VISUAL_ASSET_CATALOG_ZH_TW.md)：8 項公開視覺的預覽、投影片用途、圖說、30 秒講稿、不可說事項與 exact locator。
- [`ENGLISH_ORIGINAL_VISUAL_GUIDE.md`](./ENGLISH_ORIGINAL_VISUAL_GUIDE.md)：英文原文忠實版；區分 source-locked wording、project redraw 與 project note，並附 20–30 秒英文 speaker cue。
- `FIGURE_TABLE_SOURCE_MAP.md`：原論文 Table／Figure／頁碼到投影片用途的逐項對照。
- `ARTICLE_REFERENCE_GUIDE.md`：五篇文章應放置的 reference 輔助與投影片跳轉。
- `PRIVATE_ASSET_MANIFEST.md`：本機截圖清單、SHA-256、授權界線與公開替代方案。
- [`public_assets/redrawn/`](./public_assets/redrawn/)：6 組原創重繪圖，每組有 SVG 與 2× PNG；可由 repository root 的 [`scripts/generate_presentation_visuals.py`](../../../../scripts/generate_presentation_visuals.py) 重製。
- [`public_assets/redrawn_en/`](./public_assets/redrawn_en/)：6 組英文原文忠實重繪圖；endpoint／axis／legend 採來源英文，計畫解讀另置於 `Project note`；可由 [`scripts/generate_presentation_visuals_en.py`](../../../../scripts/generate_presentation_visuals_en.py) 重製。
- `public_assets/` 與 `public_assets/source_figures/`：5 張已逐圖確認可公開重製的 CC BY 4.0 原圖；每張均附 license、來源、SHA-256 與變更聲明。
- `chart_data/`：可在 PowerPoint、Keynote、Google Slides 或 Canva 重新繪圖的 CSV；數值不得脫離同列的 endpoint 與推論狀態。

## 三層素材規則

1. **演講投影優先用重繪圖。** 可放大、可改字體，也能保留 endpoint 邊界與 CI。
2. **原文截圖用於證據追溯。** 一張只聚焦一個 Table／Figure，旁邊加來源、頁碼與一句解讀；不把整頁密集表格當主要視覺。
3. **公開 GitHub 不收受限制全文或截圖。** NEJM、ADA、AHA／ACC 等來源頁面只保留在 gitignored 本機 cache；公開版放 source map、官方連結與可重繪資料。CC BY 圖像也必須保留完整 attribution。

## 統一頁腳格式

`Source ID · Table/Figure/section · journal/PDF page · DOI/PMID（首次出現時）`

範例：`FLOW-PRIMARY-2024 · Table 2 · NEJM p.116 · doi:10.1056/NEJMoa2403347`

## 必守的五句邊界

- FLOW 的確認性主要終點是 **五項複合終點，包含 CV death**。
- 四項腎臟專屬複合 HR 0.79 為支持性、位於確認性階層之外且未校正多重比較。
- 基線 SGLT2i 與 MRA 分析不足以證明 semaglutide 的增量硬腎臟效益或加成性。
- 「不需依腎功能調整劑量」不是 eGFR <25 或透析療效已成立的證據。
- 森林圖中一側顯著、另一側不顯著，不等於交互作用成立。

## 建議製作方式

- 主結果使用可編輯的 paired endpoint 表或 forest plot；把 HR 0.76 與 0.79 放在同一張。
- eGFR 使用三段式圖：基線至 week 12、week 12 後慢性斜率、總斜率。
- SGLT2i／MRA 以「證據紅綠燈」呈現：整體方向、CI／事件數、interaction、可說與不可說。
- 每張數據投影片右下角放 1 行 locator，講者備註再放完整 citation。
- 原始截圖只在 Q&A 或 appendix 使用；正式主畫面用重繪圖與 1 句結論。

## 可直接使用的重繪圖例

![FLOW 五項、四項與個別組成 forest](./public_assets/redrawn/01_flow_endpoints_forest_zh_tw@2x.png)

這張重繪圖可直接用於 Slide 5–7；它同時保留事件數、HR、95% CI、無效線、endpoint definition 與推論層級。另 5 張重繪圖涵蓋 eGFR 三階段、SGLT2i、MRA、SELECT／SOUL／pooled 與安全性，詳見[視覺素材總目錄](./VISUAL_ASSET_CATALOG_ZH_TW.md)。

## 可直接使用的公開來源圖

![FLOW 依 CKD 嚴重度分層之 MACE 結果](./public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg)

這張 Figure 2 適合放在「不同 CKD 嚴重度下，心血管效益是否一致？」一頁。閱讀時應先看各分層的 semaglutide 對 placebo 效果，再看 interaction P 值；交互作用未達顯著不代表各層效果已被證明完全相同，也不能由此推算分層 ARR 或 NNT。圖檔來自官方 PMC、未修改，公開使用時請保留 [`public_assets/ATTRIBUTION.md`](./public_assets/ATTRIBUTION.md) 的 CC BY 4.0 credit；若裁切、翻譯或加標記，請改註為 `Adapted from` 並描述變更。

SELECT Figure 1 的 Kaplan–Meier 圖另見 [`public_assets/source_figures/SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png`](./public_assets/source_figures/SELECT_KIDNEY_Colhoun_2024_Figure1_KM.png)。該檔保留 HR／CI／P、完整 number at risk 與 endpoint definition；它是 crop-only adaptation，公開使用時須保留相鄰 [`ATTRIBUTION.md`](./public_assets/source_figures/ATTRIBUTION.md) 的 CC BY 4.0 credit，並明說 SELECT 的終點包含新發持續性巨量白蛋白尿、排除 CV death。

Mann 等人 FLOW SGLT2i 次族群的官方英文 Figures 1–3 也收在 [`public_assets/source_figures/`](./public_assets/source_figures/)；三檔皆為官方 PMC JPEG、未修改。Figure 2 的出版圖本身存在 231 對 213 的事件數差異，請保留原圖並在旁邊加獨立說明，或改用已核對數據的英文 V03 重繪圖。

證據截止日為 2026-09-05；本資料包不構成個人化醫療建議。
