# GUIRenderer_RunDeferredDraws

- **Address:** `0x1403E6348`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned __int64 __fastcall GUIRenderer_RunDeferredDraws(__int64 r)`
- **Callers:** sub_1403D64F4, sub_1403D7B00 (V)
- **Callees:** virtual slot +104 of each record's object

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

After the frame's UI commands are recorded, calls each deferred draw callback registered in the renderer.

## Behavior

- V: the list is a vector of 80-byte records between *(r+606696) (begin) and *(r+606704) (end); count = (end - begin) / 80 (the 0x6666666666666667 multiply is the divide by 5 of the 16-byte units).
- V: for each record rec: layerNo = *(u32*)(r + 303492 + 592 * *(int*)(rec+76)) (the first dword of that layer's 592-byte record, the layer index/number written by GUIRenderer_ResetFrame); arg6 = layerNo - 1 if layerNo != 0 else 0.
- V: calls rec->obj->vtable[+104]( obj = *rec, rec+16 (qword), rec+8 (qword), rec+32 (pointer to 24 bytes), *(u32*)(rec+56), arg6, rec+24 (qword), rec+60 (pointer) ) for each.
- V: no clearing happens here; the list is cleared by GUIRenderer_ResetFrame (r+606704 = r+606696).

## Notes

Record layout I-ish from the use: +0 object, +8 / +16 / +24 qword args, +32 inline block, +56 dword, +60 inline block, +76 layer record index.

## Open questions

? who pushes the records (find the writer of r+606696..) and which objects use slot +104.
