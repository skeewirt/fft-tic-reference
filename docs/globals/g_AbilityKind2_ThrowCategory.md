# g_AbilityKind2_ThrowCategory

- **Kind:** global
- **Address:** `0x140789290`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[12]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Throw table: 12 equip-category bytes, ability 382 + i maps to one category. It stores categories, not item ids; an item is throwable when its record's equipment category matches a row for one of the unit's throw abilities.

## Behavior

- V: the 12 bytes are equip categories, one per Throw ability in ability order 382..393; category 0 does not occur.
- V: three functions read it: sub_140281488 matches the item's category byte against the unit's throw abilities; Unit_ListThrowableItems builds the category set for abilities 382..393; Ai_SurveyTargets starts one byte into the table and walks abilities 383..392.
- V: no item id is stored in the table; the id comes from the caller's scan over the inventory, which stops at 255 in the throw list and at 0x100 in the AI search.
- V: category 0 never appears, so an item whose category byte is 0 is never throwable even when every other condition holds.
- V: the throw list also requires a weapon slot, weapon flags bit 1, a non-enemy unit and a non-zero count, so a category match is one of five conditions, not the only one.

## Referenced by

- Described by tables: [AbilityKind2_ThrowCategory](../tables/AbilityKind2_ThrowCategory.md)
- Observed behaviours: [ItemCommandRelation](../behaviors/ItemCommandRelation.md)

## Notes

V: the sheets sub_140281488, Unit_ListThrowableItems and Ai_SurveyTargets.

## Open questions

? why the AI reader offsets by one byte and so never considers ability 382 or 393's category row.
