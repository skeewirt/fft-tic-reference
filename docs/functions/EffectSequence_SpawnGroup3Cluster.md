# EffectSequence_SpawnGroup3Cluster

- **Address:** `0x14031536C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_SpawnGroup3Cluster(void)`
- **Callers:** EffectSequence_Run (slot 17 of the effect sequence handler table (0x140682F30))
- **Callees:** EffectObject_Alloc, EffectObject_InitMotion, EffectObject_Step, EffectObject_Free

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 17 handler: spawns sprites of effect sprite group 3 into a shared pool of up to 24 and keeps them until their animations end.

## Behavior

- V: the working state is global: a 24-byte slot array at xmmword_14186B0E8, a live count (the high dword of qword_14186B0E0) and an end counter (its low dword).
- V: state 1 clears all of that and the entry's frame counter (+12), sets the state to 2 and returns 1.
- V: state 2: reads word +6 of the entry as an index into tbl_EffectBlendWeights (at index + 28) and, while the frame counter is at least the group 3 record's byte +2 and below its byte +3, spawns up to the record's spawn count (byte +42) sprites into free slots of the pool (stopping at 24 live), setting word +4 of each sprite to that table value plus 31424.
- V: states 2 and 3 free every pool sprite whose animation has ended (EffectObject_Step returns 0) and lower the live count; the three renderer globals are saved, set to fixed values and restored around this.
- V: adds 1 to the frame counter; when the live count is 0 and the frame counter is above the group record's byte +2 it adds 1 to the end counter; it returns qword_14186B0E0 != 1 (the whole qword: live count in the high dword, end counter in the low dword, read before the add). States other than 1, 2 and 3 return 0.
- I: the pool is shared by all entries of this kind, so only one such effect runs at a time; word +6 acts as a selector (the element mask in EffectFlash_Start), so the sprites likely change with the element.

## State touched

- Calls: [EffectObject_Alloc](EffectObject_Alloc.md), [EffectObject_InitMotion](EffectObject_InitMotion.md), [EffectObject_Step](EffectObject_Step.md), [EffectObject_Free](EffectObject_Free.md)

## Notes

Name is ours. Group 3 is 46 * 3 bytes into EffectSpriteSpawnRecords.

## Open questions

?: whether the selector at +6 is the element mask here; who sets state 3.
