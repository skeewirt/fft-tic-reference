# MapAnim_Load

- **Address:** `0x1400C6D64`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MapAnim_Load(void *animSet, unsigned mapId, int source)`
- **Callers:** MapBlock_ApplyLayerCommand
- **Callees:** MapAnim_ReadRows, sub_14006BAA8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the map's anim file when the RefinedBgAnim rows ask for one.

## Behavior

- V: returns 1 without a read when the anim set is already loaded or MapAnim_ReadRows answers 0; no row answers 1, so the file is requested.
- V: the path is the map id in three digits inside the anims folder; a missing file or a failed read returns 1 quietly; the header's tag and its dword at +8 must equal the map id (seen in the stock files), else the buffer is freed.
- V: on success sets the table pointers (32-byte header, then the 1,040-byte block) and runs two precompute steps.

## State touched

- Calls: [MapAnim_ReadRows](MapAnim_ReadRows.md), [sub_14006BAA8](sub_14006BAA8.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Called by: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md)
- Observed behaviours: [AFailedMeshLoadSkipsEveryLaterRendererStep](../behaviors/AFailedMeshLoadSkipsEveryLaterRendererStep.md), [MapMeshAndAnimFilesCarryTheirOwnMapId](../behaviors/MapMeshAndAnimFilesCarryTheirOwnMapId.md)

## Open questions

None recorded.
