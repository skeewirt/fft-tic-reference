# Party_AnyItemBelow99

- **Address:** `0x1402D6688`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Party_AnyItemBelow99(void)`
- **Callers:** sub_1402D6914 (two calls)
- **Callees:** Item_IsValidId (two sites)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether any item held by the party has reached a high count. It works on a private copy of the inventory counts,
adds the items the party members have equipped, and reports the first id whose total reaches one hundred.

## Behavior

- V: takes no arguments.
- V: copies the 261-byte live inventory count array into a 272-byte stack buffer with fixed 16-byte moves plus a dword and
  a byte.
- V: walks the party unit pointer table at 0x141800F50 for the party count byte; for each member it reads one word at +0x54
  masked to ten bits plus five unmasked words at the start of the record, and increments the copied count for every word
  the validity check accepts (that check also keeps the index inside the 261-entry range).
- V: then scans the copied counts from id 0 to 260 and returns 1 as soon as one of them is 100 (0x64) or more.
- V: returns 0 when the whole scan finds no such count.
- V: the buffer is larger than the copied array (272 bytes for 261), and only the copied range is scanned.
- V: the comparison is an unsigned above-or-equal against 0x64, so the answer is "some count reached one hundred", not
  "some count is below ninety-nine"; the name reads the test backwards.
- I: the routine is a "some stack is full" gate rather than a per-item query.
- ?: which menu or battle decision consumes the answer; the caller was not read.

## State touched

- Calls: [Item_IsValidId](Item_IsValidId.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [sub_1402D6914](sub_1402D6914.md)

## Open questions

None recorded.
