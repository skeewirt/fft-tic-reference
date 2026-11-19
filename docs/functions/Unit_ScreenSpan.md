# Unit_ScreenSpan

- **Address:** `0x1402219F0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Unit_ScreenSpan(void *unit, short *out)`
- **Callers:** sub_140221C00, sub_1402D9490
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, sub_140028B10, NxdEntry_GetRow, sub_140261F60, sub_1400D3460

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the screen x and the y of a unit's base and of its base plus its shape height.

## Behavior

- V: reads the CharShape row's height (+0x2C) and projects the unit's base and base + height.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours.

## Open questions

None recorded.
