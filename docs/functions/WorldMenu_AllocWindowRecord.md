# WorldMenu_AllocWindowRecord

- **Address:** `0x14034275C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 WorldMenu_AllocWindowRecord(void)`
- **Callers:** Errand_SelectBoardEntry, Tavern_HasNewEntries, sub_1402EDB48, sub_140318860, sub_14036A294 and others
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Takes the next 56-byte world-menu window record, registers it and returns its index.

## Behavior

- V: the array is `dword_140D4B9B0`, count `dword_140D4C974`; the pointer is appended to `qword_140D4C0B0`.
- V: clears flag bits 0x418, zeroes dwords at +0x10 and +0x14, sets bytes +0x30..+0x32 to 0x80.

## Referenced by

- Called by: [EventVarEditor_Open](EventVarEditor_Open.md), [PagedText_Init](PagedText_Init.md)

## Notes

Whole body read. Field offsets are the distances of the accessed globals from `dword_140D4B9B0`; the mask 0x418 is the complement of the stored 0xFFFFFBE7.

## Open questions

None.
