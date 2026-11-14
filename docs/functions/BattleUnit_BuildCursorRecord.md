# BattleUnit_BuildCursorRecord

- **Address:** `0x140281248`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleUnit_BuildCursorRecord(uint8_t *out, int unit_slot)`
- **Callers:** sub_1401FC044, sub_1401FC234, sub_1401FDD7C, sub_140262B20, sub_140280170, sub_1402804D8, sub_140280850, sub_14030ED60, sub_14030EE00
- **Callees:** none found

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the seven-byte cursor record a unit contributes to the targeting display: slot and flags, level, terrain height and the tile the cursor should sit on.

## Behavior

- V: the first argument is the seven-byte output record and the second is the unit slot; the record is cleared first.
- V: a slot above 0x14, a unit marker of 0xFF at +1, unit +0x61 bit 0x40 or unit +0x62 bit 1 make it return with the cleared record.
- V: out +0 is unit +0x4F, out +1 is unit +0x50, and out +2 combines bit 7 of unit +0x51 with bit 7 of the caller flags.
- V: out +3 is the slot, with bit 0x20 set for every job outside the 94..96 monster range.
- V: out +4 is 6 normally and 4 when unit +0x63 bits 1 and 2 are set; out +5 is the tile height from the map cell plus that base.
- V: out +6 adds the same base to the height and is the final cursor height.
- V: the map cell is found through the tile block at 0x140D8DCB0, indexed by the unit tile coordinates and the layer, at a stride of eight bytes.
- V: the cell bytes +2 and +3 carry the terrain height and the low five bits of the move cost used in the adjustment.
- I: the record is a cursor placement request, because the callers are the range, target and panel paths and the last byte is a screen height.
- ?: what the 0x20 bit in out +3 tells the caller beyond 'not a large monster'.

## State touched

- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Notes

Whole function read (492 bytes). The output layout is read from the writes; the semantic names of the height fields come from the cursor-range study.

## Open questions

None recorded.
