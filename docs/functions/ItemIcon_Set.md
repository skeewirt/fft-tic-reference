# ItemIcon_Set

- **Address:** `0x14022A9E4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ItemIcon_Set(void *state, uint16_t itemId)`
- **Callers:** sub_14022AFEC, sub_140266890, sub_1402F9F20, sub_140311CB0, sub_140315B10, sub_14033A37C, sub_1403932C8, sub_140399A64 (eight direct sites)
- **Callees:** Item_GetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the small draw state of one classic item icon from the item record's two icon bytes: a 16 by 16 tile in a shared sheet and a palette selector.

## Behavior

- V: the item id is masked to nine bits (0x1FF) before the record lookup, so only the low 512 ids reach the record.
- V: reads record byte +0 as the icon palette and record byte +1 as the tile index.
- V: writes the tile origin as two bytes: state+0x14 = (tile + tile / 15) * 16, the column, and state+0x15 = (tile / 15 + 2) * 16, the row plus two header rows. The division by 15 is a multiply by 0x88888889 and a shift.
- V: clamps the palette to 15 (cmova with 0xF).
- V: writes a 16 by 16 size as the dword 0x00100010 at state+0x18.
- V: builds one packed word at state+0x16 from the palette: a page part of 254 plus palette / 8 (clamped below 0x200, then shifted left 6), and a palette part of 40 plus palette modulo 8 (the base 640 divided by 16).- V: eight direct call sites.
- I: the packed word selects one of two texture pages and one of eight palette rows per page; it rests on the two base constants (254 and 640, the latter divided by 16 to 40).
- I: the state is a 32-byte record (the highest field written here is +0x18); the icon builders advance a state pointer by that stride in their own bodies, not here.
- I: the callers are unit and battle panels, a shop-row setter, a bulk icon builder and a sprite wrapper, judged from the code around each call.
- ?: which draw call consumes the state.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md)

## Referenced by

- Called by: [sub_14022AFEC](sub_14022AFEC.md), [sub_140266890](sub_140266890.md), [sub_1402F9F20](sub_1402F9F20.md), [sub_140311CB0](sub_140311CB0.md), [sub_140315B10](sub_140315B10.md), [sub_14033A37C](sub_14033A37C.md), [sub_1403932C8](sub_1403932C8.md), [sub_140399A64](sub_140399A64.md)

## Notes

- V: the whole body was read; nothing was run. The function leaves the packed palette word in eax, but the call sites ignore it, so the sheet gives it no return value.

## Open questions

- ?: the draw consumer and the exact meaning of the page field.
