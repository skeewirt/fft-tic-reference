# BattleVoice_UsesRows2And3

- **Address:** `0x1401ECEFC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleVoice_UsesRows2And3(void *controller, int line)`
- **Callers:** sub_1401ECC90, sub_1401ED708
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether a voice line may be swapped for rows 2 or 3.

## Behavior

- V: returns the BattleVoice row's replaceable byte (+0x29) as a truth value.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours.

## Open questions

None recorded.
