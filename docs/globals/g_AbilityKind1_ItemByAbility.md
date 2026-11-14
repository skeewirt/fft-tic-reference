# g_AbilityKind1_ItemByAbility

- **Kind:** global
- **Address:** `0x140785E18`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[14]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Item-command table: 14 bytes, ability 368 + i maps to item 240 + i (items 240..253). It carries item ids, not abilities, and it is the only table that pairs an Item-command ability with its item.

## Behavior

- V: Unit_ListItemCommandItems is the only direct reader: it accepts abilities 368..381, loads a row as a byte and writes the byte into the item list.
- V: Action_BuildCurrentAction reaches the same rows through an address derived as this base minus 0x170, with no range check; an index outside the 14 rows reads the real bytes that follow the table (0, 0, 0, 1, 2, 255) rather than a zero.
- V: items 254 and 255 are consumables by category and have chemist rows, but they have no row here, so the Item menu cannot offer them.
- V: the paired ability must also have animation and effect rows and must be reachable from the item skillset's 16 slots, so a consumable needs an item record, a chemist row and a paired ability that is in this table and has those rows.
- I: extending the table alone does not widen the mapping: the reader's range check and its byte-wide item output are the binding limits.

## Referenced by

- Described by tables: [AbilityKind1_ItemByAbility](../tables/AbilityKind1_ItemByAbility.md)
- Observed behaviours: [ItemCommandRelation](../behaviors/ItemCommandRelation.md)

## Notes

V: the sheets Unit_ListItemCommandItems and Action_BuildCurrentAction.

## Open questions

? the purpose of the six bytes after the 14 rows; one out-of-range reader can reach them, but no stock ability is meant to.
