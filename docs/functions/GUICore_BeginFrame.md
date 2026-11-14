# GUICore_BeginFrame

- **Address:** `0x1403D6234`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICore_BeginFrame(GUICore *core, float dt, float dt2)`
- **Callers:** UI_FrameUpdate
- **Callees:** GUILayerXform_Recompute, GUICore_DispatchEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Start of a UI frame in the GUI core: stores the frame times and the frame counters, advances the random state, refreshes the viewport transform and dispatches the queued events.

## Behavior

- V: ++core+2092; core+2136 = the application's object at g_Application+1168; core+2100 = dt; core+2104 = dt2; core+2096 += (int64)(dt * 1000.0) (a millisecond clock, truncated per frame).
- V: four dwords at core+2076 .. +2088 are rotated and mixed every frame.
- I: that is a xorshift-style random generator.
- V: when the layer transform scale core+2108 is not 1.0 the transform is reset and recomputed (GUILayerXform_Recompute) and the viewport flag core+2117 is set; with that flag set the viewport fields are refilled and an event of type 4 (carrying the size) is queued with sub_1403D69A8; an event of type 3 is queued every frame.
- V: then the four event queues at core+88 (stride 32 bytes, 68-byte events) are drained in order into GUICore_DispatchEvent.

## State touched

- Calls: [GUILayerXform_Recompute](GUILayerXform_Recompute.md), [GUICore_DispatchEvent](GUICore_DispatchEvent.md)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Called by: [UI_FrameUpdate](UI_FrameUpdate.md)
- Observed behaviours: [UIStateClock](../behaviors/UIStateClock.md)

## Notes

The name is ours (IDB: sub_1403D6234). core+2100 is the dt that GUICore_TickWidget gives to widgets with selector 0 and that GUICursorHand_Update reads for its hold timer; core+2104 is the one for selector 1.

## Open questions

None recorded.
