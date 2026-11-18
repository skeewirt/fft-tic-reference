# UnitPanel_SetSignalList

- **Address:** `0x14010A284`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void UnitPanel_SetSignalList(__int64 panel, _BYTE *list, int count)`
- **Callers:** UnitPanel_FillEffectLine
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns a status list (ids, bit 0x80 = removed) into the panel's list of BattleSignal ids.

## Behavior

- V: clears the count at panel +66216, then for each entry looks up UIStatusEffect (NXD table 57) row (id & 0x7F) + 1.
- V: an entry is kept when the row's field +20 is non-zero, its field +24 is not 59, and BattleSignal (table 214) has a row for field +24; it stores field +24 | (entry & 0x80) at panel +66176 + count and advances the count.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [UnitPanel_FillEffectLine](UnitPanel_FillEffectLine.md)
- Observed behaviours: [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md)

## Notes

Name is ours. The same UIStatusEffect fields (+20, +24) are what a status needs for its label over a hit unit.

## Open questions

None recorded.
