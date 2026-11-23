# DspDesc_Vfunc16

- **Address:** `0x14060242C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_Vfunc16(__int64 obj)`
- **Callers:** only through the table at 0x14065CB00 (slot 2), plus many direct calls from the audio engine's code (for example sub_14045EB00, sub_14048E9DC, sub_1404C1700)
- **Callees:** none (virtual call)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 2 of the descriptor table at 0x14065CB00: calls the object's virtual function at offset 16.

## Behavior

- V: reads the vtable pointer at `*obj` and calls the function at offset 16 with `obj`, returning its result.

## Notes

V: whole body read (7 bytes). The name is ours.

## Open questions

?: which class's vtable this serves.
