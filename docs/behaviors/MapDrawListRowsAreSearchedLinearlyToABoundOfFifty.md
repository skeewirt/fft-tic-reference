# MapDrawListRowsAreSearchedLinearlyToABoundOfFifty

- **Kind:** observed behaviour
- **Scope:** engine (battle map draw lists)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapDrawLists_Load](../functions/MapDrawLists_Load.md), [Map_LoadBattleData](../functions/Map_LoadBattleData.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

MapDrawLists_Load clears two 513-byte bitsets, then searches the 50 rows of the draw-list table for the row whose 16-bit map id equals the loaded map and sets, for each 0xFFFF-terminated list the row points at, the bit of every listed draw-record index. A map with no row leaves both bitsets empty.

## Behavior

- V: rows are 24 bytes: map id (16 bits) at +0, six bytes of zero, a pointer to the first list at +8 and to the second at +16; the loop adds 24 bytes per step and stops after 50 rows.
- V: the bound is a compare of the row counter with an 8-bit immediate (value 50); it is the only thing that ends the search when no row matches, and an immediate of this form holds at most 127.
- V: a row whose id equals the map is followed through both pointers without a null test, so a matching row with a null list pointer reads address 0; a zero row (id 0) therefore answers for map 0 if the bound reaches it.
- V: the first pointer's list fills the bitset at 0x142FF84A0 and the second's the bitset at 0x142FF8290; each bit index is the list entry taken as a 16-bit number, so entries run to 4,103 at most in 513 bytes.
- I: the 78 stock maps without a row draw everything the classic renderer draws by default; the lists name the draw records that are treated specially.
- V: the list with only the terminator exists in the data pool (it is the second list of map 127's row).

## Notes

Ids 2..127 appear in the 50 stock rows (map 127 last).

## Open questions

None recorded.
