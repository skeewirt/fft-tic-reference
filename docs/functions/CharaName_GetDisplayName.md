# CharaName_GetDisplayName

- **Address:** `0x1401E8B7C`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `const char *CharaName_GetDisplayName(int nameKey, const char *ownName)`
- **Callers:** about 22 callers (party lists, turn panel, battle messages, errand screens, save import)
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1401E8CD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the display name of a name key: the CharaName table's name, or the unit's own stored name string when the row says so.

## Behavior

- V: returns the name of the CharaName row of the key, or the unit's own name string when row byte +0x14 (column own_name) is non-zero and the passed string is not empty (copied with sub_1401E8CD8, length 8 or 16 by the language in g_LanguageInfo).
- V: returns 0 for key 0 or a missing row.
- V: the callers (not this body) pass (save record +0x230, +0xDC) or (work +508, +332); about 22 callers (party lists, turn panel, battle messages, errands, save import).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Open questions

None recorded.
