# WorldMapRoad

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the WorldMapRoads table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="road_ptr"></a>`0x0` | road_ptr | `pointer` | V | pointer to the road record (in .data 0x1407B58A0..0x1407B69D0) |
| <a id="point_count"></a>`0x0` | point_count | `uint8` | I | number of 12-byte way points that follow (6 in road 0; record = 4 + 12 x n, padded) |
| <a id="location_a"></a>`0x1` | location_a | `uint8` | V | location id at one end |
| <a id="location_b"></a>`0x2` | location_b | `uint8` | V | location id at the other end |
| <a id="length"></a>`0x3` | length | `uint8` | V | travel cost added to the path length by the route search |
| <a id="way_point[n]"></a>`0x4` | way_point[n] | `bytes[12]` | ? | way points of the drawn road: two signed coordinates and four more words |

## Referenced by

- Described by tables: [WorldMapRoads](../tables/WorldMapRoads.md)

## Open questions

None recorded.
