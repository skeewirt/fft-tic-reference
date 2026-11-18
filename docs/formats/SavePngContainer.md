# SavePngContainer

- **Kind:** file format
- **Extension:** `.png`
- **Area:** [Save data](../areas/save-data.md)
- **Read by:** [SaveData_InflateEntry](../functions/SaveData_InflateEntry.md), [SaveData_Scramble](../functions/SaveData_Scramble.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A game save file: an ordinary PNG whose private `ffTo` chunk carries a `UMIF` container. Each entry is scrambled and then deflated against a fixed 32 KB dictionary held in the executable, so a reader needs the container walk, the scramble and that dictionary. The file name is the area name (`ENHANCED`, `AUTOENHANCED`, `SYSTEM`, `CLASSIC`) plus `.png`; manual slots, resume entries and the settings block all travel in this one shape.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="png_signature"></a>+0 | png_signature | `8 bytes` | V | The standard PNG signature; the chunk walk starts at +8. |
| <a id="chunk_tag"></a>chunk +4 | chunk_tag | `char[4]` | V | Chunks are walked in order (length, tag, data, CRC). The save body is the private chunk tagged `ffTo`; the other chunks are skipped. |
| <a id="container_tag"></a>ffTo body +8 | container_tag | `char[4]` | V | `UMIF`, the container tag; a body with another tag is rejected as not a game save. |
| <a id="entry_count"></a>ffTo body +12 | entry_count | `uint32` | V | Number of entries; the table starts at body +16. |
| <a id="entry_record"></a>ffTo body +16 + 32i | entry_record | `{uint32 name_len; uint32 data_len; uint64 name_offset; uint64 raw_len; uint64 data_offset}` | V | One 32-byte record per entry; the dword at +12 of the record has no reader. |
| <a id="entry_name"></a>name_offset | entry_name | `scrambled bytes` | V | The name, scrambled like the data and trimmed of trailing NULs: `fftsave.bin`, `settings.sav`, `resume_*_*.sav`. |
| <a id="entry_data"></a>data_offset | entry_data | `scrambled bytes` | V | Unscrambled, its first 4 bytes are a dictionary id and the rest is deflate data; `raw_len` is the exact inflated size, and a different size is an error. |
| <a id="preset_dictionary"></a>0x14065F6E0 | preset_dictionary | `32768 bytes` | V | The fixed deflate dictionary in the executable's read-only data (its Adler-32 id 0x4DAFCB9C matches the header the inflater builds). It is never stored in the file. |

## Behavior

- V: the scramble is its own inverse: 8-byte blocks are XORed with one 64-bit key, a 4-byte tail with the key's low half, and 2- and 1-byte tails with complement-and-mask rules (SaveData_Scramble).
- V: the stored stream is raw deflate with the zlib header left out; the inflater writes a header with the dictionary flag, applies the 32 KB dictionary and checks the deflate stream's own Adler-32.
- V: the entry's own version decides the payload layout (14 for the manual slot image, 0 for the settings block, 17 for a resume entry); the container carries no version of its own.
- V: the container writer re-reads the file it is about to replace, keeps every entry it was not asked to queue, rebuilds the whole container and writes it, so an entry the game was not asked to write survives its save.
- V: the folder is created by the game at boot and the file is found by area name in the profile's save folder; a missing area file is treated as no save data, not as an error.

## Notes

Entry-level layouts are in ManualSaveEntry (version 14) and ResumeEntry (version 17); the settings block is option state and is not covered here.

## Open questions

? the 8 bytes at the start of the `ffTo` body, before the container tag; ? the dword at +12 of an entry record; ? the other chunk tags a writer of this build can emit besides `ffTo`.
