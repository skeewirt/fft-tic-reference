# MapDrawIndexLists

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140672780`
- **Rows:** 50 rows of 24 bytes
- **Keyed by:** battle map id (key at +0, linear search)
- **Read by:** [MapDrawLists_Load](../functions/MapDrawLists_Load.md)
- **Row layout:** [MapDrawIndexListRecord](../structs/MapDrawIndexListRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle map, two lists of map draw-record indices that the two map draw passes treat specially. Verdict: designer-data.

## Behavior

- V: 50 records x 24 bytes = 0x4B0 to the next symbol; search bound 0x32 in sub_140249CB8
- V: sub_140249CB8: called by the map loader sub_140251584 with the map id; clears both bitsets and sets the listed bits
- V: sub_140346E7C / sub_140346728 (two map draw passes) test the bits for each map draw record that passes their mask test

## Notes

Our names. Tags: V layout, ? meaning.

## Open questions

- ?: what the two passes do with a marked record
- ?: what a draw-record index is (polygon group / map object)
- ?: earlier research read this address as chemist table B; that reading does not fit this layout
