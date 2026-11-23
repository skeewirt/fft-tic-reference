# EffectSequence_SpawnGroup7AtTile

- **Address:** `0x140314CC8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_SpawnGroup7AtTile(void)`
- **Callers:** EffectSequence_Run (slot 9 of the effect sequence handler table (0x140682F30))
- **Callees:** EffectSprites_Spawn, EffectGroup_UpdateChildren, SceneObject_FindBySlot, BattleMap_GetTileRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind handler: plays the sprites of effect sprite group 7 for the length of that group's frame window at a ground offset worked out from the unit's tile.

## Behavior

- V: state 1 clears the entry's dword at +48 (the live sprite count and the end counter at +50) and the frame counter (+12), sets the state (+8) to 2 and returns 1.
- V: state 2 calls EffectSprites_Spawn(7, 11) after looking up the scene object of the unit slot at entry +32 (SceneObject_FindBySlot), passing its position divided by 28 (x and y) and a height byte to BattleMap_GetTileRecord, and storing a value derived from the result into word_1408F277E (-word - 12 * (byte + (byte >> 5))) inside the group's parameter block (group 7 of EffectSpriteSpawnRecords); state 3 skips the spawn and runs only the common step below.
- I: BattleMap_GetTileRecord is a terrain query for the tile (unread); the stored word shifts the sprites to the ground height there.
- V: common step: calls EffectGroup_UpdateChildren(7) (frees the entry's sprites of that group whose animation has ended and lowers the live count), then adds 1 to the frame counter; when the live count (+48) is 0 and the frame counter is above the group record's byte +2, it adds 1 to the end counter (+50).
- V: returns 0 (entry retired) when the end counter was already 1 before this frame, otherwise 1; states other than 1, 2 and 3 return 0.
- V: around its per-frame work (states 2 and 3) it saves three renderer globals (qword_143C51D70, dword_143C51D4C, dword_143C51D78) into spare slots, loads fixed values into them and puts the saved values back before it returns.
- I: nothing in this function sets state 3; the entry's owner (not read) must do it.

## State touched

- Calls: [EffectSprites_Spawn](EffectSprites_Spawn.md), [EffectGroup_UpdateChildren](EffectGroup_UpdateChildren.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [BattleMap_GetTileRecord](BattleMap_GetTileRecord.md)

## Notes

Name is ours (the group number is the first argument of EffectSprites_Spawn).

## Open questions

?: which game effect uses this kind; the meaning of the second argument (11) of EffectSprites_Spawn, stored plus 31424 in each new sprite record (word +4).
