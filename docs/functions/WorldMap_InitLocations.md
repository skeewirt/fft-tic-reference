# WorldMap_InitLocations

- **Address:** `0x14033EC0C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void WorldMap_InitLocations(void)`
- **Callers:** sub_140246078 (the world and town loop)
- **Callees:** PackedBlock766_Load, EventVar_Read, EventVar_Write, sub_140340FD0, sub_140340B94, sub_1403413C4, sub_140341094, sub_1403426F8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets up the world-map screen: the sprite piece list, the location markers and the road markers.

## Behavior

- V: converts 13 groups of 17 piece templates (0x1407BAC78, 24 bytes each) into the live sprite piece list.
- V: for each of 48 locations (index 47 skipped) builds a 52-byte marker record from the location offset table (0x1406933A0, 8 bytes each); the first 43 become active markers.
- V: reads event variables 556 + n for the 51 roads and event variables 84, 49, 46 and 47 for the screen state.
- V: calls the packed block loader with a block index and several set-up helpers (a per-location helper in the marker loop and four more after it).

## State touched

- Calls: [PackedBlock766_Load](PackedBlock766_Load.md), [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md)

## Referenced by

- Reads tables: [LocationMarkerOffsets](../tables/LocationMarkerOffsets.md), [SpritePieceTemplates](../tables/SpritePieceTemplates.md)

## Notes

Head only: the first half (piece, marker and road set-up); the rest of the function is not read.

## Open questions

?: the second half of the function.
