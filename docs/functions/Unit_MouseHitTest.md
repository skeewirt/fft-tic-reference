# Unit_MouseHitTest

- **Address:** `0x1401F6E7C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Unit_MouseHitTest(void *scene, ...)`
- **Callers:** sub_14024A6E8
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1401F8618, sub_14027A46C, sub_1400D425C, cosf, sinf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests the mouse position against the hit areas of the units on the field.

## Behavior

- V: loads the CharShape row's char_mouse_collision key (dword at +0x28) and looks up CharMouseCollision (table 334); the collision row's float +8 (times 0.5) and +0xC / +0x10 size the area tested around the unit's tile.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours; only the collision lookup was read closely.

## Open questions

None recorded.
