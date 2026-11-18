# NxdDataUIEquipAbilitySlotRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_equip_ability_slot table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set. Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Slot group (0..8). Observed in the stock rows: 0 to 8, 9 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Slot order (0..10). Observed in the stock rows: 0 to 10, 11 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Icon id (24..27 or 0). Observed in the stock rows: 0 to 27, 5 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIEquipAbilitySlot](../tables/NxdDataUIEquipAbilitySlot.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

3 of 4 columns not decoded.
