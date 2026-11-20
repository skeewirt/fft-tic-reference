# SceneUnits_ReleaseAll

- **Address:** `0x14020DE64`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void SceneUnits_ReleaseAll(void)`
- **Callers:** sub_14020DECC, sub_14020F328, sub_140210AF0 (battle scene code)
- **Callees:** sub_140254A70, SceneUnit_Release

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases every drawn unit (SceneUnit_Release on each node of g_SceneObjectList) after clearing 32 pending dwords and their 8 linked bytes.

## Behavior

- V: calls sub_140254A70; for the 32 dwords from 0x142FF8F00 that are not 0 clears the linked byte (index - 1 below 8) and the dword; clears byte_142FEC52A; then SceneUnit_Release on every scene object.

## State touched

- Calls: [SceneUnit_Release](SceneUnit_Release.md)

## Open questions

None recorded.
