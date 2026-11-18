# SpritePieceTemplates

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407BAC78`
- **Rows:** 221 rows of 24 bytes
- **Keyed by:** map object set 0..12 x piece 0..16
- **Read by:** [WorldMap_InitLocations](../functions/WorldMap_InitLocations.md)
- **Row layout:** [SpritePieceTemplate](../structs/SpritePieceTemplate.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite piece templates of the world-map objects: thirteen sets of 17 pieces. Verdict: designer-data.

## Behavior

- V: WorldMap_InitLocations: 13 groups of 17 records (0x198 bytes per group) are converted into the live sprite piece list
- V: nested loop of 13 x 17 with a stride of 24 bytes (0x198 per set); the live copy at 0x140D49AFC is built from it

## Notes

Our names. Tags: V loop and stride, I meaning.

## Open questions

- ?: which map object each of the 13 sets is
