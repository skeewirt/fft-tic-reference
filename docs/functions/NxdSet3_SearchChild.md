# NxdSet3_SearchChild

- **Address:** `0x1403D422C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdChild3 *NxdSet3_SearchChild(NxdSet3 *set, uint64 lo, uint64 hi, unsigned int key2)`
- **Callers:** NxdSet3_FindChild
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The halving loop of NxdSet3_FindChild over a set's children.

## Behavior

- V: as NxdSets_Search3, the records at set + int(set +4).

## Referenced by

- Called by: [NxdSet3_FindChild](NxdSet3_FindChild.md)

## Open questions

None recorded.
