# GUISlotVec16_Insert

- **Address:** `0x1403EE77C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int GUISlotVec16_Insert(__int64 unused, GUISlotVec *vec, const __m128i *rec)`
- **Callers:** GUIFontSlots_AcquireImage, sub_1403DA654, sub_1403DA7D4
- **Callees:** allocator vtable +16 / +24, std::vector<void *>::_Xlen

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Inserts a 16-byte record into a std::vector-like container (allocator, begin, end, cap): reuses the first record whose first qword is 0, otherwise appends (growing by 1.5x).

## Behavior

- V: vec = {+0 allocator object, +8 begin, +16 end, +24 cap}. Scans records 0..n-1 for a first qword of 0; the first hit is overwritten with *rec and its index returned.
- V: otherwise, with end == cap the buffer grows: new capacity = cap + cap/2 (at least n + 1, clamped to 0xFFFFFFFF elements; > 0xFFFFFFFF throws via std::vector::_Xlen), allocated through allocator vtable +16, the old elements copied (and the tail shifted when inserting mid-vector, which never happens here), the old buffer freed through vtable +24; the new record is stored at index n. Without growth *end = *rec and end += 16.
- V: returns the new size - 1 (the index of the appended record). The caller adds 1 and the kind bits to make a slot id.

## Referenced by

- Called by: [GUIFontSlots_AcquireImage](GUIFontSlots_AcquireImage.md)

## Notes

The name is ours (IDB: sub_1403EE77C). The first-qword-0 free-record rule is what lets slot ids stay stable after a record's resource is released and cleared.

## Open questions

-
