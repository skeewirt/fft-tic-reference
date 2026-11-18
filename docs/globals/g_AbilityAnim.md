# g_AbilityAnim

- **Kind:** global
- **Address:** `0x140672DA0`
- **Type:** `battle action data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

454 x 3 bytes (ability ids 0..453, .rdata): charge / cast effect type, motion, battle text; indexed by the scene object's effect word (+0x142, +0x18C). 8 readers (BattleAnim_SelectMotion, BattleAnim_SetChargeMotion, BattleAct_SetupEffect, sub_140206C14, sub_140206CE8, sub_1402059AC, sub_14020CC50, sub_140210AF0), none bounded

## Referenced by

- Described by tables: [AbilityAnim](../tables/AbilityAnim.md)
- Read by: [sub_1402059AC](../functions/sub_1402059AC.md), [sub_140206CE8](../functions/sub_140206CE8.md), [sub_14020CC50](../functions/sub_14020CC50.md)

## Open questions

None recorded.
