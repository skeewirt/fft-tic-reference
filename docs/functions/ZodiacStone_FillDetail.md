# ZodiacStone_FillDetail

- **Address:** `0x14016E218`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ZodiacStone_FillDetail(void *page, ...)`
- **Callers:** not recorded
- **Callees:** GuiImage_SetIconById, GUINode_PlayStateAtFrame, GUITextNode_SetTextExpandedTemp, NxdTable_GetEntryByKeys2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the stone's detail page (icons, name, description, Clear mark).

## Behavior

- V: the icon +0x20 goes to the node at +64 without any condition; the name (+0x10) and the description (+0x18) fall back to row (n, 0) when empty; the icon +0x1C goes to the node at +568.
- V: row +0x24 (clear_mark) drives the node at +56 ('Clear', bound in sub_14016DB90): 'Enable' when set, else 'Disable'. (A first reading took it for a gate on the icon; it is not.)

## State touched

- Calls: [GuiImage_SetIconById](GuiImage_SetIconById.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md)

## Referenced by

- Observed behaviours: [ClearMarkAppearsOnFourScreens](../behaviors/ClearMarkAppearsOnFourScreens.md), [ZodiacStoneBoardShowsStonesByHeldState](../behaviors/ZodiacStoneBoardShowsStonesByHeldState.md)

## Open questions

None recorded.
