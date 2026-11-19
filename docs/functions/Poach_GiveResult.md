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
- V: picks the common (job table 46 row +0x24) or the rare (+0x28) poach id by Rng_Percent(256, 31).
- V: when the id is above 96 or its held count is below 99 it adds the item (sub_1400D6FB0); otherwise it gives PoachItem row +0x28 / 2 gil (sub_140284684, sub_1400EC5F4) and flags the gil message.
- V: then it sends BattleActionPoachNotification.

## State touched

- Calls: [sub_1400D6FB0](sub_1400D6FB0.md)

## Open questions

? the two job-table columns that hold the common and the rare poach ids.
