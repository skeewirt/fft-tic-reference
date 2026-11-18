# EventMenuNodesLanguage0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408DE240`
- **Rows:** 63 rows of 88 bytes
- **Keyed by:** menu node number
- **Read by:** [EventTasks_Init](../functions/EventTasks_Init.md)
- **Row layout:** [LegacyMenuNode](../structs/LegacyMenuNode.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Legacy menu node array of the event task group, language 0 (63 nodes of 88 bytes, mutable at run time). Verdict: designer-data.

## Behavior

- V: sub_1402EA248 stores a pointer to each of the 63 nodes (stride 88) from slot 64 of the chara render manager
- V: four language copies at 0x1408DE240 (0), 0x1408DF7F0 (default), 0x1408E0DA0 (3) and 0x1408E2350 (2)
- V: the first 40 bytes of each node equal the nodes of exe.ui.menu_nodes; the rest differs

## Notes

Our names. Tags: V stride and count, I fields.

## Open questions

None recorded.
