# UITexturePath_FromRow

- **Address:** `0x1400FCA68`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `bool UITexturePath_FromRow(unsigned row, char *out, int size)`
- **Callers:** FaceTexture_FormatName and others
- **Callees:** UITable_GetRowByKey, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a UITextureParts path (that scheme followed by the row's text) from one row of UI table 0x8F.

## Behavior

- V: UITable_GetRowByKey(0x8F, row); a missing row returns false and leaves out unchanged.
- V: otherwise Str_Format(out, size, format, text): the UITextureParts scheme and the text at the row's offset in its dword +4.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [Str_Format](Str_Format.md)

## Referenced by

- Called by: [FaceTexture_FormatName](FaceTexture_FormatName.md), [WorldMapBaseList_DrawRow](WorldMapBaseList_DrawRow.md)

## Notes

The name is ours (IDB: sub_1400FCA68).

## Open questions

None recorded.
