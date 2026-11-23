# EffectSprites_Spawn

- **Address:** `0x140313210`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char EffectSprites_Spawn(int group, short x)`
- **Callers:** eight sequence kind handlers (sub_140313E10, sub_140314A74, sub_140314BA4, sub_140314CC8, sub_140314EA4, sub_140314FD4, sub_1403159EC, sub_140316160)
- **Callees:** sprite setup routine, free sprite slot allocator

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the sprites of one effect sprite group when the effect is inside the group's frame window.

## Behavior

- V: the record of the group is EffectSpriteSpawnRecords (46 bytes per group); it spawns only while the effect's frame word lies in the window of bytes +2 / +3 and its live count is below byte +4.
- V: creates up to the count at +42 sprites: takes a free sprite slot, sets up the sprite from the record with the sprite setup routine, marks it active (0x80) and increments the live count.
- V: the sprite definition pointer comes from a list indexed by byte +0 of the record.

## Referenced by

- Called by: [EffectSequence_SpawnGroup10WithCue](EffectSequence_SpawnGroup10WithCue.md), [EffectSequence_SpawnGroup11](EffectSequence_SpawnGroup11.md), [EffectSequence_SpawnGroup15](EffectSequence_SpawnGroup15.md), [EffectSequence_SpawnGroup16](EffectSequence_SpawnGroup16.md), [EffectSequence_SpawnGroup5Rising](EffectSequence_SpawnGroup5Rising.md), [EffectSequence_SpawnGroup6](EffectSequence_SpawnGroup6.md), [EffectSequence_SpawnGroup7AtTile](EffectSequence_SpawnGroup7AtTile.md), [EffectSequence_SpawnGroup8WithCue](EffectSequence_SpawnGroup8WithCue.md)
- Reads tables: [EffectSpriteSpawnRecords](../tables/EffectSpriteSpawnRecords.md)

## Notes

Name is ours. A second spawner, sub_1403138DC, reads the same records.

## Open questions

None recorded.
