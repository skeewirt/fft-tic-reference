# PoolRecordKeepsItsSpriteAcrossTheReset

- **Kind:** observed behaviour
- **Scope:** engine (battle sprite loading)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [LookPool_ResetForBattleLoad](../functions/LookPool_ResetForBattleLoad.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [LookPool_ClaimForSprite](../functions/LookPool_ClaimForSprite.md), [sub_140210AF0](../functions/sub_140210AF0.md), [g_LookPool](../globals/g_LookPool.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A look pool record keeps the sprite it holds (byte +1) after LookPool_ResetForBattleLoad, and the load pass skips the classic file of a queued sprite that any record's +1 already names; only the battle setup clears +1 of every record.

## Behavior

- V: LookPool_ResetForBattleLoad sets byte +0 of each record to 0 and leaves +1 and the data.
- V: CharaPalette_ReloadForShape's pass 2 compares the queue word with byte +1 of all 15 records (claimed or not) and, on a hit, skips the classic file read for that entry.
- V: LookPool_ClaimForSprite returns the first record whose +1 equals the sprite before it looks for a free one, so a reset record is reused for the same sprite.
- V: the battle setup sub_140210AF0 sets +1 of all 15 records to 0 (0x140210BF9) before the resume restore.
- I: so in stock a sprite number always names the same files, and a reused record's data stay valid.

## Open questions

None recorded.
