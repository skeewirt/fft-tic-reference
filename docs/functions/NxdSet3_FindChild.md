# NxdSet3_FindChild

- **Address:** `0x1403D3940`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdChild3 *NxdSet3_FindChild(NxdSet3 *set, unsigned int key2)`
- **Callers:** NxdTable_GetEntryByKeysIndex3, NxdTable_GetLeafCount3, sub_1400D5934 and the five set-scanning readers
- **Callees:** NxdSet3_SearchChild

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the child record of a key2 inside one triple-keyed set: binary search over the set's 20-byte children (offset +4 relative to the set record, count +8).

## Behavior

- V: child i at set + int(set +4) + 20 * i, key2 at +0, compared unsigned; middle first, then NxdSet3_SearchChild.
- V: returns the child or null.

## State touched

- Calls: [NxdSet3_SearchChild](NxdSet3_SearchChild.md)
- Reads: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Referenced by

- Called by: [NxdTable_GetEntryByKeysIndex3](NxdTable_GetEntryByKeysIndex3.md), [NxdTable_GetLeafCount3](NxdTable_GetLeafCount3.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md)

## Notes

A child holds its leaves at +12 (offset relative to the child) / +16 (count); retail children also store the leaf offset at +4 with count 0 at +8.

## Open questions

None recorded.
