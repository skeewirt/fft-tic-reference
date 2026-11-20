# Poach_GiveResult

- **Address:** `0x14030AB70`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Poach_GiveResult(...)`
- **Callers:** the Poach action resolver
- **Callees:** sub_1400D6FB0, sub_140284684, sub_1400EC5F4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives the result of a Poach action: an item, or gil when the stock is full, and sends the poach notification.

## Behavior

- V: runs only when not simulating and action block +18 bit 0x20 is set.
- V: picks the poach id from the acting unit's Job row (table 46) by Rng_Percent(256, 31), which is true when 256 * rand15 / 0x8000 >= 31 (225 of 256 draws): true -> Job +0x24 (column poach_item), false -> Job +0x28 (column poach_item_rare, about 12 %). The id is a PoachItem row (table 236).
- V: when the id is above 96 or its held count is below 99 it adds the item (sub_1400D6FB0); otherwise it gives PoachItem row +0x28 / 2 gil (sub_140284684, sub_1400EC5F4) and flags the gil message.
- V: then it sends BattleActionPoachNotification.

## State touched

- Calls: [sub_1400D6FB0](sub_1400D6FB0.md)

## Referenced by

- Observed behaviours: [PoachResultFromJob](../behaviors/PoachResultFromJob.md)

## Notes

The constant 0x8000 in the roll rule belongs to the callee Rng_Percent (256 * rand15 / 0x8000 >= 31).

## Open questions

None recorded.
