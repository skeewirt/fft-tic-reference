# ScriptedActorPresets

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x14068B800`
- **Rows:** 6 rows of 8 bytes
- **Keyed by:** preset slot 0..5, then a null pointer
- **Read by:** [ScenePresetOverrides_Apply](../functions/ScenePresetOverrides_Apply.md)
- **Row layout:** [ScriptedActorPresetsRow](../structs/ScriptedActorPresetsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scripted unit presets of one scene: a null-terminated list of 6 record pointers copied into the sprite palette and pose tables. Verdict: designer-data.

## Behavior

- V: the loop ends at the null pointer after 6 entries; sibling lists exist for scene ids 22, 27, 30 and 47
- V: ScenePresetOverrides_Apply (0x140348038): reads the list of the current scene; this list (0x14068B800) is chosen for scene id 50; other ids use sibling lists at 0x14068B7A0 / 0x14068B850 / 0x14068B8A0 / 0x14068B920 and a default list

## Notes

Our names. Tags: V reader, ? meaning.

## Open questions

- ?: what the preset slots are in the game (slot numbers 113..115 are above the normal unit slots)
- ?: what scene id 50 is
