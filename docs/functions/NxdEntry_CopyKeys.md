# NxdEntry_CopyKeys

- **Address:** `0x1403D2F90`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `bool NxdEntry_CopyKeys(NxdEntry *entry, unsigned int *out, uint64 n)`
- **Callers:** sub_1400DA5D8, sub_1400DAD58, sub_1400DB384, sub_1400F94DC, sub_14015E0FC (the position of an entry inside its set)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the first n keys of the row an entry points to (the record's leading dwords); false when the entry's kind has fewer than n keys.

## Behavior

- V: kind = qword 0 without bit 63; kind below n returns false; else out[i] = pointer dword i for i < n (none when out is null or n is 0), true.

## Open questions

None recorded.
