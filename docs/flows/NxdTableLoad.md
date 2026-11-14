# NxdTableLoad

- **Kind:** flow
- **Area:** [Data access](../areas/data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How one nxd table goes from a root.nxl line to rows a reader can look up.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [NxdRegistry_LoadRootNxl](../functions/NxdRegistry_LoadRootNxl.md) | V | Per root.nxl line: a table object (id, state 1), the file `<dir>/<name>.nxd` opened with NxdTable_CreateHandle as the handle factory. |
| <a id="2"></a>2 | [NxdTable_CreateHandle](../functions/NxdTable_CreateHandle.md) | V | The NexResourceHandle with NxdTable_BindRows as the load callback and NxdTable_OnReady as the ready callback, both with the table as context. |
| <a id="3"></a>3 | [ResourceHandle_ReadData](../functions/ResourceHandle_ReadData.md) | V | The reader resolves the path (the language variant, I) and reads the whole file into the handle's buffer from the heap of NxdHandle_GetHeap. |
| <a id="4"></a>4 | [NxdHandle_OnLoaded](../functions/NxdHandle_OnLoaded.md) | V | Slot 8: the load callback runs. |
| <a id="5"></a>5 | [NxdTable_BindRows](../functions/NxdTable_BindRows.md) | V | Reads the header (count, contiguous-keys flag, first key) and points the table's entries into the buffer. |
| <a id="6"></a>6 | [NxdTable_OnReady](../functions/NxdTable_OnReady.md) | V | Slot 13: the table becomes usable (state 2 or 3). |
| <a id="7"></a>7 | [ResourceHandle_FinishLoad](../functions/ResourceHandle_FinishLoad.md) | V | Reader and resolved path released; the buffer stays with the handle until the handle is released (ResourceHandle_FreeData). |
| <a id="8"></a>8 | [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md) | V | Every later lookup: by position (contiguous keys) or binary search over the entries. |

## Behavior

- I: steps 3 to 7 run in ResourceHandle_LoadNow for a synchronous load; the asynchronous path reaches the same slots.

## Open questions

? whether a table is ever reloaded in a session (a language change).
