# NxdSets_Search2

- **Address:** `0x1403D419C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdSet2 *NxdSets_Search2(NxdSetTable *sets, uint64 lo, uint64 hi, unsigned int key1)`
- **Callers:** NxdSets_Find2
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The halving loop of NxdSets_Find2 over [lo, hi) of the 12-byte set records.

## Behavior

- V: mid = lo + (hi - lo) / 2; equal key returns the record; key >= record key continues above mid, else below; an empty range returns null.

## Referenced by

- Called by: [NxdSets_Find2](NxdSets_Find2.md)

## Open questions

None recorded.
