# BattleSceneWindowTemplatesDefault

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140813660`
- **Rows:** 920 bytes of window records
- **Keyed by:** window slot
- **Row layout:** [SceneWindowTemplateRow](../structs/SceneWindowTemplateRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Window records (rectangles, flags, pointers) of the battle scene screen, default for other languages. Verdict: designer-data.

## Behavior

- V: Battle_InitScene selects this block by the text language record (0 selects the lang0 block)

## Notes

Our names. Tags: V reader, I layout.

## Open questions

- ?: exact record size and field layout
