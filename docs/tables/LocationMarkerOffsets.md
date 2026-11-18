# LocationMarkerOffsets

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x1406933A0`
- **Rows:** 48 rows of 8 bytes
- **Keyed by:** location marker index 0..47
- **Read by:** [WorldMap_InitLocations](../functions/WorldMap_InitLocations.md)
- **Row layout:** [LocationMarker](../structs/LocationMarker.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per world-map location slot, a small position and kind record used to build its marker. Verdict: designer-data.

## Behavior

- V: WorldMap_InitLocations: for each of 48 locations (the first 43 become markers, index 47 is skipped) copies the offsets into a 52-byte marker record
- V: loop of 48 with a 4-word stride; 0x190 bytes (50 rows) to the next table

## Notes

Our names. Tags: V stride and loop, I field meaning.

## Open questions

- ?: what the two byte fields are
- ?: rows 48 and 49 (no reader)
