# UIAddonFingerCursor_ResetGlide

- **Address:** `0x1401D351C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFingerCursor_ResetGlide(UIAddonFingerCursor *addon)`
- **Callers:** vtable of UIAddonFingerCursor (slot 9, data)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Makes the next placement of the cursor instant instead of a step (vtable slot 9 of the addon).

## Behavior

- V: g_GUICore+1908 = 1; addon+444 = 0 (default factor), addon+448 = 0, addon+440 = g_UIDataModule+24 (0.4), addon+445 = 1 (first placement).

## State touched

- Writes: [UIAddonFingerCursor.follow_k](../structs/UIAddonFingerCursor.md#follow_k), [UIAddonFingerCursor.custom_k](../structs/UIAddonFingerCursor.md#custom_k), [UIAddonFingerCursor.first_placement](../structs/UIAddonFingerCursor.md#first_placement)

## Notes

The name is ours (IDB: sub_1401D351C). GUICursorHand_StepToward skips its rounding step while addon+445 is 1.

## Open questions

None recorded.
