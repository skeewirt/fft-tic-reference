# PackEntry_Inflate

- **Address:** `0x1403D1ED8`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `__int64 PackEntry_Inflate(InflateState *st, char *out, PackEntryHeader *entry, int size)`
- **Callers:** PackFile_ReadEntry, sub_1402181EC
- **Callees:** memmove, sub_140411260 (inflateInit), sub_1404113B0 (inflate), sub_140412BB0 (inflateEnd), sub_140412D20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads one pack entry: a 16-byte header, then either stored bytes or a zlib stream.

## Behavior

- V: header +4 bit 1 set = zlib (inflate 1.2.11) of the data after the 16-byte header into out in chunks; otherwise memmove of header +8 bytes from entry + 16. Returns the byte count (or -1).

## Referenced by

- Called by: [PackFile_ReadEntry](PackFile_ReadEntry.md), [sub_1402181EC](sub_1402181EC.md)

## Open questions

None recorded.
