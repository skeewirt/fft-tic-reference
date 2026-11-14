# LayerBinds_RecordAllLayers

- **Address:** `0x1403A82A8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall LayerBinds_RecordAllLayers(__int64 binder)`
- **Callers:** RenderFrame_Record (V: single xref)
- **Callees:** LayerBinds_RecordLayer

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Walks every live render layer and records the per-layer shader-resource binds for those flagged as recordable.

## Behavior

- V: renderer R = qword_143CDA098. n = *(u16*)(R+13734) (live layer count). Sets binder+135 = 1 at entry and 0 at exit (recording-mode flag).
- V: for i in 0..n-1: slot = *(u16*)(R + 2*i + 7262) (order table), layer = *(qword*)(R + 8*slot + 88). Null layers skipped.
- V: only layers with (*(u32*)(layer+80) & 0x10000000) (bit 28) are recorded: binder[200*(*(u8*)(layer+86)) + 136] = layer (a 200-byte per-group record whose first qword is the layer pointer; layer+86 is the layer group id), then LayerBinds_RecordLayer(binder, layer).
- V: the loop also re-checks *(u16*)(R+13734) != 0 on every iteration.

## State touched

- Calls: [LayerBinds_RecordLayer](LayerBinds_RecordLayer.md)
- Reads: [g_Renderer](../globals/g_Renderer.md)

## Notes

Companion of the per-layer path in RenderFrame_Record, which calls LayerBinds_RecordLayer directly.

## Open questions

? meaning of bit 28 of layer+80 (probably 'owns a constant buffer'). ? the 200-byte binder group record layout beyond +0.
