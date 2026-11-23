# EffectSequence_SpawnGroup4PerUnit

- **Address:** `0x14031510C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_SpawnGroup4PerUnit(void)`
- **Callers:** EffectSequence_Run (slot 15 of the effect sequence handler table (0x140682F30))
- **Callees:** EffectObject_Alloc, EffectObject_InitMotion, EffectObject_Step, EffectObject_Free

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 15 handler: plays up to two sprites of effect sprite group 4 for a unit, with the state kept in a small table indexed by the entry's byte +2.

## Behavior

- V: the working state is an 8-byte record in an array at unk_14186B050 indexed by the entry byte +2: dword +0 live sprite count, word +4 end counter, bytes +6 and +7 the two sprite slots.
- V: state 1 clears that record's first qword, clears the entry's frame counter (+12), sets the state to 2 and returns 1.
- V: state 2: while the frame counter is at least the group 4 record's byte +2 and below its byte +3, it spawns up to the record's spawn count (byte +42) sprites into the two slots (free slot via EffectObject_Alloc, setup by EffectObject_InitMotion, word +4 of the sprite fixed at 31439), stopping when two are live.
- V: states 2 and 3 then check both slots every frame and free a sprite whose animation ended (EffectObject_Step returns 0, EffectObject_Free frees it). The three renderer globals are saved, set to fixed values and restored around the check.
- V: adds 1 to the frame counter; when the live count is 0 and the frame counter is above the record's byte +2 it adds 1 to the end counter (word +4 of the record). It returns whether that counter was not 1 beforehand; states other than 1, 2 and 3 return 0.
- I: indexing by the entry byte +2 lets several entries (one per unit) keep separate live counts; the owner of that byte was not read.

## State touched

- Calls: [EffectObject_Alloc](EffectObject_Alloc.md), [EffectObject_InitMotion](EffectObject_InitMotion.md), [EffectObject_Step](EffectObject_Step.md), [EffectObject_Free](EffectObject_Free.md)

## Notes

Name is ours. Group 4 is 46 * 4 bytes into EffectSpriteSpawnRecords.

## Open questions

?: which game effect uses kind 15; who sets state 3.
