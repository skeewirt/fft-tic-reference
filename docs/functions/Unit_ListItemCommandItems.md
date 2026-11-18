# Unit_ListItemCommandItems

- **Address:** `0x14030E680`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Unit_ListItemCommandItems(int unit_slot, uint8_t command, uint8_t *out)`
- **Callers:** sub_14023678C, sub_1402EA58C, sub_14030E174
- **Callees:** `sub_14030DB88`, `sub_14030E368`, `__security_check_cookie`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the item list for the Item command: it takes the usable ability list of the command's skill set and rewrites
each of the fourteen item abilities into the item id the command offers.

## Behavior

- V: the first argument is a battle unit slot and the second a command id; the third is the caller's output buffer.
- V: it returns 0 when the unit slot has no live unit, and 0 when the command id is not 6.
- V: for command 6 it calls `sub_14030E368` to build the usable ability list for that command and gets a count back.
- V: it walks the returned 16-bit ability words and accepts only ids 368 through 381 (the test subtracts 0x170 and rejects
  results above 0x0D); everything else is skipped.
- V: each accepted ability is translated to an item id by the fourteen-row byte table at `0x140785E18`, indexed by
  the ability id minus 368.
- V: the table read at 0x14030E722 is the single call site of that table in the image.
- V: each result is written into the output buffer as one byte, and the list is terminated with `0xFF`.
- V: it returns `0x100 + count`, not a bare count; the zero case is the failure value.
- V: it performs no inventory check; an item with a zero count is still listed by this function.
- I: the `0x100` in the return value is a list-type tag the menu uses to tell an item list from an ability list,
  because the sibling list builders return small counts.
- I: the fourteen rows cover ids 240..253, so a consumable numbered 254, 255 or above can never appear here even when
  the rest of its data is valid.
- ?: whether any caller bounds-checks the count against the output buffer size.

## State touched

- Calls: [sub_14030E368](sub_14030E368.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [sub_14023678C](sub_14023678C.md), [sub_1402EA58C](sub_1402EA58C.md), [sub_14030E174](sub_14030E174.md)
- Observed behaviours: [ItemCommandRelation](../behaviors/ItemCommandRelation.md)
- Reads tables: [AbilityKind1_ItemByAbility](../tables/AbilityKind1_ItemByAbility.md)

## Notes

- V: the whole function was read, and the single call site of the table in the image was confirmed.
- I: kind1 gives the item id per Item-command ability (ids 0x170..0x17D).

## Open questions

None recorded.
