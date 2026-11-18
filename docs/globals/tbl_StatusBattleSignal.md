# tbl_StatusBattleSignal

- **Kind:** global
- **Address:** `0x140672CC0`
- **Type:** `battle ui`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint8[40]: the BattleSignal row of each status id (index = id), 0 = no label: ids 2 KO, 21 Chicken and 22 Toad map to 0 (KO's row is 0; Chicken and Toad have labels of their own, 65 / 66); 24 Poison -> 13. Read only by ResultLabel_QueueFromUnit

## Referenced by

- Observed behaviours: [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md)

## Open questions

None recorded.
