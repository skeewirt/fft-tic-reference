# GUICursorHand_StepToward

- **Address:** `0x1401D37D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUICursorHand_StepToward(GUICursorHand *hand, int x, int y, char instant)`
- **Callers:** GUICursorHand_Update (inlined copy), sub_1401F16F4
- **Callees:** GUINode_SetPosition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One step of the hand's travel: pos = roundf(pos + (target - pos) * k), per axis, written to the hand node.

## Behavior

- V: k = hand+440 when hand+444 is set, else g_UIDataModule+24 = 0.4; skipped (the hand jumps to the target) when instant is set or hand+445 is 1 (first placement).
- V: the integer position is stored in hand+432/+436; hand node +149 = 1 marks it moved.
- I: called once per UI frame (60 per second: the main loop sleeps to 1/60 s), so the hand covers 40% of the remaining distance every 16.7 ms; rounding stalls it within 1 px of the target.
- V: this step has no time term (it is per UI frame), while the glove's bob runs on the UI frame time; both results are integers, written to different nodes: this one to the cursor reference node, the bob to the IconHand node inside the Hand component. They meet only in the float node matrices, which add integers exactly: nothing rounds their sum.

## State touched

- Calls: [GUINode_SetPosition](GUINode_SetPosition.md)
- Reads: [g_UIDataModule](../globals/g_UIDataModule.md), [UIAddonFingerCursor.last_x](../structs/UIAddonFingerCursor.md#last_x), [UIAddonFingerCursor.last_y](../structs/UIAddonFingerCursor.md#last_y), [UIAddonFingerCursor.follow_k](../structs/UIAddonFingerCursor.md#follow_k), [UIAddonFingerCursor.custom_k](../structs/UIAddonFingerCursor.md#custom_k), [UIAddonFingerCursor.first_placement](../structs/UIAddonFingerCursor.md#first_placement)
- Writes: [UIAddonFingerCursor.last_x](../structs/UIAddonFingerCursor.md#last_x), [UIAddonFingerCursor.last_y](../structs/UIAddonFingerCursor.md#last_y), [UIAddonFingerCursor.first_placement](../structs/UIAddonFingerCursor.md#first_placement)

## Referenced by

- Observed behaviours: [CursorGloveBob](../behaviors/CursorGloveBob.md)

## Notes

The studio reproduces the glove origin in its viewer code.

## Open questions

None recorded.
