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
| <a id="anchor_x"></a>`0x4` | anchor_x | `uint8` | I | Anchor of the 5 x 5 cell grid, one axis (Deployment_LoadAreaPlacement adds or subtracts the cell offsets around it). |
| <a id="anchor_y"></a>`0x5` | anchor_y | `uint8` | I | Anchor of the cell grid, the other axis. |
| <a id="facing_bit"></a>`0x6` | facing_bit | `uint8` | I | Shifted into the facing bits (bit 7 of the cell's byte +3) of every cell. |
| <a id="orientation"></a>`0x7` | orientation | `uint8` | I | Together with the first byte of the record's tile word, picks one of the four orientations of the grid. |
| <a id="count"></a>`0x8` | count | `int8` | V | Returned by Deployment_SelectArea; DeploymentGrid_CommenceCheck takes it as the area's size (I: the units the area takes). |

## Behavior

- V: Deployment_SelectArea and Deployment_LoadAreaPlacement select it by 12 * area id; GridScreen_Task and sub_1402FB4F8 read it too.

## Notes

Detail and evidence: the sheets Deployment_SelectArea and Deployment_LoadAreaPlacement.

## Open questions

? bytes +0 .. +3 and +9 .. +11; the exact roles of +4 .. +7.
