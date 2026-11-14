# GUIWidget_GetNodeScreenRect

- **Address:** `0x1403FA86C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIWidget_GetNodeScreenRect(GUIWidget *w, int rect[4], GUINode *node)`
- **Callers:** GUICursorHand_Update, GUICursorHand_GetTargetPoint, sub_14040B828 (slider), sub_14016D9E0
- **Callees:** sub_1403F9D18, sub_1403FA768

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A node's rectangle in UI (screen) pixels: its four corners pushed through its own 2x3 matrix (+160) and then each ancestor's, up to the root; result is the rounded bounds {left, top, right, bottom}.

## Behavior

- V: when an ancestor's scale mode (+540) is 1 the corners are rescaled by (parent size)/(component design size +336/+340) before applying its matrix.

## Referenced by

- Called by: [GUICursorHand_GetTargetPoint](GUICursorHand_GetTargetPoint.md), [GUICursorHand_Update](GUICursorHand_Update.md)
- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Open questions

None recorded.
