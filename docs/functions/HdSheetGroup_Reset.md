# HdSheetGroup_Reset

- **Address:** `0x1403D0E50`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void HdSheetGroup_Reset(void *group)`
- **Callers:** sub_1401E7440
- **Callees:** HdSheetGroup_ReleasePiece, Mem_Free

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Empties one battle HD sheet group: releases its 128 textures, frees its sheet buffer, and frees its pieces and palette entries.

## Behavior

- V: HdSheetGroup_ReleasePiece(group, n, 1) for n = 0..127; the live count (+21136) to 0; the buffer at +2696 freed (Mem_Free) and the pointer cleared; the sheet entry (+2692) to -1; the 16 palette entries to (-1, 0); the 128 pieces' first and used dwords to 0.

## State touched

- Calls: [HdSheetGroup_ReleasePiece](HdSheetGroup_ReleasePiece.md), [Mem_Free](Mem_Free.md)

## Open questions

None recorded.
