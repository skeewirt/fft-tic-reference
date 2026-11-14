# LayerBinds_Push

- **Address:** `0x1403A83B0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 LayerBinds_Push(LayerBinder *b, Layer *layer, unsigned __int16 slot, void *resource)`
- **Callers:** LayerBinds_RecordLayer (two sites)
- **Callees:** sub_1403C1868, sub_140031D7C (vector growth)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends a (slot, resource) pair to the binder's per-layer (mode 1) or per-target (mode 2) vectors; the pairs are replayed into a render command by LayerBinds_Replay.

## Behavior

- V: mode = byte b+135: 0 does nothing; 1 uses idx = u8 layer+86 and the vector pair at b+176+200*idx (u16 slots) / b+144+200*idx (qword resources); 2 uses idx = u8 layer+90 and the pair at b+376+200*idx / b+344+200*idx; other values return.
- V: both vectors are std::vector: begin at +8, end at +16, capacity end at +24 of the 16-byte-offset header; a push with spare capacity stores the value and adds 2 (slots) or 8 (resources) to the end pointer, else it calls the grow helper (sub_1403C1868 for u16, sub_140031D7C for qwords).

## Referenced by

- Called by: [LayerBinds_RecordLayer](LayerBinds_RecordLayer.md)

## Notes

The name is ours (IDB: sub_1403A83B0). Trivial helper; IDA shows it as variadic because the resource pointer is the 4th argument.

## Open questions

None recorded.
