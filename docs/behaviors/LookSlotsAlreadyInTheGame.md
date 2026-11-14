# LookSlotsAlreadyInTheGame

- **Kind:** observed behaviour
- **Scope:** engine (battle sprite loading)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [LookQueue_Add](../functions/LookQueue_Add.md), [LookPool_ClaimForSprite](../functions/LookPool_ClaimForSprite.md), [LookPool_ResetForBattleLoad](../functions/LookPool_ResetForBattleLoad.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [SceneUnit_SyncSpriteFromPool](../functions/SceneUnit_SyncSpriteFromPool.md), [sub_14026EB74](../functions/sub_14026EB74.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle loader already assigns small per-battle slots to looks: a 16-entry queue, 15 look pool records shared by equal sprite numbers, 16 scene-unit records and 10 HD sheet entries.

## Behavior

- V: LookPool_ClaimForSprite returns the pool index of an equal sprite number or claims the first free record; an index of 15 or more is refused, so at most 15 distinct looks are loaded in one battle (the queue itself holds 16 entries, the unit table 21).
- V: sub_14026EB74 stores the pool index at scene unit +9 and the sprite low byte at +0xA; SceneUnit_SyncSpriteFromPool copies pool +1 back into +0xA when the unit's pool record changes.
- V: HD sheet entries are kept per pool index for 0 to 9 (dword table at 0x142E7FE6C + 4 * (20 + pool) and the dword at 0x142E7FEE0); sub_14026EB74 writes the entry from the HD table at creation and sub_140260CF0 fills it at the first draw when it is -1.
- I: pool records 10 to 14 get the sheet slot 17, which only pool 9 fills; what they draw in HD is not seen.
- V: the battle snapshot copies the queue, the whole pool and the HD slot dwords.

## Open questions

? what pool indexes 10 to 14 draw in HD (live check).
