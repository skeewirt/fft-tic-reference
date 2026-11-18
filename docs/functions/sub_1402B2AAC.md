# sub_1402B2AAC

- **Address:** `0x1402B2AAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void sub_1402B2AAC(int mode)`
- **Callers:** sub_1402B2FA4, sub_1402B32D4
- **Callees:** allocation helpers, sub_1403D2004, sub_1403D21F0, sub_1403D2358, sub_1402F3A04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the classic UI atlas bundle once per process from five game textures, including the classic item icon sheet.

## Behavior

- V: returns immediately when a process-wide guard byte is already set.
- V: allocates a 0x8800-byte buffer and a 0x20-byte object.
- V: loads the five textures the classic UI needs into one buffer, two of them at known offsets: the map title texture at zero, the
  item sheet at 0xA80.
- V: the item sheet source is fftpack/tex/item/item_01.tex.
- V: calls a helper twice with the buffer and with the buffer's upper half, each time with a name string.
- I: the two calls register the two loaded textures by name, because the helper takes a name and a buffer and no other data.
- V: calls a post-process routine on the whole buffer.
- V: increments a counter byte after a successful build.
- I: the three frame textures are loaded into the remaining space between the known offsets, because they are referenced by the same
  function but their destinations were not followed.
- V: two direct callers, one passing mode 1.
- I: the item sheet supplies the 16 by 16 tiles that the classic item-icon setter indexes, because the loader is paired with that
  setter's page constants.
- ?: who frees the buffer and the object at shutdown.

## Referenced by

- Reads tables: [ItemScreenPalette](../tables/ItemScreenPalette.md)

## Notes

- V: whole body read (0x404 is the body size). The repo also holds the matching item CLUT file, 512 bytes, in the extracted pack.

## Open questions

- ?: the buffer's lifetime and the meaning of the mode argument.
