# SpriteAnimScripts

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140699730`
- **Rows:** 18 rows of 8 bytes
- **Keyed by:** animation id 0..17
- **Read by:** [SpriteAnim_Step](../functions/SpriteAnim_Step.md)
- **Row layout:** [SpriteAnimScriptsRow](../structs/SpriteAnimScriptsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Eighteen sprite animation frame lists of the opening / title sprites: each frame is a cell group index and a number of ticks. Verdict: pointer-table.

## Behavior

- V: 18 valid pointers; the next two words are not pointers
- V: 18 pointers; the reader increments a tick counter and compares it with the frame's high half-word; 0xFFFF ends a one-shot list
- V: SpriteAnim_Step (0x14038EDD4): advances the tick counter, steps to the next frame (wraps at the count), then draws the cells of the frame through the per-language cell list

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: the frame list contents are not listed here
