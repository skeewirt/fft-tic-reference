# Mem_Alloc

- **Address:** `0x140011750`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `void *Mem_Alloc(size_t size, Heap *heap, size_t align)`
- **Callers:** hundreds of call sites (every engine allocation), among them NxdTable_CreateHandle and NxdTable_BindRows
- **Callees:** the heap's allocate slot

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The engine's allocation entry: asks the heap object for `size` bytes with at least 8-byte alignment.

## Behavior

- V: size 0 returns the constant 32 (no allocation).
- V: alignment = max(align, 8); calls heap->vtable[6] (offset 48)(heap, size, alignment, &zero).

## Referenced by

- Appears in flows: [ScreenAddonCreation](../flows/ScreenAddonCreation.md)
- Called by: [BUi_BattleMenuWindowsCtor](BUi_BattleMenuWindowsCtor.md), [Boot_SetState](Boot_SetState.md), [Boot_Update](Boot_Update.md), [HdLayer_BuildTextures](HdLayer_BuildTextures.md), [InputModule_Init](InputModule_Init.md), [MovieSound_LoadBank](MovieSound_LoadBank.md), [NxdRegistry_CreateRootHandle](NxdRegistry_CreateRootHandle.md), [NxdTable_CreateHandle](NxdTable_CreateHandle.md), [SaveLoadList_BuildAutoEntries](SaveLoadList_BuildAutoEntries.md), [SaveLoadList_BuildEntries](SaveLoadList_BuildEntries.md), [Sound_PlayNovelSe](Sound_PlayNovelSe.md), [TitleScene_Start](TitleScene_Start.md), [TitleScene_Update](TitleScene_Update.md), [UIAddonFFTOEvent_Ctor](UIAddonFFTOEvent_Ctor.md), [UIAgentManager_CreateAgents](UIAgentManager_CreateAgents.md), [WorldMapAgent_CreateAddons](WorldMapAgent_CreateAddons.md), [sub_140034D7C](sub_140034D7C.md), [sub_1400C30BC](sub_1400C30BC.md), [sub_14018373C](sub_14018373C.md)

## Notes

A buffer allocated with it from the handle's own heap is found by the engine's later Mem_Free of that buffer.

## Open questions

None recorded.
