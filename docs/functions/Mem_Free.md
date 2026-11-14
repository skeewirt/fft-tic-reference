# Mem_Free

- **Address:** `0x140011804`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `void Mem_Free(void *p, size_t size, Heap *heap)`
- **Callers:** hundreds of call sites; ResourceHandle_FreeData frees a handle's file buffer with (p, 0, null)
- **Callees:** sub_140011620, the heap's free slot

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The engine's free entry: finds the heap that owns a pointer (or uses the one given) and returns the block to it.

## Behavior

- V: the constant 32 (a zero-size allocation) is ignored.
- V: with a heap given whose flag 0x2000 (dword index 92) is clear, or that claims the pointer through its slot 13, that heap frees it; else sub_140011620(p) finds the owner.
- V: calls owner->vtable[9] (offset 72)(owner, p, size).

## Referenced by

- Called by: [ResourceHandle_FreeData](ResourceHandle_FreeData.md), [Unit_InitAbilitiesFromJob](Unit_InitAbilitiesFromJob.md), [sub_140034D7C](sub_140034D7C.md), [sub_1400C30BC](sub_1400C30BC.md), [sub_1402181EC](sub_1402181EC.md)

## Open questions

None recorded.
