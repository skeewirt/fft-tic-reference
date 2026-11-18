# ItemSprite_LoadPalettes

- **Address:** `0x14026A358`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `void ItemSprite_LoadPalettes(uint16_t itemId, void *spriteState, char keepCategory)`
- **Callers:** Battle_ExecuteAction, EventScript_Run, sub_14026A7B8, SceneUnit_BuildFromQueueEntry (two sites): five direct sites in four functions
- **Callees:** Item_GetRecord, Item_GetEquipPalette, sub_1402F7594

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the two palettes of the unit's equipped weapon or shield into the sprite state, and records the item id and an equipment category with them.

## Behavior

- V: the item id is masked to nine bits (0x1FF) for the record lookup; the palette selector is asked for with the full, unmasked id.
- V: the equipment category is record byte +5.
- V: category 35 maps to 3; any category of 32 or more maps to 21.
- V: when the caller's third argument byte is zero, two special values of the state word at +0x142 also map to 21: the range 382..393 and the single value 148.
- V: a null selector from Item_GetEquipPalette leaves the palette byte at zero, so both sprite slots use palette zero.
- V: the selector's high nibble chooses the palette for sprite slot 5 and its low nibble the palette for slot 6.
- V: each palette is 32 bytes (16 colours of two bytes) taken from a table based at 0x140D35750.
- V: stores the item id at state +0x150 and the mapped category byte at +0x152.
- V: five direct call sites in four functions (battle action, event script, two sprite builders).
- I: the palette is applied to the sprite record the caller passes in, which is the unit's render state.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [Item_GetEquipPalette](Item_GetEquipPalette.md), [sub_1402F7594](sub_1402F7594.md)

## Referenced by

- Called by: [Battle_ExecuteAction](Battle_ExecuteAction.md), [SceneUnit_BuildFromQueueEntry](SceneUnit_BuildFromQueueEntry.md), [sub_14026A7B8](sub_14026A7B8.md)

## Notes

- V: whole body read; the reference sheet for the same address agrees.

## Open questions

- ?: the meaning of the 3 and 21 category mappings.
