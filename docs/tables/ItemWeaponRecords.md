# ItemWeaponRecords

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x14080F690`
- **Rows:** 128 records of 8 bytes (ids 0..0x7F)
- **Keyed by:** item id (kind 0)
- **Read by:** [sub_1402B8C74](../functions/sub_1402B8C74.md)
- **Row layout:** [ItemWeaponRecord](../structs/ItemWeaponRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Weapon sub-records of the first 128 items; two more in ItemWeaponRecordsHigh.

## Behavior

- V: the next sub-table follows without padding at +0x400.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
