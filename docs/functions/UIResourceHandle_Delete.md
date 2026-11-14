# UIResourceHandle_Delete

- **Address:** `0x1403D99C0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `UIResourceHandle *UIResourceHandle_Delete(UIResourceHandle *h, char flags)`
- **Callers:** the vtable at 0x140721BF0 (slot 0)
- **Callees:** sub_140095E5C, sub_14041FB00 (free)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scalar deleting destructor (vtable method) of the UIResourceHandle class: resets the vtable, runs the base destructor and frees the 104-byte object when bit 0 of flags is set.

## Behavior

- V: *h = vftable_faith::UISystem::UIResourceHandle (0x140721BF0); sub_140095E5C() (base destructor); if (flags & 1) sub_14041FB00(h, 104). Returns h.

## Notes

The name is ours (IDB: sub_1403D99C0). Object size 104 is from the matching constructor sub_1403D9A00.

## Open questions

? the base class of UIResourceHandle (sub_140095E5C / sub_140095DA0).
