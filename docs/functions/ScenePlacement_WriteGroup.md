# ScenePlacement_WriteGroup

- **Address:** `0x140241FF0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void ScenePlacement_WriteGroup(const uint8_t *operands)`
- **Callers:** EventScript_Run only (opcode 0x69 case; call at 0x14023D172).
- **Callees:** SceneGroup_ResolveId, SceneUnit_TestGroupMember, SceneUnit_CopyField4C, atan2f (C library)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes a 7-byte placement record for each unit of a unit or group that passes the group test against the 21 keys, each record headed from a cell position given by the operands. Opcode 0x69 calls it.

## Behavior

- V: `operands` points at the operand bytes after the opcode. Operands 1 and 2 are the 16-bit unit or group reference (operand 1 is the low byte). Operand 3 is a cell x value and operand 4 a cell y value, each one byte. Operand 5 is not read. Operand 6 goes into record byte 1, operand 7 indexes the byte table at 0x1406720B0 (its value goes into record byte 2), and operand 8 is the scale.
- V: it resolves the reference with SceneGroup_ResolveId and returns, writing nothing, when that returns 0. Nothing in the routine tests the resolved slot against 0 to 20.
- V: it walks the same 21 keys at 0x1406720C0, in the same order as ScenePlacement_WritePair, calling SceneUnit_TestGroupMember with the reference for each key. A failed test goes on to the next key.
- V: on a pass, the unit whose slot is in the reference after the test gets a record. The routine copies that unit's words with SceneUnit_CopyField4C (out[0] = node +0x4C, out[2] = node +0x50).
- V: heading: Y = 28 times operand 4, plus 14, minus the unit's +0x50 word; X = 28 times operand 3, plus 14, minus the unit's +0x4C word; both as signed 16-bit values. H = 3072 minus the truncated value of atan2(Y, X) times 4096 divided by 2 pi.
- V: the record is 7 bytes at table unk_142FEC580 plus 7 times the unit slot. Byte 0 = bits 8 to 11 of H. Byte 1 = operand 6. Byte 2 = the byte at 0x1406720B0 indexed by operand 7. Bytes 3 and 4 = 0 and 1 (the 16-bit value 256). Byte 5 is not written. Byte 6 = the count times operand 8, divided by 4 rounded down, where the count is 1 for the first record of the call and rises by one after each write.
- V: after each write, if the group mode output of the test is zero, the walk stops. A failed test does not stop it.
- V: the record offset is 7 times the slot number with no bound test, so a slot of 21 or more is written at an offset past the 21 rows.
- V: the routine writes only the table rows; it changes no object fields.

## State touched

- Calls: [SceneGroup_ResolveId](SceneGroup_ResolveId.md), [SceneUnit_TestGroupMember](SceneUnit_TestGroupMember.md), [SceneUnit_CopyField4C](SceneUnit_CopyField4C.md)

## Notes

Unlike ScenePlacement_WritePair it writes no first-unit record and makes no difference check, and its heading comes from the cell position instead of a second unit.

## Open questions

Whether a single-unit reference can resolve to a slot of 21 or more and reach the record write; what operand 5 is for (not read here); what the cell scale 28 and the offset 14 are in the game.
