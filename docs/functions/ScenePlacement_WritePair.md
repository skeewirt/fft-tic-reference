# ScenePlacement_WritePair

- **Address:** `0x140240D5C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void ScenePlacement_WritePair(const uint8_t *operands, int flag)`
- **Callers:** EventScript_Run (one call at 0x14023BD4E: opcode 0x2C enters just before it and clears the flag register, so it passes flag 0; opcode 0x53 jumps in after that clear and passes the flag 1 that the interpreter sets at the start of each instruction); EventSubScript_RunTask (call at 0x140235BDB for opcode 0x53, passing 1).
- **Callees:** SceneGroup_ResolveId, EventRef_ResolveSlot, SceneUnit_TestGroupMember, SceneUnit_CopyField4C (called twice per match), atan2f (C library)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes 7-byte placement records for a pair of units: the second unit for each valid, different unit that passes the group test, and the first unit too when flag is 0, with headings computed from the two units' position words. Opcode 0x2C calls it with flag 0 and opcode 0x53 with flag 1.

## Behavior

- V: `operands` points at the operand bytes after the opcode. The first unit reference is the 16-bit value at operands 1 and 2 (operand 1 is the low byte). The second reference is the 16-bit value at operands 3 and 4. Operand 5 goes into record byte 1, operand 6 indexes the byte table at 0x1406720B0 (its value goes into record byte 2), and operand 7 is the scale.
- V: it resolves the second reference with SceneGroup_ResolveId and returns at once, writing nothing, when that returns 0. It then resolves the first reference with EventRef_ResolveSlot and returns unless the result is 0 to 20 (an unsigned 16-bit compare).
- V: it walks the 21 16-bit keys at 0x1406720C0 in this order: 0, 4, 8, 12, 16, 20, 1, 5, 9, 13, 17, 21, 2, 6, 10, 14, 18, 3, 7, 11, 15. For each key it calls SceneUnit_TestGroupMember with the second reference; a failed test goes on to the next key.
- V: when the test passes and the slot now held in the second reference differs from the first unit's slot, it copies the position words of both units with SceneUnit_CopyField4C. If that slot is 0 to 20, it writes the records described below. After that, whatever the slot was, the walk stops when the group mode output of the test is zero.
- V: a passing key whose slot equals the first unit's slot is skipped, and it does not stop the walk.
- V: CopyField4C writes out[0] (the unit's word at node +0x4C) and out[2] (the word at node +0x50). Y is the second unit's +0x50 word minus the first unit's +0x50 word, and X is the second unit's +0x4C word minus the first unit's +0x4C word, both as signed 16-bit values. The heading H is 3072 minus the truncated value of atan2(Y, X) times 4096 divided by 2 pi.
- V: each record is 7 bytes at table unk_142FEC580 plus 7 times the unit slot. The first unit's record (written only when flag is 0) uses H; the second unit's record uses H minus 2048, which is the opposite heading.
- V: byte 0 = bits 8 to 11 of the heading value used for that record. Byte 1 = operand 5. Byte 2 = the byte at 0x1406720B0 indexed by operand 6. Bytes 3 and 4 = 0 and 1 (the 16-bit value 256). Byte 5 is not written. Byte 6 = operand 7 divided by 4, rounded down, for the first unit's record. For the second unit's record, byte 6 = the count times operand 7, divided by 4 rounded down, where the count is 1 for the first write of the call and rises by one after each second-unit write.
- V: the first unit's record is written before the second unit's, and both sit in the same branch (second slot 0 to 20 and different from the first).
- V: the routine changes no object fields; its only writes are the 7-byte table rows.

## State touched

- Calls: [SceneGroup_ResolveId](SceneGroup_ResolveId.md), [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneUnit_TestGroupMember](SceneUnit_TestGroupMember.md), [SceneUnit_CopyField4C](SceneUnit_CopyField4C.md)

## Referenced by

- Called by event opcodes: [0x2C](../opcodes/README.md)

## Notes

The first unit's record exists only for flag 0, so a caller that passes another flag gets the second unit's record alone.

## Open questions

What the three position words at node +0x4C, +0x4E and +0x50 mean in the game; what the 21 keys and the byte table at 0x1406720B0 describe; what the game reads from the 7-byte records (heading, table value, scale).
