# Unit_BuildPreviewSpriteRecord

- **Address:** `0x1402C1D40`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `int Unit_BuildPreviewSpriteRecord(SpriteRecord *out, int partyIndex, unsigned char slot, char a4, char a5, char a6, char a7)`
- **Callers:** JobTree_FillJobRecords (slot 0), sub_1402C1EA8, sub_1402C2778, sub_1402C2BFC, sub_140368B4C
- **Callees:** PreviewUnit_BuildRecord, PreviewUnit_BuildSpriteRecord, PreviewUnit_ResolveShape, sub_1400FAFB0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the sprite record for a party unit's preview. In normal play it just forwards to PreviewUnit_BuildRecord with slotArg = 2 * slot + 4.

## Behavior

- V: clears the record (job -1); when both debug globals unk_142FF9F30 and qword_142FF9F34 are zero it returns PreviewUnit_BuildRecord(out, partyIndex, unit preview index (unit +44), 0, ..., 2 * slot + 4, a4).
- V: otherwise (debug path) a6 selects overrides from the preview entry flags (4, 52 or 72 as the slot argument) and it tail-calls PreviewUnit_BuildSpriteRecord.

## State touched

- Calls: [PreviewUnit_BuildRecord](PreviewUnit_BuildRecord.md), [PreviewUnit_BuildSpriteRecord](PreviewUnit_BuildSpriteRecord.md), [PreviewUnit_ResolveShape](PreviewUnit_ResolveShape.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [JobScreen_UpdateState](JobScreen_UpdateState.md)

## Open questions

None recorded.
