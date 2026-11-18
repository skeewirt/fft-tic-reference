# ResultLabel_ShowNext

- **Address:** `0x140266A68`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 ResultLabel_ShowNext(__int64 task)`
- **Callers:** ResultLabel_QueueFromUnit, sub_140268880
- **Callees:** BattleLabel_ShowStatusSignal, BattleLabel_ShowReactionSignal, sub_14014C224

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows the next pending label over a unit: a number (HP / MP / stat change), a fixed text, or the next queued status label.

## Behavior

- V: takes the lowest set bit of the low 16 bits of task +472 first: it copies the result words of the unit (+452..+458, the HP / MP damage and recovery words) and the stat-change bytes (+466..+471, & 0x7F) into word_143740200.., stores the value in task +836 and a label kind in +834, and clears the bit.
- V: then the bits 16 .. 24 of task +472 one at a time, tested and cleared with bit instructions (each sets a fixed kind in +834).
- V: then the status queue: while the count task +469 is non-zero it decrements it, takes the entry task +476[count] (so the queue is shown from its last entry), stores entry & 0x7F as the BattleSignal id and kind 96, or 112 when bit 0x80 is set.
- V: kinds 96 / 112 call sub_14014B87C(object, slot, signal id, 0 / 1): the status label; other kinds call sub_14014BFFC or sub_14014C224 with fixed BattleSignal ids (for example 49 Miss!, 64 Evaded!, 65 Chicken, 66 Toad).
- V: the slot is the unit byte +1 (task +328 points at the unit); the drawing object is the battle screen agent reached from qword_143CD9DA8.

## State touched

- Calls: [BattleLabel_ShowStatusSignal](BattleLabel_ShowStatusSignal.md), [BattleLabel_ShowReactionSignal](BattleLabel_ShowReactionSignal.md)

## Referenced by

- Appears in flows: [StatusLabelOverAHitUnit](../flows/StatusLabelOverAHitUnit.md)
- Called by: [ResultLabel_QueueFromUnit](ResultLabel_QueueFromUnit.md)
- Observed behaviours: [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md)

## Notes

Name is ours. A 41 KB function; only the label selection is described here.

## Open questions

? the full list of kinds in +834 and the label each one draws.
