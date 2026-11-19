# NxdDataOverrideAbilityActionDataRow

- **Kind:** structure
- **Area:** [Ability data](../areas/ability-data.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.override_ability_action_data table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="flags12"></a>`0x4` | flags12 | `int16[] {int32 offset; uint32 count}` | V | Read in the code: A list whose first two values replace action record bytes +3 and +4. Observed in the stock rows: 1 distinct values. |
| <a id="flags34"></a>`0xC` | flags34 | `int16[] {int32 offset; uint32 count}` | V | Read in the code: A list whose first two values replace action record bytes +5 and +6. Observed in the stock rows: 3 distinct values. |
| <a id="range"></a>`0x14` | range | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: range. Observed in the stock rows: -1 in every row. |
| <a id="effect_area"></a>`0x16` | effect_area | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: effect area. Observed in the stock rows: -1 in every row. |
| <a id="vertical"></a>`0x18` | vertical | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: vertical reach. Observed in the stock rows: -1 in every row. |
| <a id="element"></a>`0x1A` | element | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: element. Observed in the stock rows: -1 in every row. |
| <a id="formula"></a>`0x1C` | formula | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: formula. Observed in the stock rows: -1 in every row. |
| <a id="x"></a>`0x1E` | x | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: X. Observed in the stock rows: -1 in every row. |
| <a id="y"></a>`0x20` | y | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: Y. Observed in the stock rows: -1 in every row. |
| <a id="inflict_status"></a>`0x22` | inflict_status | `int16` | V | Read in the code: When 0 or more it replaces this byte of the ability's action record: the row of the status list it applies. Observed in the stock rows: -1 in every row. |
| <a id="ct"></a>`0x24` | ct | `int16` | V | override of record byte +12 (charge time); value >= 0 replaces it. Observed in the stock rows: -1 to 10, 8 distinct values. |
| <a id="mp"></a>`0x26` | mp | `int16` | V | override of record byte +13 (MP cost); value >= 0 replaces it. Observed in the stock rows: -1 to 50, 4 distinct values. |

## Referenced by

- Described by tables: [NxdDataOverrideAbilityActionData](../tables/NxdDataOverrideAbilityActionData.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 13 columns not decoded.
