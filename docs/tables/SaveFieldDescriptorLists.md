# SaveFieldDescriptorLists

- **Kind:** table
- **Area:** [Save data](../areas/save-data.md)
- **Storage:** Executable (built on the stack by code)
- **Address:** `0x1400C2598`
- **Rows:** 11 / 108 / 76 / 2 descriptors of 88 bytes
- **Keyed by:** descriptor position in the list of one saved record type
- **Read by:** [FieldSchema_Run](../functions/FieldSchema_Run.md), [SaveFile_Serialize](../functions/SaveFile_Serialize.md), [SaveUnit_Serialize](../functions/SaveUnit_Serialize.md), [SaveWorld_Serialize](../functions/SaveWorld_Serialize.md), [SaveJobNew_Serialize](../functions/SaveJobNew_Serialize.md), [SaveEquipSet_Serialize](../functions/SaveEquipSet_Serialize.md)
- **Row layout:** [SaveFieldDescriptor](../structs/SaveFieldDescriptor.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The save schema: every saved record type has a function that builds an array of 88-byte field descriptors on the stack and hands it to FieldSchema_Run. Four lists matter for the layout: the file (11 sections), the unit (108 fields), the world block (76) and the job flags (2). About 54 schema functions exist in all.

## Behavior

- V: the descriptors exist only on the stack while a save or load runs: the executable stores the field names as strings and the code that fills the stack, not an array.
- V: the file list names 11 sections with their byte offsets in the save slot: card 0, info 256, world 440, battle 1304, user 37984, then extension sections from 38084 to a last one at 40156; each is a nested record run by its own schema function.
- V: the unit list covers a 600-byte record: single bytes and the item ids up to offset 28, then the stat, ability flag, job level and JP arrays, the name at 220, three 88-byte equipment sets at 294, 382 and 470, and a 32-bit name key at 560.
- V: the job flag list has two entries: a 21-element array of nested one-byte records at offset 0 and a 125-byte array at offset 21.

## Notes

Our names. The in-memory unit table the lists describe is UnitSaveSlots.

## Open questions

- ?: the world list (76 descriptors) is described field by field on its own sheet, not here
