# UIListGadget_Bind

- **Address:** `0x14028C5C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIListGadget_Bind(UIListGadget *gadget, GUINode *node, int tag, const char *name, int a5)`
- **Callers:** UIAddonFFTOConfig_BindNodes
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds a list gadget to its node.

## Behavior

- V: called as (gadget, node, tag 151, "List", 0) for General Options' row list.

## Referenced by

- Called by: [UIAddonFFTOConfig_BindNodes](UIAddonFFTOConfig_BindNodes.md), [WorldMapLocationPanel_Init](WorldMapLocationPanel_Init.md)

## Open questions

None recorded.
