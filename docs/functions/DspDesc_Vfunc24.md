# DspDesc_Vfunc24

- **Address:** `0x1406024EC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_Vfunc24(__int64 obj)`
- **Callers:** only through the table at 0x14065CB00 (slot 3), plus many direct calls from the audio engine's code (for example sub_14045ED50, sub_1404C0E00, sub_1404D3710)
- **Callees:** none (virtual call)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 3 of the descriptor table at 0x14065CB00: calls the object's virtual function at offset 24.

## Behavior

- V: reads the vtable pointer at `*obj` and calls the function at offset 24 with `obj`, returning its result.

## Notes

V: whole body read (7 bytes). The name is ours.

## Open questions

?: which class's vtable this serves.
