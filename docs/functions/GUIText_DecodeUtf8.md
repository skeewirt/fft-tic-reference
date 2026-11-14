# GUIText_DecodeUtf8

- **Address:** `0x1403D8510`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned __int8 *GUIText_DecodeUtf8(unsigned __int8 *p, int *outCp)`
- **Callers:** GUITextNode_Layout
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decodes one UTF-8 sequence (up to the old 6-byte form) into a code point and returns the pointer after it; the text layout's character reader.

## Behavior

- V: lead < 0x80: 1 byte. lead < 0xE0 (including the stray continuation range 0x80..0xBF) is treated as a 2-byte lead (cp = (lead & 0x1F) << 6 | (b1 & 0x3F)). 0xE0..0xEF: 3 bytes; 0xF0..0xF7: 4; 0xF8..0xFB: 5; 0xFC..0xFD: 6 bytes; 0xFE / 0xFF: stores the lead byte itself and advances 1.
- V: no validation of continuation bytes and no overlong / surrogate check (each continuation is masked with 0x3F).

## Notes

The name is ours (IDB: sub_1403D8510). The layout state pointers (+8 current, +16 next) are advanced with a separate decoder sub_1400796D0 in GUITextNode_HandleTag / PlaceGlyph; whether the two decoders differ was not compared.

## Open questions

? difference to sub_1400796D0.
