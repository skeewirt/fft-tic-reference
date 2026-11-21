# Item_IsValidId

- **Address:** `0x1402B8EBC`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Item_IsValidId(unsigned short id)`
- **Callers:** `Inventory_SnapshotWithEquipped`, `ItemOrder_SyncGroup`, `PartyUnit_FillFromWork`, `PartyUnit_FillFromWorkRecord`, `Party_AnyItemBelow99`, `sub_140226E44`, and 15 more (21 functions, 24 call sites)
- **Callees:** none found

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The stock validity test for an item id: one contiguous low range plus a five-id high range.

## Behavior

- V: It accepts ids 1 through 253 and ids 256 through 260.
- V: Ids 0, 254 and 255 are invalid, which is why 255 can be used as the empty-slot value everywhere else.
- V: The test is two range comparisons on the 16-bit id and returns 1 or 0; it calls nothing.
- V: The ranges are immediates: the id minus 1 is compared with 0xFC, and the id minus 0x100 with 4.
- V: Twenty-one distinct callers use it over twenty-four call sites.
- I: The five-id gap at 254 and 255 is deliberate, not an accident of the table, because the same gap appears in the
  category threshold table.

## Referenced by

- Called by: [ItemOrder_SyncGroup](ItemOrder_SyncGroup.md), [PartyUnit_FillFromWork](PartyUnit_FillFromWork.md), [Party_AnyItemBelow99](Party_AnyItemBelow99.md), [sub_140226E44](sub_140226E44.md), [sub_1402723EC](sub_1402723EC.md), [sub_140285B10](sub_140285B10.md), [sub_140286070](sub_140286070.md), [sub_140286160](sub_140286160.md), [sub_140286228](sub_140286228.md), [sub_140286C8C](sub_140286C8C.md), [sub_1402875A4](sub_1402875A4.md), [sub_140287D9C](sub_140287D9C.md), [sub_1402C4D1C](sub_1402C4D1C.md), [sub_1402DE564](sub_1402DE564.md), [sub_1402FE1D0](sub_1402FE1D0.md), [sub_14033B420](sub_14033B420.md), [sub_140396174](sub_140396174.md), [sub_14039684C](sub_14039684C.md), [sub_140396FEC](sub_140396FEC.md)
- Observed behaviours: [ItemIdSpace](../behaviors/ItemIdSpace.md)

## Notes

- I: Because the test is a pure range check, making 254 or 255 assignable would silently break every 255-is-empty site.

## Open questions

None recorded.
