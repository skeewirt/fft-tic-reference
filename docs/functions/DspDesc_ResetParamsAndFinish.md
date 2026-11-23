# DspDesc_ResetParamsAndFinish

- **Address:** `0x140608BCC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_ResetParamsAndFinish(__int64 state)`
- **Callers:** only through the table at 0x14065CB00 (slot 7)
- **Callees:** none (virtual call)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 7 of the descriptor table at 0x14065CB00: sets the first two parameters to 1.0 and calls the state's virtual function at offset 40.

## Behavior

- V: with the parameter count at state+12 non-zero it stores 1.0f in parameter 0, and with a count above 1 it stores 1.0f in parameter 1 (the array pointer is at state+16).
- V: then calls the function at offset 40 of the state's vtable with (`state`, 1.0f bits) and returns its result.

## Notes

V: whole body read. The name is ours. The same offset-40 slot is what `DspDesc_Vfunc40` (slot 8) calls with one argument.

## Open questions

?: the role of offset 40 in the vtable.
