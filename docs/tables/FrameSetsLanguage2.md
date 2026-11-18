# FrameSetsLanguage2

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140693E60`
- **Rows:** 142 rows of 8 bytes
- **Keyed by:** frame set id 0..141
- **Read by:** [UiAnim_DrawFrame](../functions/UiAnim_DrawFrame.md)
- **Row layout:** [FrameSetPointer](../structs/FrameSetPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite frame sets of the widget animations, language 2 variant. Verdict: pointer-table.

## Behavior

- V: UiAnim_DrawFrame: the table of language 2
- V: language switch in the reader: 0 -> 0x1406935E0, 3 -> 0x1406942D0, 2 -> this table, other -> 0x140694740; the 142-entry spacing is 0x470 bytes

## Notes

Our names. Tags: V, I count.

## Open questions

- ?: how the language 2 frame sets differ from the others
