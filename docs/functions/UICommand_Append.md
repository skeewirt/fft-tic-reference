# UICommand_Append

- **Address:** `0x1403C4794`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UICommand_Append(UIContext *ctx, int type, unsigned vertexCount, UInt64 *key, UIDrawState *state)`
- **Callers:** UIRender_QueueImageDraw, text queue
- **Callees:** UIDrawState_Copy

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends one 64-byte command record (type dword, then the draw state at +8) to the per-thread command block and reserves its vertex range.

## Behavior

- V: command blocks are 2 KB (0x800) taken from the manager 2 MB buffer at manager+176; records are 64 bytes; vertices are 24 bytes from the pool at manager+184.
- V: the record also stores the vertex count (+56) and first-vertex index (+60), and (key, record) is pushed to the sort list.

## State touched

- Calls: [UIDrawState_Copy](UIDrawState_Copy.md)

## Referenced by

- Called by: [UIRender_AppendCommand](UIRender_AppendCommand.md), [UIRender_QueueImageDraw](UIRender_QueueImageDraw.md)

## Notes

Layout confirmed by reading the live buffer (records start with 34 = 0x22).

## Open questions

None recorded.
