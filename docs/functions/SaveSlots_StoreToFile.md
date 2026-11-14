# SaveSlots_StoreToFile

- **Address:** `0x1400C39A0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveSlots_StoreToFile(int64_t mgr, const void *cache)`
- **Callers:** sub_1402185A4
- **Callees:** SaveFile_QueueEntry, UIText_Get, sub_140025D74, memmove, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the slot cache (0x1EA488 bytes = 50 x 40164) into the manager's image and queues it as the `fftsave.bin` entry of the save container.

## Behavior

- V (decompile): `memmove(mgr + 1528, cache, 0x1EA488)` and a second copy; header tick from sub_140025D74; `SaveFile_QueueEntry(file, "fftsave.bin", 14, image, 0x1EA488)`.
- V (J9, decode of the owner's file): the entry decodes to 16 + 50 x 40164 bytes, a flat raw memory image, not the named-field tree of FieldSchema_Run.

## State touched

- Calls: [SaveFile_QueueEntry](SaveFile_QueueEntry.md), [UIText_Get](UIText_Get.md), [sub_140025D74](sub_140025D74.md)

## Referenced by

- Appears in flows: [SaveFrameStep](../flows/SaveFrameStep.md)
- Called by: [sub_1402185A4](sub_1402185A4.md)

## Notes

J7 proposed SaveBlob_StoreFftsaveBin for this address; J9 corrected the role (cache to file) and its name is used.

## Open questions

None recorded.
