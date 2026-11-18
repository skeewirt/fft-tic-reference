# EffectSpriteSpawnRecords

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1408F2630`
- **Rows:** 12 rows of 46 bytes
- **Keyed by:** effect sprite group 0..11
- **Read by:** [EffectSprites_Spawn](../functions/EffectSprites_Spawn.md)
- **Row layout:** [EffectSpriteSpawnRecordsRow](../structs/EffectSpriteSpawnRecordsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One record per effect sprite group: sprite definition index, frame window, live limit, parameter block and the number of sprites to create. Verdict: designer-data.

## Behavior

- V: EffectSprites_Spawn tests the effect frame against bytes +2 and +3, the live count against +4 and creates +42 sprites
- V: the sprite definition index (+0) selects a pointer from the effect sprite definition list

## Notes

Our names. Tags: V layout of the used fields, ? parameter block, I count 12.

## Open questions

- ?: the 37-byte parameter block
- ?: whether the object holds a 13th record (the bytes say yes: rows 12..16 at 0x1408F2858..0x1408F293E have the same shape as rows 0..11 and row 17 does not, so the object probably holds 17 rows; the bound is the highest group number the 8 callers of EffectSprites_Spawn pass, not settled)
