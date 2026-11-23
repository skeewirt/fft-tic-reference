# DspDesc_Vfunc40

- **Address:** `0x140463CB8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_Vfunc40(__int64 obj)`
- **Callers:** only through the table at 0x14065CB00 (slot 8), plus many direct calls from the audio engine's code (for example sub_14042A900, sub_1404C1290, sub_1404C2220)
- **Callees:** none (virtual call)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 8 of the descriptor table at 0x14065CB00: calls the object's virtual function at offset 40.

## Behavior

- V: reads the vtable pointer at `*obj` and calls the function at offset 40 with `obj`, returning its result.

## Notes

V: whole body read (7 bytes). The name is ours.

## Open questions

?: which class's vtable this serves.
