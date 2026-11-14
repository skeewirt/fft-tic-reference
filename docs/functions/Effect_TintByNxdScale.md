# Effect_TintByNxdScale

- **Address:** `0x1403845C0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 Effect_TintByNxdScale(int64 a1, int64 node)`
- **Callers:** sub_14031B768
- **Callees:** NxdEntry_GetRow, NxdRegistry_Find, NxdTable_GetRowById, atan2f, sub_1400D30D8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Updates one effect node: copies its position and angle into the node record and sets its colour, scaled by the effect number's table row.

## Behavior

- V: when the game is not paused and the frame flag bit 0 of dword_1407B0758 is set, it writes the node position (three values shifted right by 12) into the node record and, for a node with flag 2, an angle computed with atan2f.
- V: the three colour bytes default to 0x80; a node with flag 0x40 takes them from the 160-byte records at qword_1411A3848.
- V: the colour bytes are multiplied by the float at +8 of the RefinedVFXTexture row of word_141D330BC (1.0 when the effect number is 0 or less or the row is missing) and the result is passed on to sub_140387B70.
- V (2026-11-12): the number is loaded sign-extended into edi at 0x1403846FD and tested for 0 or less before the table lookup.

## State touched

- Calls: [NxdEntry_GetRow](NxdEntry_GetRow.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)

## Notes

Name is ours. The float is column Unknown8 of table 202; every stock row holds 1.0.

## Open questions

None recorded.
