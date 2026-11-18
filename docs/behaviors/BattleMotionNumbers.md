# BattleMotionNumbers

- **Kind:** observed behaviour
- **Scope:** engine (battle unit animation choice)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [BattleAnim_SelectMotion](../functions/BattleAnim_SelectMotion.md), [BattleAnim_SelectWeaponMotion](../functions/BattleAnim_SelectWeaponMotion.md), [BattleAnim_StartMotion](../functions/BattleAnim_StartMotion.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle action names its animation by a motion number from two tables (one per ability, one per weapon type); the unit stores motion + 1, and the motion number is the pair index of the classic animation file (front view at twice the number, back view one more).

## Behavior

- V: the ability table (3 bytes an ability, at 0x140672DA0) holds the charge type, the motion number and the battle text number; motion 0 means a plain weapon attack, motion 1 a ranged special that becomes motion 58 when the target is adjacent or on the same tile, and every other value is used as it stands.
- V: the weapon table (3 bytes a weapon animation type, 24 types, at 0x140673890) holds three motion numbers per type; types 19 to 23 hold none.
- V: BattleAnim_StartMotion stores motion + 1 as the unit's animation number (scene object +0x10).
- M (data test, 2026-11-14): animation pointer 2 x motion (front) and 2 x motion + 1 (back) in the classic animation file lands the motions of every weapon type that has any on animations that draw the attack frames (frame numbers 84 and up) and carry the hit-marker opcode, with one exception that carries none (a weapon type whose animations do not mark the hit). Of the 57 distinct motion values in the ability table, 34 were tested: the values from 40 up land on animations that draw action frames; the low values (0, 1, 22, 34, 36) land on single-frame poses and one value (112) on a pointer with no frames. Other offsets (motion, motion + 1, 2 x motion - 26) land on movement poses and unrelated animations; 2 x motion + 2 lands on the next animation of the same group, so the choice of 2 x motion rests on the ordering of the weapon triples (see the next bullet). The code that does this conversion was not located.
- I: the three motions of a weapon type are three variants of one attack in the order high, middle, low of the target's height: the one weapon type read in code (type 12) picks its motion from a signed angle word, the first below -682, the second from -682 to 682, the third above 682.
- I: because the movement tables (CharAnimSeq) only hold animation ids 1 to 73 and the motions used in battle reach 118 (animation 236), the attack and cast animations are read from the classic animation file, not from those tables.

## Notes

The 17 frames past 181 of the robed layout (frames 182 to 198, four pieces each, all with art in every sheet of that layout) are drawn by no classic animation; what draws them is unknown.

## Open questions

? the function that reads the +0x10 number each frame; ? the scene mode values 457 and 292 tested by BattleAnim_StartMotion; ? what draws the robed layout's frames 182 to 198.
