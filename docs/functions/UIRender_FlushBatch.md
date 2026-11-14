# UIRender_FlushBatch

- **Address:** `0x1403AE0F0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int __fastcall UIRender_FlushBatch(__int64 r, int kind, unsigned int first, unsigned int count, int a5, __int64 drawState)`
- **Callers:** UICommand_ExecuteBatches (V: single xref)
- **Callees:** UIRender_ApplyDrawState, sub_1400ADB20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Issues one batched draw: sets the draw-call type bits of the thread state for the command kind, applies the draw state and submits the range.

## Behavior

- V: ts = *(TLS-state + 56); the dword at ts+124 is rewritten with its low 12 bits and top 10 bits kept (& 0xFFC00FFF) and bits 12..21 (the 0x3FF000 field) set to: kind 16 -> 0x2000, kind 32 -> 0x5000. Any other kind returns 56 and draws nothing.
- V: if count (a3 in the decompile naming = a3 != 0): UIRender_ApplyDrawState(r, drawState) then sub_1400ADB20(ts, a3, a4) (the draw / submit of the range) and returns its result. If a3 == 0 only the state bits are updated.
- I: kind 16 = the plain geometry command, kind 32 = the layer command that UIRender_AppendCommand emits (type 32); 0x2000 / 0x5000 select a primitive / draw type value (2 vs 5) in the same bit field UIBlur_DrawPass sets to 6.
- V: a5 is unused.

## State touched

- Calls: [UIRender_ApplyDrawState](UIRender_ApplyDrawState.md)
- Reads: [RenderContext.state_flags](../structs/RenderContext.md#state_flags)
- Writes: [RenderContext.state_flags](../structs/RenderContext.md#state_flags)

## Referenced by

- Called by: [UICommand_ExecuteBatches](UICommand_ExecuteBatches.md)

## Notes

Parameter naming: first / count are I from the call (a3, a4).

## Open questions

? decode of the 0x3FF000 field (values 2, 5, 6). ? whether kind 34 (image) is flushed elsewhere (it is not accepted here).
