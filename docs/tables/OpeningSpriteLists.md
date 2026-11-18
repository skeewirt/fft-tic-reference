# OpeningSpriteLists

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407BEF20`
- **Rows:** 152 rows of 8 bytes
- **Keyed by:** language set x list index
- **Read by:** [Opening_LoadMessageSprites](../functions/Opening_LoadMessageSprites.md), [SpriteAnim_Step](../functions/SpriteAnim_Step.md)
- **Row layout:** [OpeningSpriteListsRow](../structs/OpeningSpriteListsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per-language pointer sets of the opening sprite cell lists: four sets of 12 pointers, then four sets of 26. Verdict: pointer-table.

## Behavior

- V: 152 valid pointers, none null: four sets of 12 (language 0, 2, 3, other in address order) then four sets of 26 (language 3, 0, other, 2)
- V: 0x4C0 bytes = 4 x 12 x 8 + 4 x 26 x 8 = 152 pointers; each reader chooses its set by the text language
- V: Opening_LoadMessageSprites (0x14037DB9C): picks one of four 12-pointer sets (language 0 at +0x00, language 2 at +0x60, language 3 at +0xC0, other at +0x120) for the opening message sprites
- V: SpriteAnim_Step (0x14038EDD4): picks one of four 26-pointer sets (language 3 at +0x180, 0 at +0x250, other at +0x320, 2 at +0x3F0) as the cell lists of the animation frames

## Notes

Our names. Tags: V layout, V language choice.

## Open questions

- ?: contents of the cell lists
