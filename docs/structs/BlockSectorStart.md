# BlockSectorStart

- **Kind:** structure
- **Area:** [Resource](../areas/resource.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the sector start tables of the packed UI and event blocks.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="start_sector"></a>`0x0` | start_sector | `uint32` | V | first 2048-byte sector of the block inside the packed file; the block length is the next row minus this one |

## Referenced by

- Described by tables: [RecordBlockSectors](../tables/RecordBlockSectors.md), [RecordBlockSectors767](../tables/RecordBlockSectors767.md)

## Open questions

None recorded.
