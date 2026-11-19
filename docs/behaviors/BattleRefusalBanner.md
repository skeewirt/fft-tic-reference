# BattleRefusalBanner

- **Kind:** observed behaviour
- **Scope:** engine (battle messages)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [CMesId_IsErrorBanner](../functions/CMesId_IsErrorBanner.md), [ErrorBanner_Show](../functions/ErrorBanner_Show.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle refusal messages (C_Mes_Id keys 2001..2037, 18000, 18001) are shown as the timed red banner, not as a message box.

## Behavior

- V: the C_Mes_Id_Sample error_banner byte decides: when set, ErrorBanner_Show plays the 'timer' and 'Error' states and the callers play UI sound cue 0x6A; the normal message paths are skipped.
- M: 21 of 1734 rows have the byte; each is a refusal such as 'Select a tile within movement range.' or 'Cannot target an ally.'.

## Open questions

None recorded.
