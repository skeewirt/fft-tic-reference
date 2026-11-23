# CursorUnit_TopPoint

- **Address:** `0x1402643F8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void CursorUnit_TopPoint(void *scene, short *outPoint)`
- **Callers:** sub_1401F16F4, sub_1401F3F70
- **Callees:** sub_14026FEC8, sub_1402641DC, sub_1402642F4, sub_140028B10, Battle_FindUnitNodeAt, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1400D3150

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Projects the point above the unit at the cursor tile: the unit's base plus its shape height along the renderer's direction vector.

## Behavior

- V: takes the unit at the cursor tile (its CharShape id is node +10), reads the CharShape row's height (+0x2C, a signed byte) and adds it to the base point (plus CharaRenderMgr +13556) along the renderer's direction vector (renderer +147472..+147480), then projects the result into the caller's three words.
- I: the direction vector is the camera's up direction.

## State touched

- Calls: [Battle_FindUnitNodeAt](Battle_FindUnitNodeAt.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Name is ours.

## Open questions

None recorded.
