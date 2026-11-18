# g_SceneTaskSlots

- **Kind:** global
- **Address:** `0x14114B150`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[1512]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Nine scene-task data records of 0xA8 bytes, parsed from u16 token streams during the battle map setup and captured in a kind-1 snapshot.

## Behavior

- V: nine fill calls, slots 0 and 2..8, slot 1 with an unresolved index.

## Referenced by

- Described by tables: [SceneTaskSlots](../tables/SceneTaskSlots.md)
- Written by: [MapBlock_ApplyLayerCommand](../functions/MapBlock_ApplyLayerCommand.md), [MapBlock_RunCommand](../functions/MapBlock_RunCommand.md)

## Open questions

None recorded.
