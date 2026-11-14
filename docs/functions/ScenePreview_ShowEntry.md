# ScenePreview_ShowEntry

- **Address:** `0x14027313C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t ScenePreview_ShowEntry(int slot, int flag)`
- **Callers:** EventScript_Run (opcode 0x45, at 0x14023C3F9, 0x14023C4F9 and 0x14023CA88); EventUnitBlock_RunTask (at 0x140235E65).
- **Callees:** sub_1402718CC (claim a preview entry), sub_1403041A4 (queues one draw entry)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows the preview-table entry for a slot: clears the preview globals, claims the entry and queues a draw entry built from the record's fields. Used by opcode 0x45.

## Behavior

- V: clears dword_141856720, the qword at xmmword_140CE3240, the dword at +8 of that global and qword_140CE3250.
- V: when slot is 0 to 20 it uses the record g_BattleUnitTable + slot*512; otherwise the record pointer is null.
- V: calls sub_1402718CC(slot) to claim the entry for the slot if it is free (see ScenePreview_ClaimForUnit).
- V: calls sub_1403041A4 with the record's byte +79, byte +80, byte +81 bit 7, byte +81 low nibble, the word from +399 (0x18F) as the fifth argument, the word from +400 (0x190) as the sixth, 255 as the seventh, the record pointer as the eighth and flag as the ninth.
- V: returns 1.

## Referenced by

- Called by: [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md)
- Called by event opcodes: [0x45](../opcodes/README.md)

## Notes

sub_1403041A4 appends an 8-dword entry to the list at dword_141856720 (the count is its first dword, the limit is 16). A fifth argument of 170 or more sets the high word of that entry's second field to 1.

## Open questions

What consumes the queued entries, what the record bytes +79, +80 and +81 mean, and what the flag argument selects.
