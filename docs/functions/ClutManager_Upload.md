# ClutManager_Upload

- **Address:** `0x1402F7964`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void ClutManager_Upload(void)`
- **Callers:** sub_140210AF0, sub_1403044EC, sub_14030476C
- **Callees:** sub_14025FA60, sub_14025FE14

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the palette manager's final image into the emulated video memory when it changed.

## Behavior

- V: when the manager's second dirty dword is set it calls sub_14025FE14 for the rectangle x 0, y 494, 256 x 14 with the arguments 0 and 480, and clears the dword.
- V: when the first dirty dword is set it calls sub_14025FA60 with the same rectangle and word_140C73B70 (the final image: 14 rows of 256 colours), then stores 0 in the first dword and 1 in the second.

## Referenced by

- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The name is ours (IDB: sub_1402F7964). I: sub_14025FA60 is the emulated LoadImage (it has dozens of callers that hand it a rectangle and pixels) and the target is g_SaveYoxPage, the 1024 x 512 word video memory.

## Open questions

? what sub_14025FE14 does with the same rectangle (I: a copy inside the video memory, by its arguments).
