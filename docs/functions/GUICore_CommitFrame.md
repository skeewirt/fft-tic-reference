# GUICore_CommitFrame

- **Address:** `0x1403D67D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICore_CommitFrame(GUICore *core, int a2)`
- **Callers:** frame update
- **Callees:** sub_1403E6160, sub_1403E97A8, sub_1403E5258, sub_1403E90A8, GUILayer_ExpandBounds

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame UI commit: resets the renderer, runs every widget's draw, then expands each layer's bounds for its effects.

## Behavior

- V: sub_1403E6160 resets the renderer (512 layer records reinitialised by sub_1403E73A0); widgets are drawn through vtable +88 / +96; two cursor-sized draws (sub_1403E5258); sub_1403E90A8 closes the last layer; then GUILayer_ExpandBounds for every layer 0..(r+606584).
- V: widget order: the widget vector (core+24 .. +32) is walked from the LAST entry to the first (the vector is sorted by descending priority word w+62, so the lowest priority is drawn first and the highest ends on top); a widget is drawn when (w+74 or w+75) is non-zero and w+79 is zero, through GUICore_DrawWidget; otherwise only its vtable +96 hook runs. A widget whose root has no draw leaves no slot (the layer opened for it is reused).
- V: after the widgets, for each of the two layer transforms (core+216 + 144 j) with the int at +128 equal to 1 GUICore_DrawOutsideBars runs and the draw counter is incremented even when the screen has no letterbox bars (live 16:9: transform 0 has the flag, the call adds no quad): the draws land in the slot after the last widget layer, which therefore gets counted (the last slot of the live frame, no quad, never used or packed).

## State touched

- Calls: [GUILayer_ExpandBounds](GUILayer_ExpandBounds.md)

## Referenced by

- Appears in flows: [UiLayerComposite](../flows/UiLayerComposite.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Open questions

None recorded.
