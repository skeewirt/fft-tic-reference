# GUICore_DispatchEvent

- **Address:** `0x1403D694C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUICore_DispatchEvent(GUICore *core, UIEvent *ev)`
- **Callers:** GUICore_OnInputState
- **Callees:** GUIMessageHandler_Dispatch (vtable slot 1)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Hands one raw UI event to each registered handler (core+56..+64, vtable slot 1) until one consumes it, then to the core's own message handler (core+8).

## Behavior

- V: sets core+2116 while dispatching.

## State touched

- Calls: [GUIMessageHandler_Dispatch](GUIMessageHandler_Dispatch.md)

## Referenced by

- Called by: [GUICore_BeginFrame](GUICore_BeginFrame.md), [GUICore_OnInputState](GUICore_OnInputState.md)

## Open questions

None recorded.
