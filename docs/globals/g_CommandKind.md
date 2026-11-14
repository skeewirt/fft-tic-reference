# g_CommandKind

- **Kind:** global
- **Address:** `0x14067E010`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[256]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Command id to command kind, one byte per row: 256 stock rows indexed by the command (skillset) byte. Index 6 is 1 (Item), index 20 is 2 (Throw), and the battle range and action builders switch on the value.

## Behavior

- V: read by the range, preview and request builders at the command byte of the action block.
- V: 36 code sites read the table (11 rip-relative, 25 image-base-relative reads; the row is the skillset id); a Charge list is kind 10, as Archer's Aim, set 8.
- V (read from the table, 2026-11-10): the ids 0xB0..0xDF all give kind 6 (monster skillsets) and 0xE0..0xFF give 0; 0x11 gives 4 (charge), 0x12 gives 9 (jump), 0x13 gives 7 (iaido), 0x14 gives 2 (throw), 0x15 gives 3 (arithmeticks); kind 0 is a plain action list.

## Referenced by

- Described by tables: [CommandKind](../tables/CommandKind.md)
- Observed behaviours: [AbilityAboveStockBoundaryHasNoMpCheckOrCost](../behaviors/AbilityAboveStockBoundaryHasNoMpCheckOrCost.md), [BattleCommandMenuCarriesSetsAsBytes](../behaviors/BattleCommandMenuCarriesSetsAsBytes.md)
- Read by: [sub_140217630](../functions/sub_140217630.md), [sub_1402828E4](../functions/sub_1402828E4.md), [sub_14030B1A0](../functions/sub_14030B1A0.md), [sub_14030E010](../functions/sub_14030E010.md), [sub_140316D24](../functions/sub_140316D24.md)

## Open questions

None recorded.
