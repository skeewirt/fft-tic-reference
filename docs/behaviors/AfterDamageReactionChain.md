# AfterDamageReactionChain

- **Kind:** observed behaviour
- **Scope:** engine (battle action result)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_ApplyActionResult](../functions/Battle_ApplyActionResult.md), [sub_14030BE18](../functions/sub_14030BE18.md), [sub_14030BE68](../functions/sub_14030BE68.md), [sub_1403095E4](../functions/sub_1403095E4.md), [g_ReactionGateTable](../globals/g_ReactionGateTable.md), [UnitWorkRecord.passive_bits](../structs/UnitWorkRecord.md#passive_bits)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

At the end of Battle_ApplyActionResult the unit held in g_BattleActingUnit is tested for passive reactions in a fixed order; the first one present goes to a Brave-roll helper, and the reaction executor then handles only the ids it has a case for.

## Behavior

- V: the chain runs unless the formula result's type byte (0x1407B0788) is 7 or sub_14030AF88 answers non-zero; then it tests, in order: +0x94 bit 0x80 (id 422), 0x40 (423), 0x20 (424), 0x02 (428), +0x95 bit 0x40 (431), 0x20 (432), 0x10 (433), 0x08 (434, through sub_14030BE68), +0x96 bit 0x40 (439), 0x10 (441); only the first bit found acts.
- V: sub_14030BE18 requires the action block's flag byte +39 bit 7, passes without a roll in a simulation or rolls Rng_Percent on the unit's Brave byte (+0x2B), and stores the reaction id at block word +16 and copies the HP result (block word +6) to word +40.
- V: sub_14030BE68 additionally requires the unit's status byte +0x63 bit 0x01 and only stores the reaction id at word +16.
- V: sub_1403095E4 (run first by Battle_ResolveAction when the battle-state gate is non-zero) refuses ids whose g_ReactionGateTable byte has 1 in its low two bits (returns 0) and handles the cases 422..434, 438, 439, 444 and 446; any other id clears block byte +39 and returns -1.
- I: the compare chain has no case for 435..437 and 440..443 and has cases 444 and 446; the ids 442 and 443 are dropped.

## Notes

In Battle_ResolveAction g_BattleActingUnit is set from the second argument (the target slot of the action being resolved); which record it holds inside Battle_ApplyActionResult was not traced, the chain reads whatever record it holds.

## Open questions

? what the cases 444 and 446 are; which reaction names the ids carry (not read here).
