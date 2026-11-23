# DspDesc_CallBackend1

- **Address:** `0x140608A74`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_CallBackend1(__int64 state, __int64 arg, unsigned int arg2, __int64)`
- **Callers:** only through the table at 0x14065CB00 (slot 1)
- **Callees:** sub_140609E2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 1 of the descriptor table at 0x14065CB00: the same parameter block as slot 0, passed with two extra arguments to the second function of the backend table.

## Behavior

- V: builds the same six-float block as `DspDesc_CallBackend0` (elements 0..4 written as there, element 5 unwritten, a zero qword after the block).
- V: calls `sub_140609E2C()` and calls the function at offset 8 of the table it returns with (block, `arg`, `arg2`), returning its result.

## Notes

V: whole body read. The name is ours.

## Open questions

?: the meaning of `arg` and `arg2`.
