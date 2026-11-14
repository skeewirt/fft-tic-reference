# sub_1402EEC2C

- **Address:** `0x1402EEC2C`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int sub_1402EEC2C(int unit)`
- **Callers:** `sub_1402EEE30`
- **Callees:** `Item_GetRecord`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sums the prices of the five items a party unit has equipped and adds a fixed base amount.

## Behavior

- V: It takes a unit index, finds the party unit record and starts at its first hand word.
- V: It walks exactly five hand words and masks each to ten bits before the record lookup.
- V: Each record price is added to a running total that starts at 1000.
- V: It does not test the presence bit, so an empty slot is looked up as item 0 and contributes that record's price.
- V: It calls two helpers and has one direct caller.
- I: The missing presence test is harmless in stock only because item 0 has no price; it is a latent difference from the other hand-word readers.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [ItemRecord.price](../structs/ItemRecord.md#price)

## Open questions

None recorded.
