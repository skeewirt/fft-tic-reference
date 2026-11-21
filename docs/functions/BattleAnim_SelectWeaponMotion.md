# BattleAnim_SelectWeaponMotion

- **Address:** `0x140269790`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 BattleAnim_SelectWeaponMotion(int64_t sceneObject, int64_t targetObject)`
- **Callers:** BattleAnim_SelectMotion
- **Callees:** BattleAnim_StartMotion

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the motion of a plain weapon attack from the attacker's weapon animation type and, for some types, from how high the target stands, then starts it.

## Behavior

- V: the weapon animation type is the byte at scene object +0x152; each type has three consecutive motion numbers in the weapon motion table at 0x140673890 (3 bytes a type, 24 types); the middle one is the default when there is no target.
- V: when the sprite byte at +0x0A plus 101 is 3 or less, the motion is 62 whatever the weapon.
- V: for type 12 with a target, a signed angle word (0x1437A5C14, wrapped to -2048..2047) picks the motion: below -682 gives 83, from -682 to 682 gives 84, above 682 gives 85.
- V (table): types 1 to 9 share one triple (64, 65, 66); type 0 has 61, 62, 63; types 11 and 12 share 83, 84, 85; types 19 to 23 have none (0).
- I: the three numbers of a triple are variants of one attack in the order of the target's height (the type 12 branch above picks the first, second or third by an angle word, and the middle one is the default); types with a single repeated number have one variant.
- ?: the path for the other types with a target (it reads a byte at +0x1C0 of the target's record) was not read.

## State touched

- Calls: [BattleAnim_StartMotion](BattleAnim_StartMotion.md)

## Referenced by

- Called by: [BattleAnim_SelectMotion](BattleAnim_SelectMotion.md)
- Observed behaviours: [BattleMotionNumbers](../behaviors/BattleMotionNumbers.md), [WeaponPoseFollowsTheEquipCategory](../behaviors/WeaponPoseFollowsTheEquipCategory.md)

## Notes

The IDB already carried this name. Read: the table lookup and the type 12 branch; the rest of the target path only in outline.

## Open questions

- ? the target-dependent choice for types other than 12.
