# SaveData_InflateEntry

- **Address:** `0x14003425C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveData_InflateEntry(int64_t mgr, int64_t *outBuf, uint64_t *outSize, uint64_t size)`
- **Callers:** SaveDataManager_vfunc_15, sub_140035A28, sub_140036064
- **Callees:** SaveData_Scramble, sub_14002823C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decodes one container entry: unscrambles it and inflates it with zlib using a 32768-byte preset dictionary.

## Behavior

- V (J9): the game prepends the two bytes `78 F9` (a zlib header with FDICT); the preset dictionary is 32768 bytes at VA 0x14065F6E0 (dictionary id adler32 0x4DAFCB9C, matches).
- V (J9): the only integrity left is the deflate stream's own Adler-32.

## State touched

- Calls: [SaveData_Scramble](SaveData_Scramble.md)

## Referenced by

- Called by: [sub_140034D7C](sub_140034D7C.md), [sub_140035A28](sub_140035A28.md), [sub_140036064](sub_140036064.md)
- Reads file formats: [SavePngContainer](../formats/SavePngContainer.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

None recorded.
