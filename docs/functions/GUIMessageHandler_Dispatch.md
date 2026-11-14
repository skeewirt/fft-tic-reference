# GUIMessageHandler_Dispatch

- **Address:** `0x1403DC390`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUIMessageHandler_Dispatch(GUIMessageHandler *h, UIEvent *ev)`
- **Callers:** GUICore_DispatchEvent
- **Callees:** virtual

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a raw UI event id to a virtual method of the handler (1->+16, 3->+32, 4->+40, 5->+48, 6->+56, 7..14 -> +64..+120 by id, 15..21 -> +128..+176, 22..25 -> +184..+208, 26 -> +216).

## Behavior

- V: the base class methods are all the shared no-op sub_1400206A8; GUICore overrides slots 2, 4, 5, 6, 7..

## State touched

- Reads: [g_GUICore](../globals/g_GUICore.md)

## Referenced by

- Called by: [GUICore_DispatchEvent](GUICore_DispatchEvent.md)

## Open questions

None recorded.
