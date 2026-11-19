# UIListGadget_RefreshVisible

- **Address:** `0x14028DCA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIListGadget_RefreshVisible(UIListGadget *gadget)`
- **Callers:** UIListGadget_SetCount
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Posts event 0x1E (draw row) for every visible row.

## Behavior

- V: read from the decompilation.

## Referenced by

- Called by: [BgmMode_PlaySelected](BgmMode_PlaySelected.md), [BgmMode_ToggleTitleLanguage](BgmMode_ToggleTitleLanguage.md)

## Open questions

None recorded.
