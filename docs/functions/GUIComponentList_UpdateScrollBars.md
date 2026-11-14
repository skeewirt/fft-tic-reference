# GUIComponentList_UpdateScrollBars

- **Address:** `0x14040CA50`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIComponentList_UpdateScrollBars(GUIComponentList *list)`
- **Callers:** sub_1401130F8, sub_1401569C0, sub_140160BE0, sub_140161A28, sub_1401A1AE4, sub_140207AA0, sub_14028D7BC, sub_14028D8F4, sub_14028DAEC, sub_1402A48E8, sub_14040CFF4
- **Callees:** GUIComponentList_GetHScroll, GUIComponentList_GetVScroll

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives the horizontal and vertical scroll bars their ranges from the item count and cell size, shows a bar only when the content is larger than the viewport, and clears the dirty byte +684.

## Behavior

- V: C = list+652 (columns), n = list+648 (items), cell w = +688, cell h = +692. W = w * min(n, C); H = h * ((C + n - 1) / C) (integer, ceil(n / C) rows).
- V: horizontal bar (GUIComponentList_GetHScroll): bar+681 = 1 (move pending), bar+652 (lower) = 0, bar+656 (upper) = max(W, 1), bar+660 (viewport) = max(list+696, 1), bar+416 = (W > list+696) (visible flag).
- V: vertical bar: the same with H, list+700 and the bar returned by GUIComponentList_GetVScroll: bar+681 = 1, +652 = 0, +656 = max(H, 1), +660 = max(list+700, 1), +416 = (H > list+700).
- V: list+684 = 0.

## State touched

- Calls: [GUIComponentList_GetHScroll](GUIComponentList_GetHScroll.md), [GUIComponentList_GetVScroll](GUIComponentList_GetVScroll.md)

## Notes

The name is ours (IDB: sub_14040CA50). Writes the bar's +652 / +656 / +660 directly (V), which is what ScrollBar_SetPosition's sheet calls 'the wrong layout for this class' for raw writes from the outside: this function is the class's own way of doing it. bar+416 here toggles the bar's visibility (the same byte other sheets call 'loaded / enabled').

## Open questions

? whether bar+416 is really the visible flag for a ScrollBar (it is the byte GUIComponent_TickTree reads).
