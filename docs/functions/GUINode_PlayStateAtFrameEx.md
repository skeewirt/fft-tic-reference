# GUINode_PlayStateAtFrameEx

- **Address:** `0x140409898`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUINode_PlayStateAtFrameEx(GUINode *node, NameKey *key, int frame, char flags)`
- **Callers:** about 24 call sites (UIAddonFFTOEvent_vfunc_2, sub_1400F5974 ... sub_140293560)
- **Callees:** GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

GUINode_PlayStateAtFrame plus a flag byte that also sets the state's pause / hold / loop / keep-alive bytes.

## Behavior

- V: same start as GUINode_PlayStateAtFrame (+104 = 1, PlayState, frame clamp, +84 = +80 = f, +76 = f / 60.0, +106 = 1).
- V (flags): bit0: when state+105 (running) is set and state+107 (paused) is clear, state+107 = 1. bit1: +110 = 1 (hold). bit2: +108 = 1 (loop); else bit3: +108 = 0. bit4: +109 = 1 (keep alive); else bit5: +109 = 0.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Notes

The name is ours (IDB: sub_140409898). Flag byte meanings follow the GUINodeState_Advance field notes (+107 paused, +108 loop, +109 keep, +110 hold); the 'bit0 -> +107' rule only applies when the state is running.

## Open questions

? which flag combinations the callers pass. ? +109 meaning (read from GUINode_UpdateStates: the state is not stopped when it is past its end while +109 is set).
