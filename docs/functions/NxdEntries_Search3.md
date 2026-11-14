# NxdEntries_Search3

- **Address:** `0x1403D43C0`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdEntry *NxdEntries_Search3(NxdEntry *entries, uint64 lo, uint64 hi, const unsigned int keys[3])`
- **Callers:** NxdTable_GetEntryByKeys3 (and itself)
- **Callees:** NxdEntries_Search3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binary search of bound 16-byte entries by (key1, key2, key3), recursive on the half that can hold the keys.

## Behavior

- V: an entry of kind below 3 is skipped upward; otherwise the three dwords at its pointer are compared with the keys in order (unsigned); all three equal returns the entry.

## Referenced by

- Called by: [NxdTable_GetEntryByKeys3](NxdTable_GetEntryByKeys3.md)

## Open questions

None recorded.
