# CharaSlot_SetParams

- **Address:** `0x1400CCBA0`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `__int64 CharaSlot_SetParams(CharaSlot *s, __int16 palA, __int16 palB, unsigned a4, int flags, char fx0, char fx1, int a8, int pose)`
- **Callers:** CharaRender_SetSlotRequest
- **Callees:** sub_1400CC5DC (reset), CharaAnim_Step (tail jump)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores a slot's sprite parameters and restarts its animation sequence when any of them changed.

## Behavior

- V: compares pose (+72), palettes (+28/+30), a4 (+32), flags (+40), fx bytes (+44/+45) and a8 (+48) with the stored ones; on a difference calls sub_1400CC5DC (reset) then always continues into CharaAnim_Step (tail jump).

## State touched

- Calls: [CharaAnim_Step](CharaAnim_Step.md)

## Referenced by

- Called by: [CharaRender_SetSlotRequest](CharaRender_SetSlotRequest.md)

## Open questions

None recorded.
