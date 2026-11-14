# GUICore_UpdateFrame

- **Address:** `0x1403D7030`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_UpdateFrame(GUICore *core8, UIEvent *ev)`
- **Callers:** GUIMessageHandler_Dispatch (event 1)
- **Callees:** GUIWidget_HitTestPoint, GUILayerXform_MapPointFloat, GUICore_SetFocusComponent, sub_1403D6A64, sub_1403D6F70

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame UI update (raw event 1): finds the node under the mouse pointer and moves hover/focus onto it.

## Behavior

- V: walks the widget list (core+16..+24; widgets are skipped when +74 = 0 or +79 != 0); for the first enabled widget with +77 (pointer-enabled) it maps the pointer (+1872/+1876 of this sub-object, = core+1880/+1884) through the widget's layer transform (GUILayerXform_MapPointFloat on core+208+144*layer) and runs GUIWidget_HitTestPoint with the filter 'Collision nodes only'.
- V: the first hit's node (hit list entry +8) becomes the pointer target; when the pointer moved or a button changed (+1888/+1892/+1902) GUICore_SetFocusComponent/sub_1403D6A64 move focus to it and sub_1403D6F70 updates the hover record (+2064).
- V: focus uses the key triple at +1968/+1984/+2000 (widget id, component name, node name); pointer hover is the triple at +1920..; the node's virtual +96 plays its CursorOver state and posts event 19, the previous focus gets +104 / event 20 (GUIComponent_OnFocusGained/Lost).

## State touched

- Calls: [GUIWidget_HitTestPoint](GUIWidget_HitTestPoint.md), [GUILayerXform_MapPointFloat](GUILayerXform_MapPointFloat.md), [GUICore_SetFocusComponent](GUICore_SetFocusComponent.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Open questions

Pad (stick) focus movement shares this function and is not documented (?).
