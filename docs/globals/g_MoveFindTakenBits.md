# g_MoveFindTakenBits

- **Kind:** global
- **Address:** `0x1411A7680`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint8[128]: taken bits of the Move-Find hidden tiles, four per map, two maps per byte, byte = scene variable 51 / 2, bit 0x80 >> (tile slot + 4 x (id & 1)); saved and restored whole; directly followed by g_PoachersDenStock, so a map id of 256 or more would run into it

## Open questions

None recorded.
