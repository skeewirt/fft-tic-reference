# BattleSceneWindowColours

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140813A30`
- **Rows:** 6 rows of 20 bytes
- **Keyed by:** slot 0..5
- **Row layout:** [SceneWindowColourRow](../structs/SceneWindowColourRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Corner colours (four per row) of the battle scene window gradients. Verdict: designer-data.

## Behavior

- V: the reader copies four colours with a 20-byte step

## Notes

Our names. Tags: V.

## Open questions

- ?: which slot is which window
