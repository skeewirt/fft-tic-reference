# GUICore_OnInputState

- **Address:** `0x1403D5A9C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICore_OnInputState(GUICore *core, InputState *in)`
- **Callers:** Input listener table (qword_140C69680 +2744, function pointer)
- **Callees:** GUICore_DispatchEvent, sub_1403D69A8, sub_1403DC32C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The UI core's input listener: turns the frame's input state into queued UI events and then pumps the queue through GUICore_DispatchEvent.

## Behavior

- V: copies the 0x548-byte state to core+528; stores the pointer x/y in core+1880/+1884 (the hit test reads them) and the wheel/buttons in +1896..+1911.
- V: raw event ids queued by sub_1403D69A8 (68-byte records): 7 pointer state (x, y, buttons), 8 pointer moved, 9 wheel, 10..21 per-button pressed (&1) / released (&4) / held (&2) groups, 22..25 key queue, 26 pad axes; then event 1 (the frame tick) and a drain loop over the queue.
- V: GUIMessageHandler_Dispatch maps these ids to GUICore virtuals; event 1 reaches GUICore_UpdateFrame, which does the hover hit test.

## State touched

- Calls: [GUICore_DispatchEvent](GUICore_DispatchEvent.md)
- Reads: [g_Application](../globals/g_Application.md), [g_GUICore](../globals/g_GUICore.md)

## Referenced by

- Called by: [Input_ListenerBroadcast](Input_ListenerBroadcast.md)

## Open questions

Which raw id is the left button press (10..13 are four buttons) is not tied to a device (?).
