# WorldMapRoads

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140684980`
- **Rows:** 51 rows of 8 bytes
- **Keyed by:** road id 0..50
- **Read by:** [WorldRoute_Search](../functions/WorldRoute_Search.md)
- **Row layout:** [WorldMapRoad](../structs/WorldMapRoad.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 51 world-map roads: their two end locations, travel cost and drawn way points; event variable 556 + n opens road n. Verdict: designer-data.

## Behavior

- V: loop bound 51 and EventVar_Read(n + 556) in sub_1402471FC
- V: sub_1402471FC: recursive shortest-route search over all roads whose event variable 556 + road id is set; stores the road list, bit 8 = travelled from b to a
- V: sub_1402477C8: on arrival, the location reached = +1 or +2 of the last road depending on the direction bit
- V: sub_140341A0C / sub_140341B64: road drawing

## Notes

Our names. Tags: V header, I way points.

## Open questions

- ?: way-point field layout
- ?: location id numbering (battlegrounds are 24..42 in the encounter table)
