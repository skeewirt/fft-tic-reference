# Debug_DetectCaptureTools

- **Address:** `0x140082894`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall Debug_DetectCaptureTools(__int64 hostObject)`
- **Callers:** App_RunFrame (0x14002A35C)
- **Callees:** GetModuleHandleA, one COM/GPU interface virtual query, the returned object's vtable +16

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns 1 when a known graphics-capture/injection layer is loaded, or when a GPU/COM query on `hostObject+3504` succeeds. App_RunFrame uses it as the second half of its debug/capture gate.

## Behavior

- V: calls `GetModuleHandleA` for `winPixGpuCapturer.dll`, `Nvda.Graphics.Interception.dll`, `capture-x64.dll`, `d3d12-state-tracker-x64.dll` and `renderdoc.dll`; a non-null handle returns 1 immediately.
- V: otherwise reads the interface pointer at `hostObject+3504`; a null pointer counts as 'no capture layer' and returns 1.
- V: calls the interface's first virtual method with a 16-byte GUID-like value (four dwords: -1482006250, 1270520973, -659258480, 2015082262) and an output pointer; a failure (negative HRESULT) returns 1.
- V: releases the returned object through its vtable slot +16 when the query produced one.
- V: returns 0 only when no capture DLL is loaded and the interface query fails.
- I: the five module names are common graphics capture/debug layers (PIX, Nsight, RenderDoc and two D3D12 state trackers); the GUID identifies a GPU/display interface.

## Referenced by

- Called by: [App_RunFrame](App_RunFrame.md)

## Notes

App_RunFrame evaluates this only when `qword_140C696A8` is non-null, so the capture check is gated by a separate development/debug object.

## Open questions

The interface identified by the 16-byte GUID and what the query specifically reports.
