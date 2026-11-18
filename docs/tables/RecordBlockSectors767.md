# RecordBlockSectors767

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FA200`
- **Rows:** 115 rows of 4 bytes
- **Keyed by:** block index 0..113
- **Read by:** [PackedBlock767_Load](../functions/PackedBlock767_Load.md)
- **Row layout:** [BlockSectorStart](../structs/BlockSectorStart.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sector starts of 114 blocks of 16 sectors (32 KiB) of a second packed file; block 112 is empty. Verdict: pointer-table.

## Behavior

- V: the 115 values are sector numbers, not pointers; the reader refuses an index whose next row would be 115
- V: PackedBlock767_Load (0x14034370C): start = table[i], length = table[i+1] - table[i]; the index is refused when i + 1 is 0x73 or more
- V: values are 0, 16, 32 ... 1792, 1792, 1808; reader bounds i + 1 < 0x73 (115 entries)

## Notes

Our names. Tags: V.

## Open questions

- ?: what the blocks hold (image data of fixed size)
