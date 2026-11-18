# WeaponHitSoundCuesRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of BattleWeaponHitSoundCues.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="hit_cue_plain"></a>`0x0` | hit_cue_plain | `uint8[32]` | V | row 0: sound cue number + 1 played for a hit with that weapon type |
| <a id="hit_cue_alt"></a>`0x20` | hit_cue_alt | `uint8[32]` | I | row 1: cue number + 1 for the other mode (single target branch) |
| <a id="hit_cue_unarmed_target"></a>`0x40` | hit_cue_unarmed_target | `uint8[32]` | I | row 2: cue number + 1 when the struck unit's flag byte +447 is zero |

## Referenced by

- Described by tables: [BattleWeaponHitSoundCues](../tables/BattleWeaponHitSoundCues.md)

## Open questions

None recorded.
