---
name: today
description: >-
  Use when JJ asks what to study today or types /today. Shows today's 90-minute plan from the date, PLAN.md and PROGRESS.md.
---
1. Run `date`. Read `PLAN.md` and `PROGRESS.md`.
2. Determine the **current week** = the earliest week whose gate is not yet fully passed in PROGRESS.md (not the calendar week — if JJ is behind, stay on the unfinished week and say how many days behind).
3. Compute this week's hours used vs the 7.5 h cap.
4. Output in Korean, compactly:
   - 현재 주차 / 주제 / 게이트 상태 (3 checks)
   - 오늘 90분 블록 (template from PLAN.md), with the **exact shelf section + page** and the **exact derivation/NumPy task** still open
   - If the week's hours are already ≥ 7.5: say so and propose only the 15-min floor (1 Tutor question).
5. Do not teach anything here. End with the single first action ("MML 5.1 p.141 열고 30분 타이머").
