# AbilityAuxFlagBits

- **Kind:** registry
- **Area:** [Ability data](../areas/ability-data.md)
- **Values stored in:** [AbilityTypes](AbilityTypes.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The meaning of the bits of exe.ability.aux flags3 (byte +3) and flags4 (u32 at +4) as named here: flags3 holds the ability type in bits 0..4 and three flags in bits 5..7, flags4 the AI behaviour flags, one bit each.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="learnonhit"></a>5 | `LearnOnHit` | `flags3 bit 5` | V | Bit 5 is the bit the learn routine tests before the learn-percent roll (sub_14030CD08). |
| <a id="displayabilityname"></a>6 | `DisplayAbilityName` | `flags3 bit 6` | V | Set on 412 of 512 stock abilities. |
| <a id="dontlearnwithjp"></a>7 | `DontLearnWithJP` | `flags3 bit 7` | V | The sign bit the menu code reads from flags3 (sub_1402867BC, sub_14028A474); two stock abilities. |
| <a id="targetallies"></a>0 | `TargetAllies` | `flags4 bit 0` | V | Bit 0 is read by target resolution (sub_14038ABA4). |
| <a id="targetenemies"></a>1 | `TargetEnemies` | `flags4 bit 1` | V | Solved over all 512 rows. |
| <a id="unequip"></a>2 | `Unequip` | `flags4 bit 2` | V | Solved. |
| <a id="stats"></a>3 | `Stats` | `flags4 bit 3` | V | Solved. |
| <a id="addstatus"></a>4 | `AddStatus` | `flags4 bit 4` | V | Solved. |
| <a id="cancelstatus"></a>5 | `CancelStatus` | `flags4 bit 5` | V | Solved. |
| <a id="mp"></a>6 | `MP` | `flags4 bit 6` | V | Solved. |
| <a id="hp"></a>7 | `HP` | `flags4 bit 7` | V | Solved. |
| <a id="silence"></a>8 | `Silence` | `flags4 bit 8` | V | Solved. |
| <a id="evadeable"></a>9 | `Evadeable` | `flags4 bit 9` | V | Solved. |
| <a id="affectedbyfaith"></a>10 | `AffectedByFaith` | `flags4 bit 10` | V | Solved. |
| <a id="randomhits"></a>11 | `RandomHits` | `flags4 bit 11` | V | Solved. |
| <a id="checkct_target"></a>12 | `CheckCT_Target` | `flags4 bit 12` | V | Solved. |
| <a id="undeadreverse"></a>13 | `UndeadReverse` | `flags4 bit 13` | V | Solved. |
| <a id="reflectable"></a>14 | `Reflectable` | `flags4 bit 14` | V | Solved. |
| <a id="targetmap"></a>15 | `TargetMap` | `flags4 bit 15` | V | Solved. |
| <a id="physicalattack"></a>16 | `PhysicalAttack` | `flags4 bit 16` | V | Solved. |
| <a id="magicalattack"></a>17 | `MagicalAttack` | `flags4 bit 17` | V | Solved. |
| <a id="ranged3directions"></a>18 | `Ranged3Directions` | `flags4 bit 18` | V | Solved. |
| <a id="melee3directions"></a>19 | `Melee3Directions` | `flags4 bit 19` | V | Solved. |
| <a id="nonspearattack"></a>20 | `NonSpearAttack` | `flags4 bit 20` | V | Solved. |
| <a id="linearattack"></a>21 | `LinearAttack` | `flags4 bit 21` | V | Solved. |
| <a id="stopatobstacle"></a>22 | `StopAtObstacle` | `flags4 bit 22` | V | Solved. |
| <a id="evadewithmotion"></a>24 | `EvadeWithMotion` | `flags4 bit 24` | V | Solved. |
| <a id="onlyhitsenemies"></a>29 | `OnlyHitsEnemies` | `flags4 bit 29` | V | Solved. |
| <a id="onlyhitsalliesorself"></a>30 | `OnlyHitsAlliesOrSelf` | `flags4 bit 30` | V | Solved. |
| <a id="usablebyai"></a>31 | `UsableByAI` | `flags4 bit 31` | V | Solved; the sign bit read by sub_14038BF34. |

## Behavior

- V: each name was solved to exactly one bit over all 512 stock rows (no exception), and no flags4 bit of the low 24 or of 24..31 stays unexplained.
- V: aux_jp_classic is the ability's JP cost and aux_learn_percent its chance to learn, on all 512 rows.

## Referenced by

- Indexed by registries: [AbilityTypes](AbilityTypes.md)

## Notes

The meanings beyond what the readers listed above test are I (names, not decoded effects).

## Open questions

None recorded.
