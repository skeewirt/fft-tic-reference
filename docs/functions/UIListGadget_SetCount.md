# UIListGadget_SetCount

- **Address:** `0x14028D7BC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIListGadget_SetCount(UIListGadget *gadget, int n)`
- **Callers:** ConfigMenu_ShowTab
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the row count, scrolls to the top and redraws.

## Behavior

- V: read from the decompilation.

## Referenced by

- Called by: [BgmMode_OnTabButton](BgmMode_OnTabButton.md), [ConfigMenu_ShowTab](ConfigMenu_ShowTab.md), [WorldMapBaseList_ClearRecords](WorldMapBaseList_ClearRecords.md), [WorldMapBaseList_SelectTab](WorldMapBaseList_SelectTab.md)

## Open questions

None recorded.
