# RoadPointLists

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140684B50`
- **Rows:** 48 rows of 8 bytes
- **Keyed by:** road index 0..47 (event variable 556 + n opens the road)
- **Read by:** [WorldRoads_BuildMarkers](../functions/WorldRoads_BuildMarkers.md)
- **Row layout:** [RoadPointListPointer](../structs/RoadPointListPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per road, the list of way points that gets drawn once the road is open. Verdict: pointer-table.

## Behavior

- V: none of the 48 targets lies inside the road records that the road pointer table (0x140684980) leads to: they are separate lists in the data pool before those records (0x1407B3xxx..0x1407B5xxx); the first dword of a list is a point count, then 4-byte (x, y) pairs of signed 16-bit values (I)
- V: WorldRoads_BuildMarkers (0x140341788): for each road whose event variable (556 + n) is set, converts every way point to a screen position and keeps those inside the visible area
- V: sub_140341B64: reads the first word of the list by road index
- V: loop bound is the address of the next table (0x140684CD0): 48 pointers; the loop starts at event variable 556

## Notes

Our names. Tags: V reader and count.

## Open questions

- ?: roads 48..50 have no list (the road table of the event batch has 51 roads)
