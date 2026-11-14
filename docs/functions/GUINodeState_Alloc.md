# GUINodeState_Alloc

- **Address:** `0x140405098`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINodeState *GUINodeState_Alloc(UIStatePool *pool)`
- **Callers:** GUINode_NewState
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Takes a 208-byte state object from the state pool and gives it its default values.

## Behavior

- V: the pool is a vector of 13312-byte blocks (64 objects of 208 bytes) with a 64-bit use mask per block; a new block is allocated when all are in use; the object is the first free bit.
- V: defaults: the four name keys (+0, +16, +32, +48) empty; +64 = 0; +68 = -1; +72 = 1.0 (rate); +76 = +80 = +84 = 0; +88 = +92 = +96 = 0; +104 = 1 (enabled); +105 .. +111 = 0; +112 = 0 (set to 1 by GUINode_NewState); +200 = 0; the vectors at +144 and +176 are empty.

## State touched

- Writes: [GUINodeState.rate](../structs/GUINodeState.md#rate), [GUINodeState.enabled](../structs/GUINodeState.md#enabled), [GUINodeState.record_flags](../structs/GUINodeState.md#record_flags), [GUINodeState.time](../structs/GUINodeState.md#time), [GUINodeState.frame](../structs/GUINodeState.md#frame)

## Referenced by

- Called by: [GUINode_NewState](GUINode_NewState.md)

## Notes

The name is ours (IDB: sub_140405098). Field meanings: struct GUINodeState.

## Open questions

None recorded.
