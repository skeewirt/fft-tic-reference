# NxdSets_Search3

- **Address:** `0x1403D41E4`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdSet3 *NxdSets_Search3(NxdSetTable *sets, uint64 lo, uint64 hi, unsigned int key1)`
- **Callers:** NxdSets_Find3
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The halving loop of NxdSets_Find3 over 20-byte set records.

## Behavior

- V: as NxdSets_Search2 with a 20-byte stride.

## Referenced by

- Called by: [NxdSets_Find3](NxdSets_Find3.md)

## Open questions

None recorded.
