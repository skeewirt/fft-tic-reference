# TexHeader_ValidateCopy

- **Address:** `0x1403BAA14`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TexHeader_ValidateCopy(void *dst, unsigned int n, const unsigned char *hdr, const unsigned char *hdr8, const void *src, unsigned int srcSize)`
- **Callers:** TextureResourceHandle_StreamStep (sub_1403BB25C, two call sites)
- **Callees:** memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Checks that a TEX header table fits and copies it: returns 0 on success, 2 for a wrong version, 3 for an entry count of 0 or above 255, 4 when the table is larger than the data available.

## Behavior

- V: need = 32 * n; when hdr[5] bit 0x01: if (hdr8[12] & 0xF) == 3 need += 16 * u16(hdr8 + 2); else if hdr[5] bit 0x10 and (hdr8[12] & 0xF) != 0: need += 24 * u16(hdr8 + 2) (same rule as TexHeader_TableSize).
- V: hdr[4] != 4 returns 2; (n - 1) > 254 returns 3; need <= srcSize: memmove(dst, src, need or 32 * n) when dst != src (the shorter size when neither flag bit 0x11 is set), return 0; else returns 4.
- V (call shape): the Hex-Rays text shows only three arguments at the call sites (dst, src, size); the disassembly passes dst in rcx, n = first byte of the entry in edx, hdr in r8, hdr + 8 in r9, src and the size on the stack.

## Referenced by

- Called by: [TextureResourceHandle_StreamStep](TextureResourceHandle_StreamStep.md)

## Notes

Name proposed (IDB: sub_1403BAA14).

## Open questions

?
