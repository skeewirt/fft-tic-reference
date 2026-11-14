# WidgetRootsAreLayers

- **Kind:** observed behaviour
- **Scope:** every UI widget (the Job Tree, the finger cursor, the footer guides)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [ComponentLayer_Begin](../functions/ComponentLayer_Begin.md), [GUICore_DrawWidget](../functions/GUICore_DrawWidget.md), [GUILayer_Select](../functions/GUILayer_Select.md), [GUIComponentRef_Draw](../functions/GUIComponentRef_Draw.md), [UiLayerComposite](../flows/UiLayerComposite.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every widget's root component is drawn into its own layer record, whether or not it has an effect: the renderer's feature byte at r+606621 is 1 from the initialiser and the widget byte at +83 is 1 for all 51 widgets of the running game, so ComponentLayer_Begin opens a layer at the root. Components with an enabled effect group or a non-zero blend type open further layers inside it. UIB nodes of kind Layer (names like Layer00, LayerRoot, LayerBranches) never open a layer.

## Behavior

- V: ComponentLayer_Begin: the layer is forced when r+606621 is set and (widget +83 is set and the context depth +552 is 0 (the root), or the component byte +561 is set); it is opened when the context carries no layer (+553, which nothing in the code writes: always 0) and either the effects collector reports one or the force applies.
- V (live read, 2026-10-30): widget +83 = 1 in all 51 entries of the widget vector at g_GUICore + 24; the cursor widget (ffto_common_cursor) and the Job Tree widgets are among them.
- V (file data): the finger cursor's Widget component has blend 0 and no effect enabled, so its layer comes only from the widget-root rule: the glove is drawn into a layer target and the layer is then blended onto the frame, which is the two 8-bit stores the captures show.
- V: the other components of the Job Tree that open a layer on their own are those with an effect group enabled in the property block: UnitSelect (glow), the Line components (glow, radius and strength from state tracks), TextBoardJobName (drop shadow) and Cross (single float group).
- I: component byte +561 is set by addon code of the battle UI (seven small functions), not by anything Job Tree specific.

## Referenced by

- Observed behaviours: [JobTreeLayerList](JobTreeLayerList.md)

## Open questions

? who sets widget +83 (read as a dword field; no direct byte writer found).
