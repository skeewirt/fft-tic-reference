# AbilityTable_GetRow

- **Address:** `0x1400F8474`
- **Area:** [Ability data](../areas/ability-data.md)
- **Prototype:** `char *AbilityTable_GetRow(unsigned int abilityId)`
- **Callers:** Ability menus and UI code that needs an ability's name, icon or description.
- **Callees:** sub_1403D325C, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the Ability NXD row for an ability id, or null when the table or row is missing. The table is loaded lazily and cached.

## Behavior

- V: lazily loads NXD table 39 through `sub_1403D325C` and caches it in `qword_143CDA2D0`; returns null if the table manager or the load fails.
- V: looks up the row by ability id with `sub_1403D3AE8`; returns null when the row is missing.
- V: a negative row key resolves to the static empty row `unk_1406F5ED0`.
- V: otherwise resolves the row with `sub_1403D2FD8`.
- I: table 39 is the Ability table. The old-build accessor is a different function in this build.

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [EquipDetail_BuildCategoryLines](EquipDetail_BuildCategoryLines.md), [TurnPanel_SetTag](TurnPanel_SetTag.md), [TurnPanel_SetUnitPanel](TurnPanel_SetUnitPanel.md), [UIGadgetFFTOJobDetailWindow_SetJob](UIGadgetFFTOJobDetailWindow_SetJob.md), [Unit_ReactionVoiceAllowed](Unit_ReactionVoiceAllowed.md), [sub_14010824C](sub_14010824C.md), [sub_140153CA0](sub_140153CA0.md), [sub_1401560D0](sub_1401560D0.md)
- Reads tables: [Ability](../tables/Ability.md)

## Notes

The row layout below is ported from the earlier Ability layout research and has not been revalidated byte by byte against this build.

| Offset | Field | Type |
|---|---|---|
| `0x00` | unknown00 | int |
| `0x04` | icon | int |
| `0x08` | Name | string (relative) |
| `0x0C` | Description | string (relative, -4 base) |
| `0x10` | UnusedString10 | string (relative, -8 base) |
| `0x14` | UnusedShort14 | short |
| `0x16`-`0x19` | NounFormByte1-4 | byte x 4 |
| `0x1A` | Padding | short |
| `0x1C` | Comment | string |
| `0x20` | ui_text | int |
| `0x24` | battle_voices | int[] |
| `0x2C` | ui_text_2 | int |
| `0x30` | SlotColorTint | int |
| `0x34` | PassiveSortOrder | int |
| `0x38` | unknown38 | int |
| `0x3C` | AbilityAnimType | int |
| `0x40` | jp_cost_low, jp_cost_high | uint16 |
| `0x42` | unknown42 | byte |
| `0x43` | random_status | byte |

## Open questions

Revalidate the row layout against the current build.
