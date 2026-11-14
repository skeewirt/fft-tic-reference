# CharaRenderer_Update

- **Address:** `0x1400D4CB0`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `char CharaRenderer_Update(CharaRenderer *r, float dt)`
- **Callers:** sub_1402574E0 (frame update)
- **Callees:** CharaAnim_Step, CharaRender_DrawFrame, sub_1400C946C, sub_1400C9DCC, sub_1400C7664, sub_1400CB870, sub_1403CB40C, sub_1403CB4E0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of the unit renderer: retires finished job records, ticks the sub-systems and animates and draws every live slot.

## Behavior

- V: clears every 36-byte job record whose state is 2 (4096 records at +0) and decrements the live count at +147456.
- V: the step used for the 19 timed entries at +148104 is 0 when a pause flag (bit 0x10 of byte +24 of qword_143CD9E60) is set.
- V: calls CharaAnim_Step (advance the animation) and CharaRender_DrawFrame (draw the frame) for the slots; the update of the sub-objects at +148080 / +148096 / +148104 (19 timed entries) is done first.

## State touched

- Calls: [CharaAnim_Step](CharaAnim_Step.md), [CharaRender_DrawFrame](CharaRender_DrawFrame.md)
- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md)

## Referenced by

- Called by: [GameTasks_RunFrameSteps](GameTasks_RunFrameSteps.md)

## Open questions

The slot loop and the 19-entry timer block were only skimmed (?).
