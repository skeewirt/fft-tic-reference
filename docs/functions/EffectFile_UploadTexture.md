# EffectFile_UploadTexture

- **Address:** `0x1402741E0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectFile_UploadTexture(void)`
- **Callers:** sub_140319DA4 (state 2)
- **Callees:** sub_1402F7594, sub_14025FA60, sub_14025FCDC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Registers the two palettes and copies the picture stored at the end of the loaded effect file into the 1024 by 512 video page.

## Behavior

- V: the texture section is the file base plus the header dword at +36; the pointer is saved in qword_1411A3840.
- V: the first 512 bytes of that section go to the palette manager as bank 12 and the next 512 as bank 13 (sub_1402F7594 with mode 0).
- V: at section + 1024 a 24-bit byte count and, in the fourth byte, a flag: flag non-zero = 128 halfwords wide, else 64 halfwords wide; the height is count / 256 or count / 128 respectively; the picture data starts at section + 1028.
- V: the rectangle is placed at x = 384, y = 0 of the page and copied by VramPage_CopyRect.
- V: when the current effect number is 71 it then clears one more small rectangle of the page (sub_14025FCDC).
- V (data): the Potion file (effect 260) ends exactly at section + 1028 + 32768, a picture 64 halfwords by 256 rows.

## State touched

- Calls: [sub_1402F7594](sub_1402F7594.md)

## Notes

Name is ours. The picture is 8 bits per pixel against the palettes (I: from the 128 byte row for 64 halfwords).

## Open questions

? the exact rectangle cleared for effect 71.
