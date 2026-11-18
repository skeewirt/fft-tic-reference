# NxdDataAbilityReactionVoiceTypeRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ability_reaction_voice_type table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 3 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 3 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 4, 2 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 4, 2 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 4, 2 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |

## Referenced by

- Described by tables: [NxdDataAbilityReactionVoiceType](../tables/NxdDataAbilityReactionVoiceType.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

11 of 12 columns not decoded.
