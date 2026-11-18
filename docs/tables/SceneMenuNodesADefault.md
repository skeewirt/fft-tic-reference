# SceneMenuNodesADefault

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F2E80`
- **Rows:** 7 rows of 88 bytes
- **Keyed by:** menu node number
- **Read by:** [SceneState_Reset](../functions/SceneState_Reset.md)
- **Row layout:** [LegacyMenuNode](../structs/LegacyMenuNode.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Seven legacy menu nodes of the scene menus, first group, default language. Verdict: designer-data.

## Behavior

- V: SceneState_Reset stores a pointer to each of the seven nodes into consecutive chara render manager slots
- V: language 0 uses this array, every other language the default array

## Notes

Our names. Tags: V stride and count, I fields.

## Open questions

None recorded.
