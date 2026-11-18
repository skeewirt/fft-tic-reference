# EquipmentOrderListPointers

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x14067FA90`
- **Rows:** 4 rows of 8 bytes
- **Keyed by:** equipment group 0..3
- **Read by:** [sub_1403368C0](../functions/sub_1403368C0.md), [sub_140336B88](../functions/sub_140336B88.md), [sub_140286070](../functions/sub_140286070.md)
- **Row layout:** [EquipmentOrderListPointer](../structs/EquipmentOrderListPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointers to the four saved equipment order lists; the next eleven pointers of the run belong to other lists. Verdict: pointer-table.

## Behavior

- V: the first four pointers address runtime buffers in the zero-initialised part of the image (their spacing gives the list capacities 141, 30 and 38 entries); entries 4..14 address constant lists in the initialised data
- V: ItemOrder equipment synchroniser sub_140286070: groups at or above 4 return at once, so only four entries are read
- V: sub_1403368C0 and sub_140336B88: pass table[group] to the order filter or fill it after a sort
- V: all three readers guard the index below 4; the first four targets are runtime buffers full of 0xFFFF words (equipment order lists of 141, 30, 38 and further entries by target spacing); entries 4..14 point at constant lists in the executable that the sort-field table at 0x14067FAB0 also names

## Notes

Our names. Tags: V first four entries, I entries 4..14 are sort field lists.

## Open questions

- ?: the length of the fourth list
