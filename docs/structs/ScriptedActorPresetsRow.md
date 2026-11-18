# ScriptedActorPresetsRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the ScriptedActorPresets table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="record_ptr"></a>`0x0` | record_ptr | `uint64` | V | pointer to a 16-byte record of four dwords |
| <a id="record"></a>`0x8` | record | `bytes[16]` | I | 4 dwords: unit slot (113, 114, ...), copy-table index, row of the 144-byte job-sprite table, variant 0..2 choosing one of three 12-byte groups of that row |

## Referenced by

- Described by tables: [ScriptedActorPresets](../tables/ScriptedActorPresets.md)

## Open questions

None recorded.
