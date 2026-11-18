# UITitleMenu_BindNodes

- **Address:** `0x1401C3EB0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UITitleMenu_BindNodes(UIAddonFFTOTitle *addon)`
- **Callers:** the add-on's vtable (slot 4)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The title menu add-on's node binding (vtable slot 4): finds the TitleEnhanced and Menu nodes and the six MenuButton nodes, and tags them for the event handler.

## Behavior

- V: finds the node `TitleEnhanced`, then `TitleEnhanced/Menu`, then `MenuButton01` to `MenuButton06` (format `MenuButton%02d`, a loop of 6).
- V: each button found gets node +544 = 121 (the tag `UIAddonFFTOTitle_OnEvent` tests), +548 = its index, +557 = 0, the add-on's id in its listener list (+584, 4 slots), and its `Title` text part is stored in the add-on's row.
- V: the buttons are kind 3 nodes (+536); `+220 = -1` at the end. The kind byte of row i is read at +88 + 24 * i by UIAddonFFTOTitle_OnEvent (event 16, the decide on a node tagged 121, index = node +548), by TitleMenu_FocusCurrent and by TitleMenu_SelectKind.

## Referenced by

- Reads file formats: [TitleMenuLayout](../formats/TitleMenuLayout.md), [TitleScreenLayout](../formats/TitleScreenLayout.md)

## Notes

This name replaces an earlier one (`UnDecorator::getZName`) that was a wrong library match in the database.

## Open questions

None recorded.
