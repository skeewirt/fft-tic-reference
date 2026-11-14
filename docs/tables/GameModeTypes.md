# GameModeTypes

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 88
- **Keyed by:** battle state
- **Held in:** [g_FastForwardStateTable](../globals/g_FastForwardStateTable.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per game-mode flags. The only use recorded here: a byte at row +16 says whether fast-forward is allowed in a battle state.

## Behavior

- V: the fast-forward state table is filled with 1, then loaded from this table's row byte +16 (see g_FastForwardStateTable).

## Notes

NXD tables are loaded through the shared registry (NxdRegistry_Find by table id) and read with NxdTable_GetRowById or a key lookup; the file format is described by the NXD format records.

## Open questions

None recorded.
