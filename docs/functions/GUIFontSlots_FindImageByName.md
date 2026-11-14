# GUIFontSlots_FindImageByName

- **Address:** `0x1403DB390`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontSlots_FindImageByName(__int64 slots, const char *name)`
- **Callers:** sub_1403DA654, GUIFontSlots_AcquireImage
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Linear search of the image records for one whose name equals name; returns an image id (1-based index | 0x03000000) or 0.

## Behavior

- V: image vector: begin slots+112, end slots+120, 16-byte entries (count = (end-begin)>>4); empty returns 0.
- V: an entry is considered only if its word at +8 != 0 and its qword at +0 (object pointer) != 0.
- V: name pointer = the qword at obj + 24 if non-zero, else the global empty string `Str`; compared byte by byte (case-sensitive strcmp) with name.
- V: on match returns (index + 1) | 0x3000000; no match returns 0.
- V: callers sub_1403DA654 (0x1403DA727), GUIFontSlots_AcquireImage (0x1403DB2E5).

## Notes

Sibling of GUIFontSlots_FindPartByName (kind 3 images vs parts).

## Open questions

? what the word at entry+8 means (used as an 'in use' flag; I).
