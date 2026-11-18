# ClassicSaveListLanguage0Record

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)
- **Size:** 176 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the ClassicSaveListLanguage0 table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="template"></a>`0x0` | template | `bytes[168]` | ? | window / list template of the classic save list (layout words; first word 0x180, a 0x54 at +0xA) |
| <a id="cursor"></a>`0xA8` | cursor | `int16` | V | list cursor row, written when a slot is chosen (word_1407DC798) |

## Referenced by

- Described by tables: [ClassicSaveListLanguage0](../tables/ClassicSaveListLanguage0.md)

## Open questions

None recorded.
