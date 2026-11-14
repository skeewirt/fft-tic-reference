# g_BattleCommandBytesB

- **Kind:** global
- **Address:** `0x14184B2C0`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[8]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The second copy of the battle command menu's byte list, built by the same builder for the other command menu (BattleCommand_BuildUnitList), 0xFF-terminated.

## Behavior

- V: written only by sub_14030E010, called from BattleCommand_BuildUnitList (0x1402EB1A6, which first stores 0 here); read by sub_1402E38E4 and BattleCommand_BuildUnitList.
- V: the same list shape as g_BattleCommandBytes (the twin menu code around 0x1402E3.. / 0x1402EB.. mirrors the 0x14022.. / 0x14023.. code).

## Referenced by

- Observed behaviours: [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md)
- Written by: [sub_14030E010](../functions/sub_14030E010.md)

## Notes

Source: IDA reads of 2026-11-12.

## Open questions

? which screen the second menu is.
