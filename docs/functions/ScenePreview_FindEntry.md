# ScenePreview_FindEntry

- **Address:** `0x14027260C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *ScenePreview_FindEntry(char key, int32_t *status)`
- **Callers:** 17 routines (26 call sites): EventScript_Run (3), EventRef_ResolveSlot (4), sub_1402DE204 (4), sub_1402C60E4 (2), and about 11 others including sub_1400CB870, sub_140226CA0, sub_140227458, EventUnitBlock_RunTask, sub_140239144, sub_140239294, sub_140240B8C, sub_1402416C8 and sub_14033BE88.
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a preview-unit record by a one-byte key and reports how it was found through the status pointer. The table is 21 records of 512 bytes at g_BattleUnitTable.

## Behavior

- V: the table is 21 records of 512 bytes, starting at `g_BattleUnitTable` (0x141853CE0) and ending at 0x1418566E0. The key is compared with byte +401 of each record; the flag bytes read are +1, +97, +98 and +437.
- V: pass 1, records 0 to 20 in order: a record matches when byte +1 is not 0xFF and byte +401 equals the key. The status is the record index (0 to 20), or -3 when bit 0x40 of byte +97 or bit 0x01 of byte +98 is set. The record pointer is returned in both cases.
- V: pass 2, only when pass 1 finds nothing: a record matches when byte +1 is 0xFF, byte +401 equals the key and byte +437 is not 0xFF. Byte +437 = 0 gives status -2, 0x80 gives -3 and 2 gives -6; each returns that record. Other values are skipped.
- V: when nothing matches it returns null and sets status -3.
- V: the key is a char parameter, so only its low 8 bits are compared. The function writes nothing else and calls nothing.

## Referenced by

- Called by: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [EventRef_ResolveSlotForMessage](EventRef_ResolveSlotForMessage.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md), [EventUnitStatus_RunMembers](EventUnitStatus_RunMembers.md), [sub_1402C60E4](sub_1402C60E4.md)
- Called by event opcodes: [0x45](../opcodes/README.md)

## Notes

sub_140272538 reads the same records by byte +0 (its unit id), so each record carries a unit id at +0 and a second id at +401.

## Open questions

What bytes +1, +97, +98, +401 and +437 represent, and what the status codes -2, -3 and -6 mean to the callers.
