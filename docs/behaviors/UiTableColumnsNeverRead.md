# UiTableColumnsNeverRead

- **Kind:** observed behaviour
- **Scope:** engine (table readers)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [NxdRegistry_Find](../functions/NxdRegistry_Find.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

No code reads the first dword of UIKeyAssign, UIPadDefine, Icon, SystemBonusEntitlement, UIButtonGuide, BattleVoiceGroupRate and the other UI rows read here; the tables DebugMap (78) and DebugFIdSound (89) are never fetched.

## Behavior

- V: every one of the 390 callers of NxdRegistry_Find computes its table id as a constant; none is 78 or 89, and the UITable wrappers have only two callers with a variable id (credit script tables 307 / 308, and table 61).
- V: the unread columns are named in the column list as unknown; the stock rows hold 1 in them on some rows (UIKeyAssign 7 rows, UIPadDefine 21 of 61, UIButtonGuide 20 of 1152).

## Open questions

None recorded.
