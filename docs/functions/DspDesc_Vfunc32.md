# DspDesc_Vfunc32

- **Address:** `0x140608AE4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_Vfunc32(__int64 obj, unsigned int *in, __int64 out, int flag)`
- **Callers:** only through the table at 0x14065CB00 (slot 4)
- **Callees:** none (virtual call)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 4 of the descriptor table at 0x14065CB00: calls the object's virtual function at offset 32 with the fields of an input block and an output block.

## Behavior

- V: when `flag` is 0 it copies `in[1]` to `out[1]` (the dword at out+4) first.
- V: calls the function at vtable offset 32 of `obj` with (`obj`, `in[0]`, `in[1]`, the qword at in+8, `out`, `out + 4`, the qword at out+8) and returns its result.
- I: the blocks are an input and an output buffer descriptor (rests on the table being an audio effect descriptor; not decoded).

## Notes

V: whole body read. The name is ours.

## Open questions

?: the field meanings.
