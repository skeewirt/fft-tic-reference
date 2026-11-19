# g_BattleActingUnit

- **Kind:** global
- **Address:** `0x14186AF68`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `ptr`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer to the unit record the current battle action is worked out on: the TARGET of the action (the unit hit), although the name says acting; its byte at +0x97 carries the reaction flags and its byte at +0x61 the item/defend phase bits.

## Behavior

- V: sub_14030AFEC, sub_14030B278, sub_140308C98 and sub_1401F9CC4 read the block through this pointer.
- V: Battle_ResolveAction stores it (0x140309A4D) as g_PreviewUnitTable + 512 * (request byte 1); the formula blocks read the target's statuses (+0x61..+0x65), passives (+0x99..+0x9B), element masks (+0x76..+0x79), equipment words (+0x1A..+0x26) and HP / MP through it. The unit of the one acting is g_BattleCasterUnit.

## Referenced by

- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)
- Read by: [Formula_75_ItemRevive](../functions/Formula_75_ItemRevive.md), [sub_1401F9CC4](../functions/sub_1401F9CC4.md), [sub_14030AFEC](../functions/sub_14030AFEC.md), [sub_14030B278](../functions/sub_14030B278.md)

## Open questions

None recorded.
