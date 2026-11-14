# EventVar_Alu

- **Address:** `0x1402EC038`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t EventVar_Alu(int op, int dst, int src)`
- **Callers:** EventVar_Read and EventVar_Write only.
- **Callees:** EventVar_ResolveSlot, EventVar_Read (for the write lock), EventTask_Terminate (error trap)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The event variable arithmetic unit: applies one operation to the destination variable using either a literal or another variable as the operand, and stores the result back into the packed store.

## Behavior

- V: op parity chooses the operand. Even ops use `src` as a literal; odd ops read variable `src`. Variable 33 is a random source: a 16-bit linear congruential generator, `seed = seed * 25173 + 13849`, returned as an unsigned 16-bit value.
- V: op meaning by range: up to 177 add; 178-179 subtract; 180-181 multiply; 182-183 divide; 184-185 modulo; 186-187 AND; 188-189 OR; 190 clears the destination (no operand).
- V: a divide by zero calls the error trap EventTask_Terminate; so does any variable id of 1024 or more.
- V: the current value of `dst` is read through EventVar_ResolveSlot, which also tells the width: dword, single bit or nibble. Bit and nibble variables are extracted before the arithmetic and merged back after it, masked to 1 or 15.
- V: a re-entrancy flag, `byte_142FEC547`, skips the write checks when set.
- V: write lock: a destination of 960 or above is stored only if its current value is below 12. In every case the store then happens only when variable 508 (0x1FC) reads 0, or the destination is in 0-43, 112-143 or 508-511, or is one of a fixed set within 48-102.
- V: after a dword store, the low dword of `xmmword_14078D9C0` is refreshed; when the destination was variable 25 it takes the new value.
- I: the lock mode is a protection that freezes most story variables, for example during a replay or a preview.

## State touched

- Calls: [EventVar_ResolveSlot](EventVar_ResolveSlot.md), [EventVar_Read](EventVar_Read.md), [EventTask_Terminate](EventTask_Terminate.md)

## Referenced by

- Called by: [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md)

## Notes

The operation numbers 176-190 are the event system's own arithmetic opcodes (0xB0-0xBE in event scripts); the two accessors above use only 176, 177 and 190. The event interpreter uses the second-group twin, SceneVar_Alu, directly. The caller-saved scratch is variable 0.

## Open questions

What the write lock protects.
