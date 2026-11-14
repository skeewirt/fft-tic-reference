# GUIFactory_FreeSlotGroup

- **Address:** `0x1403FECD0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIFactory_FreeSlotGroup(GUIFactory *pool, GUIFontSlotGroup *g)`
- **Callers:** GUIWidget_ReleaseSlotGroup, sub_1403F9188 (widget teardown, the group vector loop)
- **Callees:** sub_1403F3D28, sub_140011804

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a slot group to the pool: clears its occupancy bit, runs the group's destructor and, every time the live count crosses 32 modulo 64, drops empty pages.

## Behavior

- V: pool = qword_143CDA280: page vector +176..+184, live count +204, cursor +200. Pages are scanned from the last to the first for the one with page <= g < page + 7168.
- V: on the hit: mask bit (g - page) / 112 is cleared, count -= 1, sub_1403F3D28(g) runs (destructor: frees the vectors at +56 and +24 through their allocators and releases the name's interned id with sub_1403D8D1C).
- V: when (count & 0x3F) == 32 the page vector is compacted: every page whose mask is 0 is freed (sub_140011804(page, 0, allocator)) and removed from the vector; the cursor +200 = last page index.
- V: a pointer that is in no page does nothing.

## Referenced by

- Called by: [GUIWidget_ReleaseSlotGroup](GUIWidget_ReleaseSlotGroup.md)

## Notes

The name is ours (IDB: sub_1403FECD0); 'factory' is I (the same global is passed to the sibling free functions sub_1403FF800 / FF4F8 / FEB5C / FEE44 that free components, nodes and other widget vectors in sub_1403F9188).

## Open questions

? why the compaction fires on 32 mod 64 (an amortisation heuristic?).
