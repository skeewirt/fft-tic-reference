# ActionEntryWord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 16-bit word of a four-byte action entry (the AI and preview form): the action id in bits 0..9 and the acting unit slot in bits 10..15. The current-action builder splits it with a 10-bit mask and a shift of ten.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="action_id"></a>bits 0..9 | action_id | `uint16` | V | Item id, ability id or throw item id depending on the command; the builder masks it with 0x3FF. |
| <a id="acting_unit"></a>bits 10..15 | acting_unit | `bits` | V | Acting unit slot, taken by a right shift of ten. A width census labels these six bits an action kind; the decoded reader uses them as the unit slot, and the record follows the reader. |

## Behavior

- V: the entry is four bytes: this word, a command byte and a flags byte. The builder stores the command byte at block +0, the word at +2 and the flags at +0x10.
- V: only ten id bits are ever read, so a raw id above 1023 cannot reach the builder through this word.
- V: for the Item command the word holds an ability id (item + 0x80) at use; the builder subtracts 0x80 to recover the item id, stores the item at block +6 and keeps the ability in the word.
- V: for Throw the low ten bits are an item id first and become the resolved throw ability, so the word and the item field at +6 disagree about what the low bits mean until the ability is resolved.
- I: a six-bit field cannot be both a unit slot and an action kind; the unit-slot reading is the decoded one, so the kind label in the width census is a naming error rather than a second meaning.

## Referenced by

- Observed behaviours: [ItemCommandRelation](../behaviors/ItemCommandRelation.md)

## Notes

V: the sheet Action_BuildCurrentAction (layout and the item/throw branches).

## Open questions

? whether any other producer packs a different field into bits 10..15 (the width census's kind).
