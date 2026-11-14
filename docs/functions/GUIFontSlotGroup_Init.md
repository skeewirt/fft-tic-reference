# GUIFontSlotGroup_Init

- **Address:** `0x1403F3CAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontSlotGroup_Init(__int64 group)`
- **Callers:** sub_1403E5B84, GUIWidget_NewSlotGroup
- **Callees:** sub_1403DC1E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of a per-widget group that owns slot references: sets two empty vectors, a name key and a trailing slot record.

## Behavior

- V: +0 = global `Str` (vtable-ish / empty-string pointer), +8 dword = 0 (name key; released by Destroy via UIName_ReleaseKey).
- V: vector A: allocator at +16 (= qword_143CDAA80[+32] or 0), begin +24, end +32, cap +40 all 0 (Destroy frees with a size masked to 16-byte multiples, so 16-byte elements).
- V: vector B: allocator at +48, begin +56, end +64, cap +72 all 0 (4-byte elements: size masked to 4).
- V: sub_1403DC1E8(group + 96) initialises an embedded member; then +80 qword, +88 word and +90 byte are stored from an uninitialised register (decompiler artefact, I: they are zeroed by the caller convention).
- V: callers sub_1403E5B84 (0x1403E5BFE), GUIWidget_NewSlotGroup (0x1403FBAA4).

## State touched

- Calls: [sub_1403DC1E8](sub_1403DC1E8.md)

## Notes

Destroy sheet gives the element sizes. The +80..+90 stores should be re-read in the disassembly before being trusted.

## Open questions

? what the embedded object at +96 is. ? values stored at +80/+88/+90 (r9 / r10 leak in the decompile).
