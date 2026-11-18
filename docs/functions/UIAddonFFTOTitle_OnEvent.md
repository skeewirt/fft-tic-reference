# UIAddonFFTOTitle_OnEvent

- **Address:** `0x1401C4228`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddonFFTOTitle_OnEvent(UIAddonFFTOTitle *addon, int event, GUINode *node)`
- **Callers:** not recorded
- **Callees:** sub_1400F1C5C, sub_1400F4BCC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The title add-on's event handler (vtable slot 2) for the nodes tagged 121 (the six menu buttons).

## Behavior

- V: event 13 sets the current row to -1 and clears the focus.
- V: event 16 (decide) takes an input lock of 0.1 s (`sub_1400F1C5C`), plays sound 0xFC (`sub_1400F4BCC`), then calls the owning agent's vtable +48 with (agent, add-on, 0, the kind of the row, 0).
- V: event 19 (pointer over) sets the current row to the node's +548 and plays cursor sound 0xD1, unless widget +616 suppresses it once.

## State touched

- Calls: [sub_1400F4BCC](sub_1400F4BCC.md)

## Referenced by

- Appears in flows: [TitleMenuAction](../flows/TitleMenuAction.md)

## Notes

The agent's slot is UIAgentFFTOTitle_OnAddonEvent.

## Open questions

None recorded.
