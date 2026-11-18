# TurnPanel_SetTag

- **Address:** `0x140215540`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void TurnPanel_SetTag(int tag, int listIndex, int unit, uint8 entryFlags, unsigned int entryAbility)`
- **Callers:** TurnPanel_Refresh (10 sites), TurnPanel_RefreshUnit
- **Callees:** sub_14022AA88, Str_Format, AbilityTable_GetRow, sub_1401EB5D0, sub_1400E5814

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one tag of the turn-order panel from a list entry: the unit's portrait data and, for a pending action, the ability name.

## Behavior

- V: the name: when entryFlags has 0x40 and not 0x20, ability = entryAbility + (entryFlags & 0x80 ? 256 : 0); ids 394..405 get no name; otherwise AbilityTable_GetRow(ability) gives the text (formatted into byte_143CDA780).
- V: the rest comes from the unit's work record (shape through sub_14022AA88, HP / MP words +48 / +50, status bytes +494, +504) and goes to sub_1400E5814.

## State touched

- Calls: [sub_14022AA88](sub_14022AA88.md), [Str_Format](Str_Format.md), [AbilityTable_GetRow](AbilityTable_GetRow.md)
- Reads: [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

## Referenced by

- Called by: [Battle_TimelineRefresh](Battle_TimelineRefresh.md)
- Observed behaviours: [BattleFaceIsThePoolSpriteByte](../behaviors/BattleFaceIsThePoolSpriteByte.md), [FaceLookupInlineCopiesDisagreeAboveCode159](../behaviors/FaceLookupInlineCopiesDisagreeAboveCode159.md), [FaceNumberCapsClipRawCodesToo](../behaviors/FaceNumberCapsClipRawCodesToo.md), [TurnOrderEntryKeepsNineBitsOfTheAbility](../behaviors/TurnOrderEntryKeepsNineBitsOfTheAbility.md)
- Reads tables: [SceneSpriteToFace](../tables/SceneSpriteToFace.md)

## Notes

One of two readers of the entry's ability (the other: TurnPanel_SetUnitPanel). A census of this decode (the byte plus 256 chosen by the flag) over the whole exe finds three; the third, in TurnList_Build, only tests the result for != 0.

2026-11-08: the portrait face is an inline copy of SpriteId_ToShape (the code bound at 0x14021569D, the table read at 0x1402156A5, the cap register r8d = 0xCD set at 0x14021568B and compared at 0x140215786). For an unset code (-1) the value capped is the per-pool value from sub_14022AA88, not a table answer. Its list for codes above 0x9F differs from SpriteId_ToShape's at code 205 (no face here; run under unicorn). The bound is 0x9F and the cap 0xCD.

## Open questions

None recorded.
