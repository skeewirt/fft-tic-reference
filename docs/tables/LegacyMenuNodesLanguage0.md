# LegacyMenuNodesLanguage0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data, written at run time)
- **Address:** `0x140801370`
- **Rows:** 63 rows of 88 bytes
- **Keyed by:** menu node id
- **Row layout:** [LegacyMenuNode](../structs/LegacyMenuNode.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Legacy battle / scene menu tree, language 0: 63 nodes of 88 bytes; mutable at run time. Verdict: designer-data.

## Behavior

- V: 0x15A8 = 63 x 88 bytes; four language copies 0x140801370 / 0x140802920 / 0x140803ED0 / 0x140805480
- V: SceneTasks_Init: picks the language's node array as the live menu tree (qword_140D40950)
- V: sub_1402346D0, sub_140233B24, sub_1402037A0, sub_1402361FC, BattleMsg_Dispatch: index nodes by id x 88

## Notes

Our names. Tags: V stride, I fields.

## Open questions

- ?: full node field list
