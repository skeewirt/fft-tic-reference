# WorldMenu_AllocOverlayRecord

- **Address:** `0x1403426F8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 WorldMenu_AllocOverlayRecord(void)`
- **Callers:** Tavern_HasNewEntries, WorldMap_InitLocations, sub_1402EDB48 and others
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Takes the next 36-byte world-menu record from a fixed array, registers it and returns its index.

## Behavior

- V: the array is `dword_140D4C4B0`, count `dword_140D4CA00`; the record pointer is appended to `qword_140D4C0B0` (count `dword_140D4C978`).
- V: clears flag bits 0x418 in dword 0, zeroes the dword at +0x14 and sets bytes +0x20..+0x22 to 0x80.

## Referenced by

- Called by: [EventVarEditor_Open](EventVarEditor_Open.md), [PagedText_Init](PagedText_Init.md), [StatusGlossary_Open](StatusGlossary_Open.md), [WorldMap_InitLocations](WorldMap_InitLocations.md), [sub_14036A294](sub_14036A294.md), [sub_140373BB0](sub_140373BB0.md)

## Notes

Whole body read. Field offsets are the distances of the accessed globals from the array base (for example 0x14, 0x20 and 0x22 from `dword_140D4C4B0`); the mask 0x418 is the complement of the stored 0xFFFFFBE7.

## Open questions

What the records draw.
