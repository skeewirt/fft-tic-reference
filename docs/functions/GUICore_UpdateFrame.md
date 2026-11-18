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
- V: keeps the last pointed node by name, as three UI name keys at core +2016 (widget), +2032 and +2048 (the component's +504 and +280 keys; `UIName_Assign`, 0x1403D750A..). Each frame it finds the widget with `GUICore_FindWidgetByKey` (the live widget list core +24..+32, by name id or string) and the component with `GUIWidget_FindComponentCached(widget, +2048, +2032, no cache)` (the widget's map +128 / +136, then its vector +104) and calls that component's vtable +72 / +64 (cursor out); when the pointed node changes it resets the keys with `UIName_SetKey(key, Str)` (`Str` 0x1406F9FA0, the empty string).
- V (crash dump, 2026-11-13): the component the pointed-node lookup returned held the vtable of a `UIResourceHandle` (vtable 0x140721BF0, slot 8 its deleting destructor; a data address from the dump, not used by this function's own code), reached by the call through vtable +0x40 (return 0x1403D7638): a component pointer to freed memory reused by a resource handle of a screen opened since. I: the pointed-node names still named a node of a screen freed earlier; the minidump holds no heap, so which widget is not read. I (2026-11-18): the same signature (StringHandle_Release <- UIResourceHandle_Delete, return 0x1403D7638) as the row freed inside its decide event below, so likely the same cause.
- V: on a mouse release over the pointed component it calls that component's vtable +0x48 (0x1403D75F3), resets the three keys (`UIName_SetKey(this + 0x7D8 / 0x7E8 / 0x7F8, Str)`, 0x1403D75FB..0x1403D762A; `this` = core + 8, as this function is the GUICore vtable at object +8, so these are core +2016 / +2032 / +2048) and then calls the SAME component pointer's vtable +0x40 (0x1403D7635, return 0x1403D7638); the pointer is not looked up again between the two calls.
- V (seen live 2026-11-18, reproduced with one mouse click, two dumps): a screen whose decide handler for a click on a list row rebuilt the list's rows at once (the list's row count set again, its rows shown again, inside the event) crashed in StringHandle_Release <- sub_140095E5C <- UIResourceHandle_Delete, called through vtable +0x40 at 0x1403D7635: the clicked row's component was freed inside the event and its memory reused. The same decide from the keyboard did not crash, and rebuilding the rows in the screen's next per-frame update instead of inside the event did not crash (click and keyboard). I: the decide event is raised inside the +0x48 call.

## State touched

- Calls: [GUIWidget_HitTestPoint](GUIWidget_HitTestPoint.md), [GUILayerXform_MapPointFloat](GUILayerXform_MapPointFloat.md), [GUICore_SetFocusComponent](GUICore_SetFocusComponent.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Open questions

Pad (stick) focus movement shares this function and is not documented (?).
