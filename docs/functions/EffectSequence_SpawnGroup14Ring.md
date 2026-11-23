# EffectSequence_SpawnGroup14Ring

- **Address:** `0x140316284`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_SpawnGroup14Ring(void)`
- **Callers:** EffectSequence_Run (slot 22 of the effect sequence handler table (0x140682F30))
- **Callees:** EffectAnchor_GetPoint, SoundCue_Play, EffectObject_Alloc, EffectObject_InitMotion, EffectObject_Step, EffectObject_Free, sub_1402BAAA8, sub_1402BA96C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 22 handler: creates 30 sprites of effect sprite group 14 and moves them in three trailing circles around a point, growing and spinning, then fading them out.

## Behavior

- V: state 1: takes an anchor point from EffectAnchor_GetPoint(0, -1, ...) into the global block at xmmword_14186B0E8 + 8 and lowers its height word by 24; clears the ring sample table; allocates 30 sprite slots into the entry's bytes +52..+81 (word +4 of each sprite fixed at 31436, group 14 record); clears the frame counter (+12) and the fade counter (+50), sets the state to 2, calls SoundCue_Play(0x20) and returns 1.
- V: state 2: while the frame counter is below 24 the circle radius and the spin step follow it (radius = frame, spin step = 3 * frame); while below 8 the brightness is 16 * (frame + 1); the counter is then incremented up to 256. The fade counter is not touched.
- V: state 3: while the fade counter (+50) is at most 60, the radius grows by 1 on every frame whose counter has bit 3 set (8 frames of each 16) and the spin step by 1 each frame; brightness is 4 * (60 - counter); the counter counts up to 61.
- V: each frame it adds the spin step to a spin angle, fills a 10-sample table for each of three phases 1365 apart (a third of the 4096-unit turn) with cos and sin of the angle times the radius, and places every sprite at the anchor plus the sample picked by its slot position and a rotating start index (so the sprites trail one another), calling EffectObject_Step for each.
- V: it sets each sprite's three colour bytes to brightness * a byte of the 10-entry table at 0x14071E7B0 / 128.
- V: returns 1 while the fade counter is below 61; at 61 or more it frees all 30 sprite slots (EffectObject_Free), calls sub_1402BAAA8(32) and, if that returns 0, sub_1402BA96C(33), and returns 0.
- I: nothing in this function moves the entry from state 2 to 3; the owner does it when the effect should fade (the fade counter, not the state 2 frame counter, drives the end).
- I: the two sound calls at the end stop or follow up the cue started with SoundCue_Play(0x20); they were not read.

## State touched

- Calls: [EffectAnchor_GetPoint](EffectAnchor_GetPoint.md), [SoundCue_Play](SoundCue_Play.md), [EffectObject_Alloc](EffectObject_Alloc.md), [EffectObject_InitMotion](EffectObject_InitMotion.md), [EffectObject_Step](EffectObject_Step.md), [EffectObject_Free](EffectObject_Free.md)

## Notes

Name is ours. Group 14 is 46 * 14 bytes into EffectSpriteSpawnRecords (beyond the 12 rows the table record lists).

## Open questions

?: which game effect uses kind 22; what the 10-byte weight table at 0x14071E7B0 holds.
