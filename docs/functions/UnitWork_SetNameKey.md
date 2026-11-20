# UnitWork_SetNameKey

- **Address:** `0x140277CF0`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void UnitWork_SetNameKey(uint8_t *work, const uint8_t *overrideRow)`
- **Callers:** sub_1402760E8 (the end of Unit_BuildFromRecord, with the OverrideEntryData row)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a unit's name key (work dword +508) and name string (work +332).

## Behavior

- V: a unit without a save record (work +2 == 0xFF): when an OverrideEntryData row is given and its dword +0x0C (column chara_name) is non-zero, work +508 = that dword; otherwise, when the name key is still 0xFF, it draws a random generic name key (256 + Rng(256) for work +6 bit 7, 512.. for bit 6, 768.. otherwise) that no save record (+0x22C) and no battle unit (+508, same gender bits) already uses.
- V: a unit with a save record: work +508 = save record dword +0x230 and work +332 = save record string +0xDC (64 bytes).
- V: clears work +475..+484.
- M: every non-zero value of the OverrideEntryData chara_name column is a key of the CharaName table.

## Referenced by

- Called by: [sub_1402760E8](sub_1402760E8.md)

## Open questions

? what work +475..+484 holds.
