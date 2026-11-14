# LayerBinds_RecordLayer

- **Address:** `0x1403A8354`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall LayerBinds_RecordLayer(__int64 binder, __int64 layer)`
- **Callers:** LayerBinds_RecordAllLayers, RenderFrame_Record (V)
- **Callees:** LayerBinds_Push

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Records two bind entries for one layer: the per-group constant buffer and, if the layer has a render target, that target's buffer.

## Behavior

- V: target = *(qword*)(layer+40). First push: LayerBinds_Push(binder, layer, *(u16*)(binder+48), *(qword*)(binder + 8*(*(u8*)(layer+86)) + 8)), i.e. slot index binder+48 with the buffer pointer from the per-group array starting at binder+8, indexed by layer group id (layer+86).
- V: if target != 0, second push: LayerBinds_Push(binder, layer, *(u16*)(binder+50), *(qword*)(target+3248)); the buffer comes from target+3248.
- V: returns the result of the last push.
- I: u16s at binder+48 and +50 are shader constant-buffer slot indices resolved at init (cf. UIRender_CreateBuffers storing slot ids as u16).

## State touched

- Calls: [LayerBinds_Push](LayerBinds_Push.md)

## Referenced by

- Called by: [LayerBinds_RecordAllLayers](LayerBinds_RecordAllLayers.md)

## Open questions

? what the second buffer at target+3248 holds (per-target size / texel constants?).
