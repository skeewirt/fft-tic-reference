# ManualSaveEntry

- **Kind:** file format
- **Extension:** `.bin`
- **Area:** [Save data](../areas/save-data.md)
- **Read by:** [SaveSlots_LoadFromFile](../functions/SaveSlots_LoadFromFile.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The `fftsave.bin` entry of `enhanced.png` (and of `classic.png`): one flat image of the 50-slot save cache, 50 x 40,164 bytes behind a 16-byte header. There is no per-slot file and no per-slot write: a save, a delete and an import all rewrite the whole image.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="header"></a>+0 | header | `{uint32 header_size; uint32 crc32; uint32 version; uint32 reserved}` | V | Header size 16, CRC-32 over the 50-slot payload, version 14, reserved 0. |
| <a id="slots"></a>+16 | slots | `slot[50]` | V | One 40,164-byte (0x9CE4) slot per index; slot n starts at +16 + 40,164 n. |
| <a id="magic"></a>slot +0 | magic | `char[2]` | V | `SC`: a slot that starts with this pair is used; any other slot is skipped by the load list. |
| <a id="summary_job"></a>slot +274 | summary_job | `uint8` | V | The leader's job byte as the load list shows it. |
| <a id="summary_level"></a>slot +275 | summary_level | `uint8` | V | The leader's level. |
| <a id="place"></a>slot +278 | place | `uint8` | V | The place byte the list shows. |
| <a id="situation"></a>slot +282 | situation | `uint8` | V | 1 marks a slot saved in battle; loading such a slot also requests its resume entry. |
| <a id="unit_records"></a>slot +1304 | unit_records | `UnitSaveRecord[54]` | V | 54 records of 600 bytes, the same layout the live table g_UnitSaveData holds (see UnitSaveRecord). |
| <a id="total"></a>+16 + 50 x 40,164 | total | `2,008,216 bytes` | V | The decoded entry length; a reader that finds another length rejects the whole image. |

## Behavior

- V: the store copies the 50-slot cache into the manager image and queues this entry with version 14; the PNG write is requested separately on the request object, in the same frame step.
- V: the load first fills the image with the empty-slot pattern and then requests the entry, so a missing or rejected payload leaves 50 empty slots rather than stale ones.
- V: the payload handler checks the CRC and, for version 14, the exact size; on a mismatch it zeroes the image and returns an error (there is no per-slot recovery).
- V: a delete is a slot rewrite (the slot is filled with 0xFF) followed by the same whole-image store; no separate record is removed.
- V: `classic.png` uses the same entry and the same image, but its list maps index 0 to the 51st auto slot g_SaveAutoSlot and shifts the cache by one.
- V: every backup slot read from real save files was reproduced as a 40,164-byte slot byte for byte, which is the practical check of this layout.

## Notes

The slot's own fields (summary, sprite records, unit table, item and errand tables) are described in UnitSaveRecord and in the save schema records; this page covers the entry envelope and the anchors needed to place a slot.

## Open questions

? the spare bytes at the end of a slot image (0xFF in a used slot).
