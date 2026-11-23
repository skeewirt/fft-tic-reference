# PackedBlock767_Load

- **Address:** `0x14034370C`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int PackedBlock767_Load(int blockIndex)`
- **Callers:** sub_140318BBC, sub_140375538, sub_140375E7C, sub_140376CA8, sub_1403793DC
- **Callees:** sub_140343564, sub_1403434D0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts loading one block of packed data file 767 into its block buffer.

## Behavior

- V: does nothing when the block is already the current one; sets the buffer pointer first.
- V: waits for any read in progress, then (for indexes below 114) takes start = table[index] and length = table[index + 1] - table[index] sectors from the table at 0x1408FA200 and starts the read.

## Referenced by

- Called by: [MenuCtl_Entry28](MenuCtl_Entry28.md), [MenuCtl_Entry43](MenuCtl_Entry43.md), [sub_140375E7C](sub_140375E7C.md)
- Reads tables: [RecordBlockSectors767](../tables/RecordBlockSectors767.md)

## Notes

Read in full (one small function).

## Open questions

?: what the blocks contain.
