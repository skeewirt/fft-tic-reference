# DspDesc_CallBackend0

- **Address:** `0x140608A1C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_CallBackend0(__int64 state, __int64, __int64, __int64)`
- **Callers:** only through the table at 0x14065CB00 (slot 0), reached from the audio engine's own code
- **Callees:** sub_140609E2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 0 of the 20-slot descriptor table at 0x14065CB00: packs a parameter block from a state object and calls the first function of the backend table that `sub_140609E2C` returns.

## Behavior

- V: builds six floats on the stack: elements 0..4 of a six-float block: element 0 is the float at `*state`, element 1 holds the integer 48000, elements 2..4 are the three ints at `*(state + 8)` converted to float; element 5 is never written, and the qword right after the block is set to zero.
- V: calls `sub_140609E2C()` (it returns the address of the table `off_14065CD20`) and calls the first function of that table with the block, returning its result.
- I: 48000 is a sample rate in Hz and the descriptor table is an audio effect's (rests on the number and on slot 6's error text naming a DSP parameter).

## Notes

V: whole body read. The name is ours. Other slots of this table: `DspDesc_CallBackend1` (1), `DspDesc_Vfunc16` (2), `DspDesc_Vfunc24` (3), `DspDesc_Vfunc32` (4), `DspDesc_ReturnArg` (5 and 15), `DspDesc_SetParam` (6), `DspDesc_ResetParamsAndFinish` (7), `DspDesc_Vfunc40` (8).

## Open questions

?: what the backend's first function does and what the state's first float is.
