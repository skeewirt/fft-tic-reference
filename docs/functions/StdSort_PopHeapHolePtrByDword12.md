# StdSort_PopHeapHolePtrByDword12

- **Address:** `0x1403C3EF4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 StdSort_PopHeapHolePtrByDword12(UILayer **heap, __int64 hole, __int64 count, UILayer **value)`
- **Callers:** StdSort_LayersByOrder
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

MSVC's heap 'pop with hole' step for the layer pointer array, key = dword at layer+12: moves the hole at index hole down to a leaf along the larger child, then sifts the value up from there.

## Behavior

- V: while the hole has two children below count it takes the child with the larger key (the right child when its key is not below the left's) and moves it up; a lone left child at the end is taken the same way; then the value is sifted up from the final hole while the parent's key is below the value's key, and stored.

## Referenced by

- Called by: [StdSort_LayersByOrder](StdSort_LayersByOrder.md)

## Notes

Name proposed (IDB: sub_1403C3EF4). Only reached by the heap-sort fallback of the introsort (ideal depth exhausted).

## Open questions

None recorded.
