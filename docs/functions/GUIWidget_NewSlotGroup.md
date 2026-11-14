# GUIWidget_NewSlotGroup

- **Address:** `0x1403FB960`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIFontSlotGroup *GUIWidget_NewSlotGroup(GUIWidget *w, const char *name)`
- **Callers:** GUIWidget_EnsureSlotGroup, sub_1403F495C (widget resource-section loader)
- **Callees:** sub_140011750, sub_14006635C, sub_1403F3CAC, sub_1403D8870, sub_140031D7C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates a texture slot group from the global group pool, names it (default 'None'), registers the widget as one of its owners and appends it to the widget's group vector.

## Behavior

- V: pool = qword_143CDA280 (the global factory): page vector at +176..+184 (16-byte {page pointer, 64-bit occupancy mask}), cursor dword +200, live count dword +204. A page is 7168 bytes = 64 groups of 112 bytes (sub_140011750(7168, allocator, 16)).
- V: when the live count equals pages * 64 a new page is allocated and appended (cursor = its index); otherwise the pages are scanned starting at the cursor and going backwards (index = (n + cursor - i) mod n) for a page whose mask word is not -1; none = return 0 (0xFFFFFFFF index).
- V: the lowest clear bit of that page's mask is set, the live count is incremented and the group at page + 112 * bit is constructed with sub_1403F3CAC (name {Str, 0}, two allocator-backed empty vectors at +24 and +56, ids +80 = 0, flags +88 / +89 / +90 = 0). A null construct result returns 0.
- V: the name is set with sub_1403D8870(group, name ? name : "None") (interns it in the global name table).
- V: the widget's object id (w+8) is stored in the first free slot of the four-dword owner array at group+96..+108 unless it is already present (an existing equal id stops the search).
- V: the group pointer is appended to the widget's group vector (w+224..+232, capacity +240; sub_140031D7C grows it) and returned.

## Referenced by

- Called by: [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md)

## Notes

The name is ours (IDB: sub_1403FB960). The widget vector at +224 is the one GUIWidget_FindResourceByName searches and GUIWidget_ReleaseSlotGroup / sub_1403F9188 free. Calling the global at qword_143CDA280 'the factory' follows the vtable name GUIFactory next to the widget vtable (I).

## Open questions

? a 0xFFFFFFFF page index (all pages full but count != pages * 64) is treated as failure; whether that case can occur was not examined.
