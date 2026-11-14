# SceneUnit_ApplyFlagRow

- **Address:** `0x140240C9C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_ApplyFlagRow(const uint8_t *operands)`
- **Callers:** EventScript_Run (opcode 0x8C case; call at 0x14023DC01); EventSubScript_RunTask (call at 0x140235C27).
- **Callees:** EventRef_ResolveSlot, SceneObject_FindBySlot, `sub_14021F538`, `sub_14021F414`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets or clears a flag on one unit, writes its 7-byte row when the slot is 0 to 20, and calls two scene helpers with the slot and operand values. Opcode 0x8C calls it.

## Behavior

- V: `operands` points at the operand bytes after the opcode. Operands 1 and 2 are the 16-bit reference (operand 1 is the low byte), resolved with EventRef_ResolveSlot. If the result has bit 15 set (negative as a 16-bit value), the routine returns that result at once and does nothing else.
- V: otherwise it looks up the 16-bit slot with SceneObject_FindBySlot. A slot of 2000 finds no object, because the key is compared as a 16-bit value against a byte.
- V: operand 5 is the high byte of the signed 16-bit value at operands 4 and 5. If it is zero and the object exists, bit 0x01 of the object's byte +143 is cleared. If it is nonzero and the object exists, bit 0x01 of byte +143 is set and the word at +24 is set to 0.
- V: if the slot is 0 to 20 (unsigned 16-bit compare), it writes the 7-byte row at unk_142FEC580 plus 7 times the slot: byte 0 = operand 3, byte 4 = 0 and byte 6 = 0. Bytes 1, 2, 3 and 5 are not written.
- V: for any slot that is not negative, including 2000, it calls sub_14021F538 with the slot and operand 3 as a byte, and then returns the value of sub_14021F414 called with the slot and the signed 16-bit value of operands 4 and 5.
- V: sub_14021F538 (helper): if event variable 509 is zero and ScenePreview_IndexOfSlot(slot) is 0 or more, it reads byte +436 of preview record number index (for index 21 or more it reads the absolute address 0x1B4). When that byte is nonzero it calls sub_140272B14 with ScenePreview_SlotOfIndex(byte AND 0x1F). It always ends by calling sub_140272B14 with the slot and the value.
- V: sub_140272B14 (level 2): if the object exists, it stores the value times 256 as a word at +0x7C, calls sub_140268E04 with the count max(2, the unsigned word at +0x1FC divided by 2) and the object, and returns the slot. Without an object it returns -1.
- V: sub_14021F414 (helper): it calls sub_140272A04 (slot, value) and returns, when event variable 509 is nonzero, when event variable 111 is zero, when ScenePreview_IndexOfSlot is negative, when the value is 500 or more (unsigned), and when sub_140249088(4, ...) returns under 2 and byte +436 of the record has no bits 0xC0. Otherwise it sets the global callback qword_140D40940 to sub_1402729EC when byte +436 has bits 0xC0, or to sub_140272964 otherwise, and calls it with the slot. When dword_140D40948 is nonzero it first zeroes the qwords at +96 and +104 of block 0 of off_140783088 and calls through the global pointer.
- V: sub_140272A04 (level 2): if the object exists, and when the global dword_140782A94 is 439 and the object's byte +10 is 0x45, it calls sub_1402735F0(slot, 1, 2) for value 600, and for value 2 it calls sub_14026947C(object, 0, 1) and zeroes dword_142E7FB18[slot + 420] when that dword is at least 100. In every case with an object it then sets the word at +16 to value + 1.
- V: sub_140249088 (level 2): for selector 4 it returns bits 5 to 7 of byte 3 of 8-byte record number (a2 + a3 times the byte at 0x140C6AD6A + (a4 << 8)) in table byte_140D8DCB0.
- I: sub_140268E04, sub_1402729EC, sub_140272964, sub_1402735F0 and sub_14026947C were read only as far as their first lines; the fields they write beyond those lines are not described here.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Notes

A reference that resolves to 2000 still reaches both helpers, which then find no object, so only the row write and the flag write depend on the slot being found.

## Open questions

The meaning of object byte +143 bit 0x01, word +24 and the 7-byte row; which index values ScenePreview_IndexOfSlot can return, since 21 or more makes both helpers read the absolute addresses 0x4F to 0x51 and 0x1B4; what the game does with the value sent through the callbacks.
