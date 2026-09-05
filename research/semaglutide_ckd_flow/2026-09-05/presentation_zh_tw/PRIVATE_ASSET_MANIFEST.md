# 本機來源截圖 manifest

下列檔案存放於 gitignored `sources/retrieved/cache/presentation_assets/source_pages/`，供個人研究、演講準備與來源核對。**它們不會被推送到公開 GitHub。** 公開簡報應優先使用 `chart_data/` 重繪；若要公開原圖，需逐圖確認 license、attribution 與第三方素材例外。

| 本機檔名 | SHA-256 | 內容 | 適合投影片 | 權利／公開處理 |
|---|---|---|---:|---|
| `FLOW_PRIMARY_p04_Table1A.png` | `7f5521a2ebf5559b3d65e4fdfae61cc680d61ef6c9b2d70fbe1973696a9fb4ec` | FLOW Table 1 前半 | 3–4 appendix | NEJM；本機核對用，不公開 |
| `FLOW_PRIMARY_p05_Table1B.png` | `27690a8808186cc2fd633437913f5cf7a821d04ab6cf6d63f7d91c5d8290b1b3` | FLOW Table 1 後半、背景藥物 | 4 appendix | NEJM；本機核對用，不公開 |
| `FLOW_PRIMARY_p06_Figure1.png` | `53119841485e9b4df7a8e271ccdfa182253e1527fdf4c7d2b33bfcb47488b235` | 主要 endpoint 累積發生曲線 | 6 appendix | NEJM；本機核對用，不公開 |
| `FLOW_PRIMARY_p08_Table2.png` | `d168e2c3d18756042a6c09adfc043819abf54f644248e76c219bc6cfad03e12a` | 主要、components、腎臟專屬、MACE、斜率 | 5–9 appendix | NEJM；本機核對用，不公開 |
| `FLOW_PRIMARY_p10_Figure2.png` | `fb4d397dee14d24cee3754fe25783f3704a771af1197d93728437190278cc1db` | 預先指定主要終點森林圖 | 12–14 appendix | NEJM；本機核對用，不公開 |
| `FLOW_PRIMARY_p12_Table3.png` | `4115692d1a8ec87617aae272e4f54ca0be3aa7b834837bb7fe6e22bc5caca8cd` | 整體 safety/SAE | 19 appendix | NEJM；本機核對用，不公開 |
| `FLOW_SUPP_p16_InterimMethods.png` | `bb14c52ad790aed5ff6efce4ce4222bd12ab92c6b80fb96f70a851abfaaae6c1` | 期中分析的群組序貫方法與 DMC／lock 紀錄 | 11 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_SUPP_p17_Hierarchy.png` | `55a3c1e312361c5ee2b63785ec0cc512fbf69d3a7c08ef410a3abc38bc68d9cf` | 確認性次要終點的階層順序 | 11 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_SUPP_p18_FigureS1.png` | `f4134aa7737b33019928e99f1e790a6b5e86007e05e0090693b8db233fcf0735` | Figure S1 病人流程圖 | 3／11 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_SUPP_p19_FigureS2.png` | `149ca4df721944eb562df554226140c6d196b9108032a2df3b657d0c34d94c25` | UACR／體重等變化 | 10 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_SUPP_p28_TableS4.png` | `821e74f8b2dda76e2dd32acf47b59d3734a1589cffc5479826cc402378b564a3` | Table S4 起始頁 | 19–20 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_SUPP_p29_TableS4_AKI.png` | `023ca25a677aec8bb21209f61c2c22fdd6c0d44ad31f094e78ff61758165397d` | Table S4 的 AKI 與 serious GI preferred-term 列 | 19–20 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_SUPP_p30_TableS4_Dehydration.png` | `1bf367e2dd3b4b84771bc7cb62a82ba0eb204f35780a5c9f4c544d8f5d76f3f9` | Table S4 的 dehydration、hypoglycemia 與 eye-disorder 列 | 19–20 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_SUPP_p32_TableS5.png` | `1c654e1fa8cfc06aff7317fecc6e70b593c0e969fcbd7ec5e088438178b73c85` | permanent discontinuation | 19 appendix | NEJM supplement；本機核對用，不公開 |
| `FLOW_CKDSEVERITY_p08_Figure2.png` | `eb3d9e1105ffcde188ba083e3d56cbe15461fd249160844d63e0fbaac2e7c9c1` | Mahaffey Figure 2 與同頁 Figure 3 | 12–13 appendix | 來源為 CC BY 4.0；公開資料夾另放官方未修改 Figure 2 與完整 attribution |

## 截圖旁的固定說明格式

1. **圖表在回答什麼：** 先寫 population、endpoint、time horizon。
2. **看到什麼：** 報 effect estimate、CI、interaction 或事件數。
3. **不可怎麼說：** 指出 hierarchy、多重比較、additivity 或外推限制。
4. **來源：** `Source ID · Table/Figure · page · DOI/PMID`。

示例（FLOW Table 2）：

> 這張表同時放入含 CV death 的五項確認性主要終點與排除 CV death 的四項支持性腎臟複合；兩者方向一致，但不能把 HR 0.79 升格為確認性結果，也不能從 component counts 推導 CV death 的療效占比。
