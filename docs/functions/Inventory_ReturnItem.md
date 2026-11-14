# Inventory_ReturnItem

- **Address:** `0x14030CEA4`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Inventory_ReturnItem(void *unit, uint16_t item)`
- **Callers:** sub_1402722D8, Battle_ApplyActionResult (two sites), sub_14030BF04
- **Callees:** `sub_140278FEC` (Item_CountOwnedAndEquipped), `sub_14030CF38`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Puts one item back into the party inventory: the refund step for a use that was cancelled or resolved away. It is the
counterpart of the item-consume path and leaves the same store it takes from.

## Behavior

- V: it refuses to act while the battle-context dword at `0x14186AF80` is nonzero; that dword is set to 2 around
  reaction and secondary actions, so those actions never refund.
- V: it refuses item id 0 and id `0xFF`, which are the empty-slot values.
- V: it refuses every item id at or above `0x105` (261); an item numbered above 260 cannot be
  returned by this path.
- V: it refuses when the owning unit's team bits (record +0x1EE, mask `0x30`) are set, so enemy units get no refund.
- V: it counts how many copies the party owns and has equipped, using Item_CountOwnedAndEquipped.
- V: it writes the item id and a zero into the block reached through the render-manager global (g_CharaRenderMgr), at
  +0x3524 and +0x3528.
- V: when the count is below 99 it increments the per-id byte count in the inventory array at `0x1411A7C00` and
  returns 0.
- V: when the count is 99 or more it calls `sub_14030CF38` with the unit, a zero and the id instead of incrementing, and
  returns that call's value.
- I: the count test is the 99-per-stack rule, and `sub_14030CF38` handles the overflow case, because the ordinary
  shop-add path uses the same threshold.
- I: the pair at +0x3524 and +0x3528 is the UI's last-item record, because the same write appears in other inventory
  routines.
- I: the result applier calls it twice because a result can be undone once per actor and once per target list.
- ?: what `sub_14030CF38` does with a full stack; it was not read for this sheet.

## State touched

- Calls: [sub_140278FEC](sub_140278FEC.md), [sub_14030CF38](sub_14030CF38.md)
- Reads: [g_BattleContextGate](../globals/g_BattleContextGate.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Referenced by

- Called by: [sub_1402722D8](sub_1402722D8.md), [sub_14030BF04](sub_14030BF04.md)

## Notes

- V: the whole function was read (it is short); the overflow helper was not.

## Open questions

None recorded.
