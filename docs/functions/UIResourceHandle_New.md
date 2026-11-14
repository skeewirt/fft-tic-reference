# UIResourceHandle_New

- **Address:** `0x1403D9A00`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `UIResourceHandle *UIResourceHandle_New(__int64 a1, __int64 a2, __int64 a3, __int64 a4)`
- **Callers:** vtable of the resource factory (0x143D41584 pointer table); sub_1403D9A54
- **Callees:** sub_140011750, sub_140095DA0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Factory: allocates a 104-byte UIResourceHandle through the allocator object at qword_143CDAA80 (+8) and constructs it.

## Behavior

- V: allocator = *(qword_143CDAA80 + 8) or 0; sub_140011750(104, allocator, 8, ...); null returns 0; sub_140095DA0(obj) base constructor, byte +96 = 0, vtable = UIResourceHandle (0x140721BF0).

## Notes

The name is ours (IDB: sub_1403D9A00).

## Open questions

? the interface that registers this factory (a2..a4 unused).
