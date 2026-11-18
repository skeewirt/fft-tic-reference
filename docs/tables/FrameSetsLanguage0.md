# FrameSetsLanguage0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406935E0`
- **Rows:** 142 rows of 8 bytes
- **Keyed by:** frame set id 0..141
- **Read by:** [UiAnim_DrawFrame](../functions/UiAnim_DrawFrame.md)
- **Row layout:** [FrameSetPointer](../structs/FrameSetPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite frame sets of the widget animations, language 0 variant. Verdict: pointer-table.

## Behavior

- V: the four language tables (this one, FrameSetsLanguage2, FrameSetsLanguage3 and FrameSetsDefault) differ in 86 of 142 pointers in every pair; the two not yet recorded are the language 3 table at 0x1406942D0 and the default table at 0x140694740
- V: UiAnim_DrawFrame: picks the language's table (language 0 here, 2 at 0x140693E60, 3 at 0x1406942D0, others at 0x140694740) and draws the pieces of the set the current animation step names
- V: reader indexes with a 16-bit id taken from the animation step list; the four language tables are 142 entries each (0x470 bytes apart); the animation step list table follows this one

## Notes

Our names. Tags: V layout, I count 142 (spacing between the four tables).

## Open questions

- ?: meaning of the two header dwords of a frame set
