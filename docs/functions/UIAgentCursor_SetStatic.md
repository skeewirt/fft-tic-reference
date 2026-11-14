# UIAgentCursor_SetStatic

- **Address:** `0x1401D2E0C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentCursor_SetStatic(UIAgentCursor *agent, char on)`
- **Callers:** sub_1400FB3B0, sub_14015BAC4, sub_14016C110, sub_1401F3F70 (twice)
- **Callees:** UIAddonFingerCursor_FreezePose

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Switches the finger cursor between its animated mode and a static mode in which it neither bobs nor glides.

## Behavior

- V: nothing happens unless on differs from agent+132.
- V: on = 1 with an addon: UIAddonFingerCursor_FreezePose(addon); the cursor node (addon+56) is hidden (+144 = 0), the glide is reset (addon+444 = 0, addon+440 = g_UIDataModule+24, addon+445 = 1: next placement instant) and the node is shown again (+144 = 1). agent+132 = on in every case.
- V: while agent+132 != 0 GUICursorHand_Update only sets the node visible; it does not place it, so the hand stays where it was.

## State touched

- Calls: [UIAddonFingerCursor_FreezePose](UIAddonFingerCursor_FreezePose.md)
- Writes: [UIAgentCursor.static_mode](../structs/UIAgentCursor.md#static_mode), [UIAddonFingerCursor.follow_k](../structs/UIAddonFingerCursor.md#follow_k), [UIAddonFingerCursor.custom_k](../structs/UIAddonFingerCursor.md#custom_k), [UIAddonFingerCursor.first_placement](../structs/UIAddonFingerCursor.md#first_placement)

## Notes

The name is ours (IDB: sub_1401D2E0C).

## Open questions

? Which screens switch the cursor to static mode (none of the Job Tree functions does).
