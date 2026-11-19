# BattleAnim_StartMotion

- **Address:** `0x140268E04`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 BattleAnim_StartMotion(int motion, int16_t direction, int64_t sceneObject)`
- **Callers:** BattleAnim_SelectMotion, BattleAnim_SelectWeaponMotion
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a motion on a battle unit's scene object: stores the animation number and the facing value the unit's animation will use.

## Behavior

- V: the animation number stored is `motion + 1`, at scene object +0x10 (16-bit); the direction argument goes to +0x7C (16-bit) and bit 0x20 of the byte at +0x8F is set. This is the "+1" the callers' motion numbers carry.
- V: when the global scene mode word (dword at 0x140782A94) is 457, the store happens at once with no other test.
- V: otherwise, when that word is 292 and an event script is running, the store happens only if the unit's current animation number (+0x12) already equals `motion + 1`; in every other case it happens.
- V: before a store, a non-zero byte at +0x156 is cleared and the animation number at +0x10 is zeroed.
- ?: what the mode values 457 and 292 are called.

## Referenced by

- Called by: [BattleAnim_SelectMotion](BattleAnim_SelectMotion.md), [BattleAnim_SelectWeaponMotion](BattleAnim_SelectWeaponMotion.md), [EventControl_ApplyCarry](EventControl_ApplyCarry.md)
- Observed behaviours: [BattleMotionNumbers](../behaviors/BattleMotionNumbers.md)

## Notes

The name is ours (IDB: sub_140268E04). Read in full (a short function).

## Open questions

- ? names of the scene mode values; ? which code reads the +0x10 animation number each frame and turns it into the classic animation pointer (not located; see UnitMovementAnimationTables and BattleMotionNumbers).
