# PortraitCodeIsAByteOnTheSaveRecordPath

- **Kind:** observed behaviour
- **Scope:** engine (party faces)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_14032AB3C](../functions/sub_14032AB3C.md), [PortraitCode_FillCell](../functions/PortraitCode_FillCell.md), [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

On the save-record path a portrait code can only carry 256 distinct faces: the code reader refuses a code with bit 8 or 9 and the cell function returns the low byte.

## Behavior

- V: sub_14032AB3C returns -1 for (code & 0x300) != 0; PortraitCode_FillCell returns (uint8_t)code and puts bits 10 and 11 into the colour.
- M (unicorn, pristine exe): 0x100 -> 0, 0x2FF -> 255, 0x405 -> 5 with colour 9.
- M (unicorn, Unit_GetSpriteSetId's tail 0x1402C07FD..0x1402C0821, codes 0..255): mode word 0 or 2: no code gives -1, 146 codes map (largest face 204), 110 come back as themselves (50 of them 206..255); mode words 1 and 5: the 50 codes 206..255 give -1.
- M: codes above 255 (only if one arrived): mode word 0 returns them raw (256 .. 1299), mode word 1 gives -1.

## Open questions

None recorded.
