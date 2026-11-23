# WorldRoads_BuildMarkers

- **Address:** `0x140341788`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void WorldRoads_BuildMarkers(void *screen)`
- **Callers:** sub_140246A14, sub_140246C04, sub_1402CD448
- **Callees:** EventVar_Read, Math_RotateTranslateVector, sub_140340494

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the drawable marker points of every open road on the world map.

## Behavior

- V: loops over the 48 entries of the road point list table (0x140684B50), from event variable 556: a road is drawn only when its event variable is set.
- V: for each way point id in the road's list converts it to a screen position with Math_RotateTranslateVector and marks whether it lies inside the visible area; every four points it emits one marker segment with sub_140340494.
- V: does nothing when a world-map flag (bit 5 of the world state dword) is set.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [Math_RotateTranslateVector](Math_RotateTranslateVector.md)

## Referenced by

- Reads tables: [RoadPointLists](../tables/RoadPointLists.md)

## Notes

Read in full.

## Open questions

?: the visible area bounds used for the test.
