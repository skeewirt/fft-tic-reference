# EffectSequence_SpawnGroup5Rising

- **Address:** `0x140314FD4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_SpawnGroup5Rising(void)`
- **Callers:** EffectSequence_Run (slot 13 of the effect sequence handler table (0x140682F30))
- **Callees:** EffectSprites_Spawn, EffectGroup_UpdateChildren

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind handler: plays the sprites of effect sprite group 5 for the length of that group's frame window, moving its start offset by 3 every frame.

## Behavior

- V: state 1 clears the entry's dword at +48 (the live sprite count and the end counter at +50) and the frame counter (+12), sets the state (+8) to 2 and returns 1; it also sets word_1408F2722 (a word of the group's parameter block) to -8.
- V: state 2 calls EffectSprites_Spawn(5, 11) (group 5 of EffectSpriteSpawnRecords); state 3 skips the spawn and runs only the common step below.
- V: after that call, state 2 lowers word_1408F2722 by 3 (state 3 does not).
- I: word_1408F2722 sits inside the group 5 record's parameter bytes (+5..+41), so each frame's new sprites start 3 units further along that offset; the axis is unread.
- V: common step: calls EffectGroup_UpdateChildren(5) (frees the entry's sprites of that group whose animation has ended and lowers the live count), then adds 1 to the frame counter; when the live count (+48) is 0 and the frame counter is above the group record's byte +2, it adds 1 to the end counter (+50).
- V: returns 0 (entry retired) when the end counter was already 1 before this frame, otherwise 1; states other than 1, 2 and 3 return 0.
- V: around its per-frame work (states 2 and 3) it saves three renderer globals (qword_143C51D70, dword_143C51D4C, dword_143C51D78) into spare slots, loads fixed values into them and puts the saved values back before it returns.
- I: nothing in this function sets state 3; the entry's owner (not read) must do it.

## State touched

- Calls: [EffectSprites_Spawn](EffectSprites_Spawn.md), [EffectGroup_UpdateChildren](EffectGroup_UpdateChildren.md)

## Notes

Name is ours (the group number is the first argument of EffectSprites_Spawn).

## Open questions

?: which game effect uses this kind; the meaning of the second argument (11) of EffectSprites_Spawn, stored plus 31424 in each new sprite record (word +4).
