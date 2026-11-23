# EffectObject_Step

- **Address:** `0x140387FB4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool __fastcall EffectObject_Step(int index, unsigned __int16 arg)`
- **Callers:** EffectFlash_Start (two calls), EffectGroup_UpdateChildren, EffectSequence_HitFlashSprites (two calls), EffectSequence_SpawnGroup4PerUnit, EffectSequence_SpawnGroup3Cluster, EffectSequence_SpawnGroup14Ring; also a data reference at 0x143D3F61C
- **Callees:** sub_140380FB8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Advances one effect object by a frame: moves it, updates its motion vectors, steps its small frame script, runs a per-frame helper and reports whether it is still alive.

## Behavior

- V: the object is record `index` of `word_14186D7B0` (488 words = 976 bytes each); offsets below are bytes into the record.
- V: adds the dwords at +452, +456, +460 to those at +440, +444, +448, then rewrites the +452..+460 triple from the old values, the signed divisor word at +436, the word at +438 and three globals (`dword_143C51D4C`, `qword_143C51D70`, `dword_143C51D78`) with a 12-bit fixed-point blend, and adds the dwords at +476, +480, +484 to those at +464, +468, +472.
- V: decrements the word at +416; at or below zero it reads the next entry of the u16 list pointed to by the qword at +424 (entry 0 of the list is a count): the entry's high byte goes to byte +411, its low byte becomes the new counter and the index word at +414 advances; when the index reaches the count it is reset to 0 and the script is marked finished.
- V: calls `sub_140380FB8(record, arg)` every frame.
- V: the word at +432: when it is non-negative it is decremented and the function returns whether it is now non-zero; when negative the function returns 1 unless the frame script finished.
- I: +440..+448 is a position and +452..+460 its velocity (rests on the first addition).

## Referenced by

- Called by: [EffectGroup_UpdateChildren](EffectGroup_UpdateChildren.md), [EffectSequence_HitFlashSprites](EffectSequence_HitFlashSprites.md), [EffectSequence_SpawnGroup14Ring](EffectSequence_SpawnGroup14Ring.md), [EffectSequence_SpawnGroup3Cluster](EffectSequence_SpawnGroup3Cluster.md), [EffectSequence_SpawnGroup4PerUnit](EffectSequence_SpawnGroup4PerUnit.md)

## Notes

V: whole body read. The name is ours. I: the three globals are wind/gravity-like constants (rests only on their use as multiplicands).

## Open questions

?: what the three globals are and what the record fields at +436 and +438 hold.
