# ItemAccessoryRecordsHigh

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x140673674`
- **Rows:** 1 record of 2 bytes (id 0x104)
- **Keyed by:** item id - 0x104 (kind 8)
- **Read by:** [sub_1402B8DA0](../functions/sub_1402B8DA0.md)
- **Row layout:** [ItemAccessoryRow](../structs/ItemAccessoryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Accessory sub-record of item 260. It lies at index 41 of the 4-byte run of BattleStatusIconFlagMasks (the slot after its 40 status rows), so the two tables overlap by address.

## Behavior

- V: by address, 0x140673674 is index 41 of the run that BattleStatusIconFlagMasks occupies (42 entries to the next symbol).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: whether the status mask table has 42 entries or the item record lies over its padding
