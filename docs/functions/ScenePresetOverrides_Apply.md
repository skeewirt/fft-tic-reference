# ScenePresetOverrides_Apply

- **Address:** `0x140348038`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `long ScenePresetOverrides_Apply(void)`
- **Callers:** sub_1402516BC (map loader)
- **Callees:** sub_140347FE8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the sprite palette and pose entries named by the current scene's preset list into the live sprite tables.

## Behavior

- V: the list is chosen by the scene id (22, 27, 30, 47 and 50 each have one, a default list otherwise); each list is null terminated.
- V: per record: a variant 0..2 selects one of three groups of the 144-byte job-sprite row, then two copies write the sprite tables for the record's unit slot and set a terminator.

## Referenced by

- Reads tables: [ScriptedActorPresets](../tables/ScriptedActorPresets.md)

## Open questions

?: what the scenes' presets are in the game.
