# g_ReactionGateTable

- **Kind:** global
- **Address:** `0x14067F730`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[32]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One byte per reaction id 422..453: the reaction executor refuses (returns 0 at once) an id whose byte has 1 in its low two bits.

## Behavior

- V: sub_1403095E4 indexes it by id - 422. The values are 6 for the ids 422..433, then 42, 41, 41, 41, 6, 6, 45, 41, 41, 6, 14, 16, 14, 16, 16, 16, 16, 16, 16, 25 for 434..453; the low two bits are 1 for the ids 435, 436, 437, 440, 441, 442 and 453.
- V: the byte for id 443 is 6 (the same as the self-targeting reactions 422..433).
- ?: what the other bits of the bytes mean; only the low two bits are tested.

## Referenced by

- Described by tables: [ReactionGates](../tables/ReactionGates.md)
- Observed behaviours: [AfterDamageReactionChain](../behaviors/AfterDamageReactionChain.md)
- Read by: [sub_1403095E4](../functions/sub_1403095E4.md)

## Notes

The table is 32 bytes (the next data starts at 0x14067F750).

## Open questions

? the meaning of the upper bits.
