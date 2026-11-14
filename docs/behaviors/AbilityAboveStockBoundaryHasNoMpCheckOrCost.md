# AbilityAboveStockBoundaryHasNoMpCheckOrCost

- **Kind:** observed behaviour
- **Scope:** engine (action start and preview)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_1402828E4](../functions/sub_1402828E4.md), [sub_14030B1A0](../functions/sub_14030B1A0.md), [g_AbilityMpCost](../globals/g_AbilityMpCost.md), [g_CommandKind](../globals/g_CommandKind.md), [UnitWorkRecord.passive_bits](../structs/UnitWorkRecord.md#passive_bits)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The MP check and payment (sub_1402828E4) and its preview twin (sub_14030B1A0) only look at ids up to 0x16F (367): an ability id above that boundary pays no MP, has no MP check and shows no cost.

## Behavior

- V: sub_1402828E4 reads the unit's command byte (+0x1A1) and ability word (+0x1A2), looks the kind up in g_CommandKind and clears g_AbilityMpCost; a unit with status mask 0x04 at +0x65 or a non-zero sub_14030DD1C answer returns that answer + 6; a Toad unit (+0x63 mask 0x02) returns 5 unless the ability is 0, 367 or 29 (a kind of 10 returns 5 whatever the ability).
- V: an id above 0x16F skips the rest and returns 0; otherwise, for a kind-0 or kind-6 command, the action row's flag byte +5 mask 0x20 together with the unit's +0x62 mask 0x08 returns 2.
- V: for kind 0, a job byte other than 93 and an id up to 0x16F: the cost is action-row byte +13, halved when unit +0x99 has bit 7; it is stored in g_AbilityMpCost; if the unit's MP (+0x34) is below it the function returns 3; otherwise MP is paid unless the simulate mode is 2.
- V: sub_14030B1A0 is the same chain without the payment or the return 3: it only stores the cost.
- V: the equality tests against 367 at 0x14020CB7F (sub_14020CB0C), 0x14026B693 (sub_14026B310), 0x140282960 and 0x14030B202 are the four single-id tests of this boundary.

## Notes

The return codes 2, 3 and 5 are read as values; their consumers were not traced.

## Open questions

? the consumers of the return codes.
