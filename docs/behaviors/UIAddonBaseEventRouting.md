# UIAddonBaseEventRouting

- **Kind:** observed behaviour
- **Scope:** how a screen's events reach its handlers
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UIAddon_OnEventBase](../functions/UIAddon_OnEventBase.md), [UIAddon_CanTakeInput](../functions/UIAddon_CanTakeInput.md), [UIAddonFFTOConfig_OnEvent](../functions/UIAddonFFTOConfig_OnEvent.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every add-on's event handler calls UIAddon_OnEventBase first; input reaches the add-on's slot 12 only when its id is not excluded, byte +47 is clear and slot 3 allows it.

## Behavior

- V: event 1 = input, 4 = per-frame update, 5 = shown, 6 = hidden, 7 = busy query, 0xC = focus a node, 13 = release a list (details on the sheet).
- V: a screen hidden with `UIAddon_Hide` (0x1401D1EAC) sets +43 while it hides; slot 3 refuses input while +42 or +43 is set.
- V: node events of the General Options rows: a switch node (kind 4 at +536, on flag at +648) posts event 21 / 22 to the add-on ids in its listener slots (+584, 4 slots); a list item node has kind 10 at +536.

## Open questions

None recorded.
