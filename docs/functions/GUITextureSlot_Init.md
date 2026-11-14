# GUITextureSlot_Init

- **Address:** `0x1403DAAF4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUITextureSlot_Init(__int64 slots, unsigned int index)`
- **Callers:** sub_1403D9EE0, sub_1403DACD4
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises one texture slot record from its source texture object, with two paths depending on a field of the texture.

## Behavior

- V: entry = *(slots + 80) + 32*index (32-byte entries); tex = entry[0]; rec = entry[2] (pointer at entry+16).
- V: v5 = the dword at tex + 76. If v5 != 0: rec[0..2] qwords = 0, rec+24 = v5, rec+28 = 0, rec+32 word = 0, rec+34 byte = 0 (placeholder / pending state carrying v5).
- V: else: atomic increment of the dword at tex+12 (reference count), rec[0] = tex, rec+8, +16, +24 = 0, rec+32 word = 0, rec+34 = byte(tex+120) & 1 (flag bit).
- V: both paths finish with rec+38 = 0 and rec+36 word = 0.
- V: callers sub_1403D9EE0 (0x1403DA0F1) and sub_1403DACD4 (0x1403DAEC5).

## Notes

Slot-array layout matches GUIFontSlots_GetSlot (base +80, stride 32, record pointer at +16).

## Open questions

? meaning of tex+76 (non-zero looks like an error / pending code; I), tex+120 bit 0, and rec+24/28/32/34/36/38 flags.
