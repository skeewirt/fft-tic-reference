# NxdEntries_Search2

- **Address:** `0x1403D4304`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntry *NxdEntries_Search2(NxdEntry *entries, uint64 lo, uint64 hi, uint64 keys)`
- **Callers:** NxdTable_GetEntryByKeys2
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binary search of bound 16-byte entries by (key1, key2), packed as key1 | key2 << 32.

## Behavior

- V: an entry of kind below 2 compares as keys (0, 0); otherwise its pointer's first two dwords are (key1, key2).
- V: order: key1 unsigned first, then key2 unsigned; an equal qword returns the entry, an empty range null.

## Referenced by

- Called by: [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md)

## Notes

So the file's flat entry table must be sorted by (key1, key2) for every key to be found.

## Open questions

None recorded.
