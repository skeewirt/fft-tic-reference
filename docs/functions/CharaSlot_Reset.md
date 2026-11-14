# CharaSlot_Reset

- **Address:** `0x1400CC5DC`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 CharaSlot_Reset(CharaSlotState *s)`
- **Callers:** CharaSlot_SetParams, sub_1400CCAF8
- **Callees:** sub_1400CE1AC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears a slot's animation state and releases its frame-cache entry so the next request rebuilds it.

## Behavior

- V: when the slot has an id (>= 0) and the renderer exists, releases the cached textures (sub_1400CE1AC when present at +68656) and clears the low 4 flag bits of the frame cache entry (renderer+47152 + 44 * id); then sets the slot id fields to -1 and zeroes the rest (pose at +72 included).

## State touched

- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md)

## Open questions

None recorded.
