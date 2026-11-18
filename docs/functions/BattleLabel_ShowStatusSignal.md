# BattleLabel_ShowStatusSignal

- **Address:** `0x14014B87C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 BattleLabel_ShowStatusSignal(__int64 screen, unsigned int slot, unsigned int signal, int removed)`
- **Callers:** ResultLabel_ShowNext
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a styled status label over a unit: the BattleSignal row's title with the icon of the status that names the row.

## Behavior

- V: does nothing for a slot above 20 or when the slot has no label node (screen +144 * slot + 72 / +80).
- V: looks up BattleSignal (NXD table 214) row signal; with a row, it scans UIStatusEffect (NXD table 57) keys 1..1005 for the first row whose field +24 equals the BattleSignal key, and takes that row (key 0 when none) for the icon.
- V: fills the label node's parts by name: TextBuff, Title, IconStatus, Icon; then applies the Show state.
- V (seen live 2026-11-17): a UIStatusEffect row above the stock keys that names a BattleSignal row beyond the stock 71 is found by the scan; the label showed that row's title and the status's own icon.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Appears in flows: [StatusLabelOverAHitUnit](../flows/StatusLabelOverAHitUnit.md)
- Called by: [ResultLabel_ShowNext](ResultLabel_ShowNext.md)
- Observed behaviours: [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md)

## Notes

Name is ours.

## Open questions

? what the removed flag (fourth argument) changes in the drawing.
