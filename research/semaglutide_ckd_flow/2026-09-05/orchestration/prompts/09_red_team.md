# Session brief — Adversarial clinical evidence reviewer

Read `CLAUDE.md`, the master prompt, all final numbered files, the five standalone
Traditional-Chinese articles plus their README, and the source/acquisition ledgers.
Write `17_RED_TEAM_QA.md` only.

Independently audit:

1. every headline event count, HR/RR, CI, P value, slope, UACR change, ARR and NNT;
2. endpoint labels, denominators, time horizons, prespecified/post hoc status and interaction claims;
3. CV-death-inclusive versus kidney-specific wording;
4. additive-therapy claims for SGLT2i and finerenone;
5. extrapolation to low UACR, eGFR <25, non-diabetic CKD, dialysis/transplant and frailty;
6. FDA/EMA/Taiwan and guideline status as of 2026-09-05;
7. citation links, source IDs and whether cited sources actually support the sentence;
8. internal consistency between `14_MASTER_EVIDENCE_TABLE.md`, `15_CLAIM_EVIDENCE_MAP.md` and `16_FINAL_SYNTHESIS_ZH_TW.md`.
9. acquisition/license provenance, parse-QA warnings, and whether any restricted
   PDF/derived Markdown, key, token, or cache artifact has been tracked;
10. the known high-risk corrections: Mahaffey Figure 2, CV-death nonpartition,
   MRA N=257/finerenone=0, SGLT2 hard-composite HRs >1, pooled-paper online date,
   EMA 4.1 versus 5.1, and the 26% versus 28.8% discontinuation discrepancy.
11. the isolated nominal component-interaction signals: sustained ≥50% eGFR
    decline by baseline SGLT2i use (P-interaction=.023) and RRT initiation by
    baseline MRA use (P-interaction=.027), ensuring neither is omitted or promoted
    to proof of harm, additivity, or true effect modification.

Before finishing, use `ListAgents` to locate the exact `flow-director-wave3-main`
session and send one structured `CHALLENGE REDTEAM-FINAL` message summarizing every
BLOCKER/MAJOR finding, or an explicit `CONFIRM REDTEAM-FINAL` if none remain. Record
the actual delivery state in `17_RED_TEAM_QA.md`; a held/expired attempt is not a
delivered message. Do not resume, fork, or modify any other session.

Classify findings as BLOCKER, MAJOR, MINOR or INTERPRETIVE DISAGREEMENT. For every
BLOCKER/MAJOR item, give exact source evidence and replacement text. Do not expose
secrets, change Claude settings, upload restricted files, edit source/fulltext
artifacts, or push. Commit only `17_RED_TEAM_QA.md`.
