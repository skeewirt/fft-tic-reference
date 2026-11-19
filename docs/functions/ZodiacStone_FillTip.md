# ZodiacStone_FillTip

- **Address:** `0x14016D72C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ZodiacStone_FillTip(void *tip, ...)`
- **Callers:** not recorded
- **Callees:** GuiImage_SetIconById, GUITextNode_SetTextExpandedTemp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the stone's tip (icon, name, summary).

## Behavior

- V: the icon node at +472 gets GuiImage_SetIconById(row +0x20 icon_2); the texts are the name (+0x10) and the summary (+0x14), taking the row (n, 0) when the chosen row's string is empty.

## State touched

- Calls: [GuiImage_SetIconById](GuiImage_SetIconById.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Referenced by

- Observed behaviours: [ZodiacStoneBoardShowsStonesByHeldState](../behaviors/ZodiacStoneBoardShowsStonesByHeldState.md)

## Open questions

None recorded.
