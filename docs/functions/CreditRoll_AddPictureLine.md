# CreditRoll_AddPictureLine

- **Address:** `0x1401BEF44`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int CreditRoll_AddPictureLine(void *roll, int *spacing, void *template, int icon, int height)`
- **Callers:** sub_1401CB254
- **Callees:** GUIWidget_FindComponentCached, Icon_FormatPath, GuiImage_SetIconById, GUINode_SetSize, GUINode_SetPosition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Credit roll line type 5: draws a picture line.

## Behavior

- V: builds the image path with Icon_FormatPath(icon) and sets the image with GuiImage_SetIconById.
- V: sets the image node's height to the height argument (UICreditRow icon_height, read by CreditRoll_Step), then advances the roll's y position by the node height and the spacing.

## State touched

- Calls: [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [Icon_FormatPath](Icon_FormatPath.md), [GuiImage_SetIconById](GuiImage_SetIconById.md), [GUINode_SetSize](GUINode_SetSize.md), [GUINode_SetPosition](GUINode_SetPosition.md)

## Notes

Name is ours. The stock credits have no row of line type 5.

## Open questions

None recorded.
