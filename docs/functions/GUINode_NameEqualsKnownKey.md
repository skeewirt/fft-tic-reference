# GUINode_NameEqualsKnownKey

- **Address:** `0x1404007FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUINode_NameEqualsKnownKey(NameKey *k)`
- **Callers:** GUIComponent_ApplyStateAnims, GUINode_ApplyStateAtFrame
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests a name key against one global key (string at qword_143CDA2A0+5144, interned id at +5152): id compare when both ids are non-zero, byte-wise string compare otherwise.

## Behavior

- V (live read 2026-10-28): the key at qword_143CDA2A0+5144 is the C string "#Component" (the runtime name of an embedded component root).
- V: when k+8 != 0 and dword (qword_143CDA2A0 + 5152) != 0: returns k+8 == that id. Otherwise byte-wise C string compare of *k with the string pointer at +5144; returns equal.

## State touched

- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The name is ours (IDB: sub_1404007FC). 590 hits per 4 s. I: the key is a reserved state name (the state that is applied specially in ApplyStateAtFrame); the text was not read because it is filled at run time.

## Open questions

? The string at qword_143CDA2A0+5144.
