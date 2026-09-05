# Semaglutide × CKD：繁體中文投影片證據包

這個資料夾把已完成的 FLOW／semaglutide CKD 證據綜述，轉成可直接準備學術演講的素材。建議主版本為 **25 張、20–25 分鐘**；若只有 12–15 分鐘，可保留 Slide 1、3–7、9、11、14–16、19、21、23、25。

## 交付內容

- `SLIDE_STORYBOARD_ZH_TW.md`：每張投影片的單一訊息、視覺型態、來源與解讀警語。
- `SPEAKER_NOTES_ZH_TW.md`：每張 30–60 秒講稿、腎臟科／內分泌科視角、預期提問與轉場。
- `FIGURE_TABLE_SOURCE_MAP.md`：原論文 Table／Figure／頁碼到投影片用途的逐項對照。
- `ARTICLE_REFERENCE_GUIDE.md`：五篇文章應放置的 reference 輔助與投影片跳轉。
- `PRIVATE_ASSET_MANIFEST.md`：本機截圖清單、SHA-256、授權界線與公開替代方案。
- `public_assets/`：已逐圖確認可公開重製的原圖；每張均附 license、來源、SHA-256 與變更聲明。
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

## 可直接使用的公開圖例

![FLOW 依 CKD 嚴重度分層之 MACE 結果](./public_assets/FLOW_CKDSEVERITY_Mahaffey_Figure2.jpg)

這張 Figure 2 適合放在「不同 CKD 嚴重度下，心血管效益是否一致？」一頁。閱讀時應先看各分層的 semaglutide 對 placebo 效果，再看 interaction P 值；交互作用未達顯著不代表各層效果已被證明完全相同，也不能由此推算分層 ARR 或 NNT。圖檔來自官方 PMC、未修改，公開使用時請保留 [`public_assets/ATTRIBUTION.md`](./public_assets/ATTRIBUTION.md) 的 CC BY 4.0 credit；若裁切、翻譯或加標記，請改註為 `Adapted from` 並描述變更。

證據截止日為 2026-09-05；本資料包不構成個人化醫療建議。
