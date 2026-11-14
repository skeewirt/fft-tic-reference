# GUIFontSlots_FindPartByName

- **Address:** `0x1403DAB60`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int GUIFontSlots_FindPartByName(GUIFontSlots *slots, const char *name)`
- **Callers:** GUIFontSlots_AcquireTexturePart, sub_1403DA654
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Linear search of the kind-2 (texture part) records for a live record whose resource name equals name; returns its id or 0.

## Behavior

- V: iterates the 32-byte records at slots+80 / +88. A record counts when u16 rec+24 != 0 and the qword rec+0 is non-null; its name is the C string at *(rec+0)+24, or the shared empty string Str when that pointer is 0.
- V: byte-wise strcmp with name; the first equal record returns (index + 1) | 0x2000000. No match returns 0.

## Notes

The name is ours (IDB: sub_1403DAB60). Case-sensitive compare.

## Open questions

-
