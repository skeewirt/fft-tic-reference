# SaveFile_QueueEntry

- **Address:** `0x140033B9C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveFile_QueueEntry(int64_t file, const char *name, int version, const void *buf, size_t size)`
- **Callers:** Options_ApplyBlock, SaveSlots_StoreToFile, sub_1400C3140
- **Callees:** memmove, sub_140011750, sub_140011804, sub_140026BD4, sub_140032B94, sub_140033AD4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues one named entry (name, version, data buffer) into the save file object for writing into the PNG container.

## Behavior

- V (J9): signature seen from SaveSlots_StoreToFile: (file object, "fftsave.bin", 14, buffer, 0x1EA488).
- V (J9, decode): the 16-byte file header is `{16, tick, version 14, 0}`; there is no checksum of the payload at this layer.

## Referenced by

- Called by: [SaveSlots_StoreToFile](SaveSlots_StoreToFile.md), [sub_1400C3140](sub_1400C3140.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

None recorded.
