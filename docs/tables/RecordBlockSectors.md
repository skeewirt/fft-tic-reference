# RecordBlockSectors

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x140684CD0`
- **Rows:** 93 rows of 4 bytes
- **Keyed by:** block index (byte 9 of the record-offset event command)
- **Read by:** [PackedBlock766_Load](../functions/PackedBlock766_Load.md)
- **Row layout:** [BlockSectorStart](../structs/BlockSectorStart.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sector start of each block of a packed data file that event commands load. Verdict: pointer-table.

## Behavior

- V: the 93 values are sector numbers, not pointers (0, 5, 10 ... 427); the dword behind them is not a sector and belongs to another object
- V: the reader takes block i as the sectors table[i] .. table[i + 1], so the last row only ends the previous block
- V: PackedBlock766_Load (0x1403436C0): start = table[i], length = table[i+1] - table[i] sectors, then starts the asynchronous sector read into the block buffer
- V: sub_140341788: uses this address only as the end bound of the road pointer table that precedes it
- V: monotonic run from 0 (+5 per block for the first 34 blocks, then 4 or 5) to 427 at index 92; entry 93 is a non-sector value; the read length is length x 2048 (shift 11)

## Notes

Our names. Tags: V reader and arithmetic, I extent 93 (monotonic run), I what the blocks hold.

## Open questions

- ?: what the 92 blocks hold (images and sprite data parsed with TimImage_Parse: I)
