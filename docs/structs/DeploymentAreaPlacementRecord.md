# DeploymentAreaPlacementRecord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 12-byte placement record of the deployment areas (the table at 0x1407AE2D0, indexed by the area id that ScenarioSetupRow entry_area / entry_area_2 name; the same id is the first key of EntryArea, nxd 244).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="cell_mask"></a>`0x0` | cell_mask | `uint32` | V | 25-bit mask of the deployment cells of the 5 x 5 grid: sub_1402FF440 (run by Deployment_LoadAreaPlacement) turns bit k into the flag byte of one grid cell at 0x1437A0420, in an order picked by +7 % 16 (four orientations). Stock: 380 of the first 600 rows have 6 or more cells (M). |
| <a id="anchor_x"></a>`0x4` | anchor_x | `uint8` | I | Anchor of the 5 x 5 cell grid, one axis (Deployment_LoadAreaPlacement adds or subtracts the cell offsets around it). |
| <a id="anchor_y"></a>`0x5` | anchor_y | `uint8` | I | Anchor of the cell grid, the other axis. |
| <a id="facing_bit"></a>`0x6` | facing_bit | `uint8` | I | Shifted into the facing bits (bit 7 of the cell's byte +3) of every cell. |
| <a id="orientation"></a>`0x7` | orientation | `uint8` | I | Together with the first byte of the record's tile word, picks one of the four orientations of the grid. |
| <a id="count"></a>`0x8` | count | `int8` | V | The number of party units the area takes. Returned by Deployment_SelectArea; the deployment capacity is the sum over the battle's areas (sub_1401EF0D8), and Deployment_SelectTile refuses a placement once the units standing on the area's cells reach it (the red 'this group is full' banner, which prints the count). Seen live: raised in memory from 5 to 6, the area took a sixth unit and the 'Remaining' counter started at 6. It is not the number of cells (row 554: 9 cells, count 5). |

## Behavior

- V: Deployment_SelectArea and Deployment_LoadAreaPlacement select it by 12 * area id; GridScreen_Task and sub_1402FB4F8 read it too.

## Notes

Detail and evidence: the sheets Deployment_SelectArea and Deployment_LoadAreaPlacement.

## Open questions

? byte +9 (0 on most rows, 0x55 on row 554); the u16 at +10 equals the row number (M); the exact roles of +4 .. +7.
