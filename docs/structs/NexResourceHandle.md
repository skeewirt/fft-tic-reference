# NexResourceHandle

- **Kind:** structure
- **Area:** [Resource](../areas/resource.md)
- **Size:** 168 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The resource handle an nxd file is loaded through (NxdTable_CreateHandle; root.nxl uses the same layout with the NxlResourceHandle vtable): the common resource handle plus two callback pairs.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="vtable"></a>`0x0` | vtable | `void **` | V | 0x140721600 (NexResourceHandle); slot 8 NxdHandle_OnLoaded, slot 13 NxdHandle_OnReady, slot 14 NxdHandle_GetHeap. |  |  |
| <a id="refs"></a>`0xC` | refs | `int32` | V | Reference count (ResourceHandle_Init sets 1). |  |  |
| <a id="path"></a>`0x18` | path | `char *` | V | The requested path (`<dir>/<name>.nxd`). |  |  |
| <a id="resolved"></a>`0x28` | resolved | `StringObject *` | V | The path the reader resolved (text at +8, capacity at +32), freed by ResourceHandle_FinishLoad after the callbacks. |  |  |
| <a id="reader"></a>`0x30` | reader | `Reader *` | V | The file reader; deleted by ResourceHandle_FinishLoad. |  |  |
| <a id="data"></a>`0x38` | data | `uint8 *` | V | The whole file, read by ResourceHandle_ReadData from the heap of slot 14; freed by ResourceHandle_FreeData with Mem_Free unless flag 0x100. | [NxdTable_BindRows](../functions/NxdTable_BindRows.md), [NxdTable_GetEntryByKeyIndex](../functions/NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetEntryByKeysIndex3](../functions/NxdTable_GetEntryByKeysIndex3.md) | [ResourceHandle_ReadData](../functions/ResourceHandle_ReadData.md) |
| <a id="size"></a>`0x40` | size | `uint64` | V | The file size. |  |  |
| <a id="status"></a>`0x50` | status | `int32` | V | 1 loaded, 2 failed (ResourceHandle_LoadNow); NxdTable_OnReady reads it. | [NxdTable_OnReady](../functions/NxdTable_OnReady.md) |  |
| <a id="state"></a>`0x54` | state | `int32` | V | Load state (0 new, 2 opening, 3 read, 1 done). |  |  |
| <a id="flags"></a>`0x5C` | flags | `uint32` | V | 0x2008 for nxd handles; 0x100 = the buffer is not the handle's (not freed); 0x800 = open before read; 8 = localised. | [ResourceHandle_FreeData](../functions/ResourceHandle_FreeData.md) |  |
| <a id="loaded_invoker"></a>`0x60` | loaded_invoker | `code *` | V | sub_1400674E8. |  |  |
| <a id="loaded_context"></a>`0x68` | loaded_context | `NxdTable *` | V | The table object. | [NxdHandle_OnLoaded](../functions/NxdHandle_OnLoaded.md) |  |
| <a id="loaded_callback"></a>`0x70` | loaded_callback | `code *` | V | NxdTable_BindRows. | [NxdHandle_OnLoaded](../functions/NxdHandle_OnLoaded.md) | [NxdTable_CreateHandle](../functions/NxdTable_CreateHandle.md) |
| <a id="ready_invoker"></a>`0x80` | ready_invoker | `code *` | V | sub_1400674E8. |  |  |
| <a id="ready_context"></a>`0x88` | ready_context | `NxdTable *` | V | The table object. |  |  |
| <a id="ready_callback"></a>`0x90` | ready_callback | `code *` | V | NxdTable_OnReady. |  | [NxdTable_CreateHandle](../functions/NxdTable_CreateHandle.md) |
| <a id="heap_select"></a>`0xA0` | heap_select | `uint8` | V | 0: NxdHandle_GetHeap returns the default heap. |  |  |

## Notes

Offsets 0x0..0x5F are the common resource handle (ResourceHandle_Init).

## Open questions

? +0x10 (a size or pointer the reader fills), +0x48 (path hash, I).
