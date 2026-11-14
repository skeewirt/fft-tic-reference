# Utf8_DecodeUnit

- **Address:** `0x1403BF9D4`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `__int64 Utf8_DecodeUnit(unsigned char *src, unsigned short *out)`
- **Callers:** 0x1403a9474, 0x1403ba3a4, 0x1403dd780
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decodes one UTF-8 sequence to a 16-bit code unit and returns the number of bytes used.

## Behavior

- V: sequence length from the lead byte (< 0xC0 / 0xE0 / 0xF0 / 0xF8 / 0xFC limits give 1..6); the value = lead & mask followed by 6 bits per continuation byte.
- V: values above 0xFFFF are replaced by 9632 (0x25A0, a black square); the low 16 bits are stored to *out.

## Notes

The name is ours (IDB: sub_1403BF9D4). No validation of continuation bytes; characters beyond the BMP become U+25A0.

## Open questions

None recorded.
