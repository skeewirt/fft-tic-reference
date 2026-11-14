# GUIWidget_FindRefNodeForComponent

- **Address:** `0x1403FA768`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUINode *GUIWidget_FindRefNodeForComponent(GUIWidget *w, GUIComponent *comp)`
- **Callers:** GUICursorHand_GetTargetPoint, GUICursorHand_Update, GUIWidget_GetNodeScreenRect, sub_1400F71E8, sub_1402977C8, sub_140297990, sub_14029F0D4, sub_1402A0024, sub_14040AD5C, sub_14040AEE8
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the component reference node (kind 12) of the widget that points at a given component, by the component's two names.

## Behavior

- V: iterates the node pointer vector w+160..+168; a node qualifies when node+52 == 12 and its name pair matches the component's: (node+208, id node+216) with (comp+280, id comp+288), and (node+224, id node+232) with (comp+504, id comp+512); a pair matches by interned id when both ids are non-zero, otherwise by C string compare. Returns the first match or 0.

## Notes

The name is ours (IDB: sub_1403FA768). Mirrors GUIComponentRef_Draw, which looks a component up with the same pair (ref+208, ref+224).

## Open questions

None recorded.
