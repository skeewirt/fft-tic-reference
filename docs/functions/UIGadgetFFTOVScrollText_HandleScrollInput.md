# UIGadgetFFTOVScrollText_HandleScrollInput

- **Address:** `0x1402AB0B8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UIGadgetFFTOVScrollText_HandleScrollInput(UIGadgetFFTOVScrollText *g, InputState *in)`
- **Callers:** about 20 window update methods (the glossary, equipment windows, job windows ...): sub_140112748, sub_14012E82C, sub_140131068, sub_140168A18 ... sub_140295D2C, sub_14037085C
- **Callees:** sub_1400FE2D0, ScrollBar_SetPosition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Mouse wheel / stick scrolling of a scroll-text gadget: moves the scroll bar by 20 units per wheel notch or by the stick axis; returns 1 when it scrolled.

## Behavior

- V: over = 1 when the hit-test node at g+320 is null; otherwise over = sub_1400FE2D0(node, g+328) (true when the mouse point (g_GUICore +1880 / +1884) lies inside the node's hit region and the topmost hit component's byte +143 equals the id g+328).
- V: bar = qword (g + 24); acts only when bar and bar byte +416 (enabled) are set.
- V: if wheel = int (in+8) != 0 and over: pos = (int)(float(bar+648) + float(wheel * -1.0) * 20.0). Else if signed byte in+1227 != 0: pos = (int)(float(bar+648) + (-float(g_GUICore+2100) * (signed char)in[1227]) * 20.0). Calls ScrollBar_SetPosition(bar, pos, 1, 1) and returns 1.
- V: returns 0 when nothing scrolled.

## State touched

- Calls: [ScrollBar_SetPosition](ScrollBar_SetPosition.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Notes

Name proposed (IDB: sub_1402AB0B8). The stick axis term is scaled by a float at g_GUICore+2100 (per-frame scroll speed; value not read).

## Open questions

? the unit of in+8 (wheel notch count), the sign convention of in+1227 and the float at g_GUICore+2100.
