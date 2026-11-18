# FrameSetsDefault

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140694740`
- **Rows:** 142 rows of 8 bytes
- **Keyed by:** frame set id 0..141
- **Read by:** [UiAnim_DrawFrame](../functions/UiAnim_DrawFrame.md)
- **Row layout:** [FrameSetPointer](../structs/FrameSetPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite frame sets of the widget animations, the default (language 1) variant. Verdict: pointer-table.

## Behavior

- V: UiAnim_DrawFrame picks this table for every language that is not 0, 2 or 3
- I: 142 entries (the four language tables are 0x470 bytes apart)

## Notes

Our names. Found beside the table at 0x140693E60; tags V, I count.

## Open questions

None recorded.
