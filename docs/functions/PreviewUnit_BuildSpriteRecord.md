# PreviewUnit_BuildSpriteRecord

- **Address:** `0x1400FB038`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `int PreviewUnit_BuildSpriteRecord(void *out, int jobId, int previewIndex, int a4, int a5, int palette, char allowAltShape, char setPalette, char a9)`
- **Callers:** Unit_BuildPreviewSpriteRecord, sub_14013C238, sub_14013FAB0, sub_140142884, sub_1401442FC, sub_14014A970, sub_1402C6514, sub_1402C72B8, sub_1402D0080
- **Callees:** PreviewUnit_ResolveShape, UITable_GetRowByKey, sub_1401E39BC, sub_1400FAFB0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a sprite record from preview-table entry `previewIndex` (<= 0x14), resolving shape/palette and applying the entry's flag-driven overrides.

## Behavior

- V: initializes the record and returns it zeroed with job -1 when previewIndex > 0x14; otherwise writes jobId to +0.
- V: PreviewUnit_ResolveShape(previewIndex, &shape, &palette); the shape goes to +4 and +16, the palette to +8.
- V: with allowAltShape, entry+99 bit 4 selects shape -100 (0x9C) and bit 2 selects shape -99 (0x9D).
- V: with setPalette, a row for entry+0 in table 0x112 (sub_1401E39BC) overrides the palette: +10 gets that byte and +20 = 0; otherwise +8 keeps the resolved palette.
- V: +24 gets 2 when the palette argument is 4, else the argument; a8 -> +20 = sub_1400FAFB0(entry+97); +12 = 0; +28 = -1.

## State touched

- Calls: [PreviewUnit_ResolveShape](PreviewUnit_ResolveShape.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Called by: [Unit_BuildPreviewSpriteRecord](Unit_BuildPreviewSpriteRecord.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

This is the generic preview-sprite builder behind the job-change/unit-preview screens; the tree path reaches it through Unit_BuildPreviewSpriteRecord. Fields: +0 job id, +4/+16 shape, +8 palette, +10 alternate value, +12 flags (filled later by SpriteRecord_SetPaletteBits), +20 override flag, +24 palette id, +28 -1.

## Open questions

Consumers of the +10 alternate value and the +20 override flag (CharaRender path) were not traced.
