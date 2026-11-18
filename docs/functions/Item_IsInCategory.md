# Item_IsInCategory

- **Address:** `0x1402B8EE8`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Item_IsInCategory(unsigned short id, int category)`
- **Callers:** `Battle_ResolveAction`, `Item_MenuCategory`, `PartyUnit_FillFromWorkRecord`, `sub_1400FB9F0`, `sub_140227CF8`, `sub_140284998`, and 13 more (19 functions, 56 call sites)
- **Callees:** `Item_FindCategoryIndex`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests whether an item belongs to a given menu category, accepting the matching category or one exactly seven apart.

## Behavior

- V: It resolves the item's category through Item_FindCategoryIndex and compares it with the requested category.
- V: An exact match returns 1 immediately.
- V: Otherwise it takes the absolute difference and returns -1 when that is exactly seven, and 0 for every other
  difference; the value is all-ones, not 1, so the test is non-zero rather than true.
- V: It keeps the category in r9 across the Item_FindCategoryIndex call, which is safe because that callee leaves r9
  untouched.
- V: It has nineteen direct callers over fifty-six call sites, which makes it one of the most reused item predicates in the
  game.
- I: Categories c and c + 7 are the same kind in the low and the high id space (0 and 7 are the weapon kinds 0 and 5).
- I: The seven-apart form is a table geometry fact, not a width; it survives an id-space change only if the category table
  keeps that layout.

## State touched

- Calls: [Item_FindCategoryIndex](Item_FindCategoryIndex.md)

## Referenced by

- Called by: [Battle_ResolveAction](Battle_ResolveAction.md), [ClassicItemListPage_Run](ClassicItemListPage_Run.md), [Item_GetMenuField](Item_GetMenuField.md), [Party_ReturnHandItems](Party_ReturnHandItems.md), [sub_1400FB9F0](sub_1400FB9F0.md), [sub_1402875A4](sub_1402875A4.md), [sub_140287D9C](sub_140287D9C.md), [sub_140288788](sub_140288788.md), [sub_1402890C0](sub_1402890C0.md), [sub_14028B180](sub_14028B180.md), [sub_14028B354](sub_14028B354.md), [sub_1403099B0](sub_1403099B0.md), [sub_140396D08](sub_140396D08.md)
- Resolves registries: [ItemCategories](../registries/ItemCategories.md)

## Open questions

None recorded.
