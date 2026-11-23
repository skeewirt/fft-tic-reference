# Errand_ComputeRewards

- **Address:** `0x1402D29C0`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void Errand_ComputeRewards(int activeSlot)`
- **Callers:** `sub_1402ED540`, `Errand_ReportListInput`
- **Callees:** Errand_LoadRecord, Errand_ScoreParty, Errand_RollBonusLoot

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Computes JP and gil rewards, the grade and the bonus loot for one active errand when it ends.

## Behavior

- V: loads the record of the active slot's errand and records the slot number; then chooses a featured unit.
- V: the selector word decides it: 1 highest Brave, 2 lowest Brave, 3 highest Faith, 4 lowest Faith; a single unit is featured as is.
- V: calls Errand_ScoreParty, then, unless failure is forced, sets each unit's JP from the JP tier table and its gil from the gil tier table, scaled by the grade (JP 100, 10 or 5 percent; gil 100, 20 or 5 percent), plus the unit's score.
- V: calls Errand_RollBonusLoot, which may add more JP, a bonus gil amount and a treasure.
- V: the days elapsed minus the record's base day count, clamped to 0..9, indexes a day-bonus table that scales JP and gil of every unit by a percentage (about 100 to 120 for JP, 100 to 150 for gil); a negative difference gives no scaling.
- I: the featured unit appears to drive the pose or text shown in the result scene.

## State touched

- Calls: [Errand_LoadRecord](Errand_LoadRecord.md), [Errand_ScoreParty](Errand_ScoreParty.md), [Errand_RollBonusLoot](Errand_RollBonusLoot.md)

## Referenced by

- Called by: [Errand_BoardInput](Errand_BoardInput.md), [Errand_ReportListInput](Errand_ReportListInput.md)
- Reads tables: [ErrandBlob](../tables/ErrandBlob.md)

## Notes

Five blob operands of this function (0x1402D2AEE .. 0x1402D2C22: base, jp/gil tiers, day percentages).

The selector value is 4 in all stock records.

## Open questions

Whether the selector word or the unread evenly spread word 15 is the intended one.
