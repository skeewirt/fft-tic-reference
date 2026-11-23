# EventWork_RunCommand

- **Address:** `0x14024F5A0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall EventWork_RunCommand(unsigned int command, __int64 slot, __int64 arg, int arg2)`
- **Callers:** EventScript_Run (constant 0x71), Effect_RunStateMachine (0x70 + reg, 0x72 + reg), sub_14023A0B4 (128, 131 and 0x59 + reg), sub_14035D540, sub_14035D598, sub_14035DCA8
- **Callees:** sub_140254F48, SceneVar_Read, sub_1400C9538, sub_1400C729C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A command switch over per-slot work records of the event system: save, restore, select, read and commit commands, chosen by a command number.

## Behavior

- V: it returns 0 for every command except 129 and 130, which return a stored value.
- V: 106 (slot < 32) moves the slot's byte at `byte_141149ABE` (20-byte stride) into the saved array `byte_142FF8F80` and clears it; 107 copies it back; 113 does that move for all 32 slots; 114 copies all 32 back.
- V: 128 copies a 68-byte (17-dword) sub-record number `arg` of the slot's 544-byte block at `byte_140DE1850` over sub-record 0, stores `arg2 | arg << 8` in `xmmword_140DDEFD0[slot]` and marks the slot's record at `unk_14114B1D0` (stride 168) with 2 and 1.
- V: 129 returns `xmmword_140DDEFD0[slot]`; 130 returns the signed high byte of the word at `word_141149AC2` (20-byte stride).
- V: 122 and 123 set a pair of constant flags in two work blocks (the values 0xE1 and a 64-bit constant that differs by 0x200 between them).
- V: command 131 acts on the slot's stored command byte (refilled from the saved array when zero): bytes 1..29 and 128..130 are committed, any other value returns 0 at once; command 131 itself is not in that set. A committed command copies six words of the slot's pending record into a 32-byte-stride record at 0x142FF8FC4, in some cases calls `sub_1400C9538` or `sub_1400C729C` on the character renderer or rewrites a renderer block, then sets the slot's word to 382 and clears its command byte.
- V: 152 does nothing while `g_ShopModeGate` is non-zero; otherwise it zeroes two word buffers, rebuilds eight 42-dword records (counts as ceil(n/8) of four globals) and calls `sub_140254F48` for each.
- V: 154 clears `byte_140D4003F`; 157 (slot < 32) stores `arg` in a byte of the slot's record and clears one byte (the low byte of the next word).
- I: the commands are event-script operations on per-unit or per-actor work slots; the meaning rests on the callers (EventScript_Run passes the constant 113; Effect_RunStateMachine passes values at offsets 0x70 and 0x72 (113 and 114 as a save-all / restore-all pair); sub_14023A0B4 passes 128 and a variable form 0x59 plus a register).

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Called by: [EffectCb_SixRequests](EffectCb_SixRequests.md)

## Notes

Whole body read (1589 bytes); the case numbers are the compared values. The exact byte positions inside the 20-byte records were not mapped. The 0x200 is the difference of the two stored 64-bit constants, not a value in the code. The 0x59 and 0x72 values are caller-side operands (call sites in sub_14023A0B4 and Effect_RunStateMachine), not in this body.

## Open questions

What the 20-byte slot records are, and what scene variable 39 equal to 14 selects in command 131.
