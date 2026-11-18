# EquipScreen_InitVram

- **Address:** `0x14033DE68`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int EquipScreen_InitVram(void)`
- **Callers:** sub_14033E038
- **Callees:** VramPage_CopyRect, sub_14025FC38, Inventory_SnapshotWithEquipped, sub_14039684C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Uploads the palette and strips of the equipment screen to VRAM and resets the equipment lists.

## Behavior

- V: uploads the staging block to a VRAM rectangle at x 256 and the 64 x 4 word palette block (0x1407B4E60) to the rectangle at x 256, y 250.
- V: uploads two more small strips built through sub_14025FC38, then clears an eight-byte state and sets four words to 0xFFFF.
- V: takes a snapshot of the inventory including the equipped items and synchronises the saved order lists of groups 0..4 (sub_14039684C), then zeroes the screen's work block.
- I: the item-order work and the call from the unit equipment screen task (sub_14033E038) show this is the equipment screen's set-up.

## State touched

- Calls: [VramPage_CopyRect](VramPage_CopyRect.md), [sub_14025FC38](sub_14025FC38.md), [sub_14039684C](sub_14039684C.md)

## Referenced by

- Reads tables: [EquipScreenPalette](../tables/EquipScreenPalette.md)

## Notes

IDA carried a wrong library name for this function; the code is the screen set-up above. The four words are set by storing -1 (0xFFFF); the value 0xFFFF does not appear as a literal in the body.

## Open questions

?: what the two small strips are.
