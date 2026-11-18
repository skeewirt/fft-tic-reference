# TitleBackdropAndInputFlag

- **Kind:** observed behaviour
- **Scope:** the title screen behind another screen
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UIAddon_OnEventBase](../functions/UIAddon_OnEventBase.md), [TitleScreenLayout](../formats/TitleScreenLayout.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Hiding the title add-on hides its backdrop; input reaches an add-on only when its byte +47 is clear.

## Behavior

- V: writers of +47 in the title code: UIAddonFFTOTitlePlaymode vtable slot 17 (0 at 0x1401C5674) and 0x1401C60E4 (1 at 0x1401C6172). I: +47 = takes no input.
- V: `GUIComponent_UpdateNodeTree` skips a node with enabled byte +144 = 0 with its whole subtree.
- V: the title agent's own functions (UITitle_ShowMenu, UIAgentFFTOTitle_Update, UIAgentFFTOTitle_OnAddonEvent, UITitle_OnMenuAction, UITitle_ShowPlayMode) use their agent's +72 / +80 / +88, not the menu add-on's rows.

## Open questions

None recorded.
