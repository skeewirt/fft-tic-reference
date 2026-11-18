# WorldRoute_Search

- **Address:** `0x1402471FC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void WorldRoute_Search(int from, int to)`
- **Callers:** sub_140247E8C, itself
- **Callees:** EventVar_Read, sub_14033FE00, sub_140340C2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recursive shortest-route search over the open world-map roads; keeps the best road list.

## Behavior

- V: walks the 51 roads of the road table (0x140684980); a road is usable when event variable 556 + road id is set and it is not already on the current path.
- V: follows a road from either end (bit 8 of the stored entry = travelled from its second location to its first) and adds the road's length to the running cost.
- V: a path that reaches the target with fewer roads, or as many roads and a lower cost, replaces the kept route (up to 16 roads).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [sub_14033FE00](sub_14033FE00.md)

## Referenced by

- Reads tables: [WorldMapRoads](../tables/WorldMapRoads.md)

## Open questions

None recorded.
