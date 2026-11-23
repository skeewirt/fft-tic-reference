# EffectSequence_ProjectileFlight

- **Address:** `0x14031342C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectSequence_ProjectileFlight(void)`
- **Callers:** EffectSequence_Run (slot 1 of the effect sequence handler table (0x140682F30))
- **Callees:** atan2f, sub_140312424, Math_RotateTranslateVector, sub_1400D2FA4, sub_140310CE4, SceneObject_FindBySlot, sub_1401FAEE8, sub_1403109E8, sub_1402746E8, Math_BuildRotationMatrix, sub_1402F3A04, ResourcePool_AllocBlocks

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 1 handler: flies a model along a heading from a start point towards an end point, following the ground height, and ends the flight on arrival.

## Behavior

- V: state 1 takes the heading from atan2 of the difference of two stored endpoint pairs (words at dword_14186D778 / 77C and 780 / 784), converts it to a 4096-per-turn angle, and sets a pitch from atan2 of a stored value against 4096. It also sets the step length from the cosine table and a value read through sub_1402746E8, copies a step count (dword_14186D770) into word_1437A20D8, converts the heading to a position (Math_BuildRotationMatrix), sets the state to 2 and returns 1.
- V: state 1 also frees any buffer held at entry +88 (sub_1402F3A04), allocates a new 0x1910-byte buffer (ResourcePool_AllocBlocks) at +88 and fills it as 2 blocks of 4 records (80 bytes) and 13 records (104 bytes), each with fixed marker values.
- V: state 2 advances a distance counter (dword_1437A1A18) by the step each frame, looks up the ground height at the old distance and at the new distance plus one step (old + 2 steps; sub_140312424, called with the ground-level value dword_14186D774), derives the pitch from atan2 of that height difference over twice the step, takes a third lookup at the new distance for the vertical position, and draws the model with sub_140310CE4 using a word of the table that follows the handler table (0x140682FF0, reached as the word at 0x140682FF2 plus 4 per kind: the second word of the 4-byte row of the entry's effect kind (+4)).
- V: each frame in state 2 it also counts word_1437A20D8 down. The count is decremented; if it was 1 before the decrement, or the vertical position is not negative, the state becomes 3; in the same step, if the entry's sub-kind byte (+33) minus 3 is at most 2 or dword_1437A5C10 is -1, it takes a free sequence entry (sub_1403109E8, result used as an index into the 96-byte entry array at 0x1437A5C40) and fills it as kind 5, effect kind 21, state 1, frame 0.
- V: while the count is 2 and dword_1437A5C10 is not -1 and entry +44 is non-zero, it looks up the scene objects of the unit slots at entry +20 and +32 (SceneObject_FindBySlot) and calls sub_1401FAEE8.
- I: the second scene object is passed as its second argument; the first argument is an unresolved register in the decompile.
- V: state 2 returns 1; state 3 and any other state return 0, so the entry is retired the frame after the flight ends.
- I: the follow-up kind 5 entry is the two-frame hold handler (EffectSequence_HoldTwoFrames), so the flight ends by queueing a short entry of effect kind 21 (the impact); this rests on the slot 5 table entry and the constants written, not on a read of the consumer.
- I: the second endpoint pair is read from globals the effect setup fills; their writers were not read.

## State touched

- Calls: [Math_RotateTranslateVector](Math_RotateTranslateVector.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [Math_BuildRotationMatrix](Math_BuildRotationMatrix.md), [ResourcePool_AllocBlocks](ResourcePool_AllocBlocks.md)

## Notes

Name is ours. The flight follows the ground height with a heading and a pitch, so it suits a shot such as an arrow or bolt (I).

## Open questions

?: what sub_140312424 returns exactly (read here as the ground height at a distance); what the 0x1910-byte buffer at +88 holds.
