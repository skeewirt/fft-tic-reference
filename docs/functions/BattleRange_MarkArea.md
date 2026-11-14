# BattleRange_MarkArea

- **Address:** `0x140280B40`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleRange_MarkArea(const void *action)`
- **Callers:** BattleRange_ApplyShape
- **Callees:** AbilityAction_GetRecord, sub_14027EBF8, sub_14027EA18, sub_14027F874, sub_140281014, sub_140280ED0, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks every tile of an action effect area: it reads the ability action record, builds the area offsets for the shape, and sets them relative to the target tile.

## Behavior

- V: the action block is copied to the stack; the acting slot is byte 0 and the ability or item id is the signed word at +2.
- V: the ability record is fetched through AbilityAction_GetRecord and its bytes +1, +2, +3, +4 and +6 drive the area shape.
- V: the shape bits select one of the offset builders (sub_14027EBF8, sub_14027EA18, sub_14027F874, sub_140281014), and the tile set is applied through sub_140280ED0.
- V: the map cells are addressed through the tile block at 0x140D8DCB0 with a stride of eight bytes (image base + 0xD8DCB5, the height byte); the flag byte at +6 of each cell is tested.
- V: the party and unit tables at 0x141800EE0 and 0x1418004E0 are consulted when the area is centred on a unit rather than a tile.
- V: the final pass sets or clears bit 0x80 of the height byte over the 0x1000/8 cells, then the routine ends with the /GS check at 0x14041FAE0 (__security_check_cookie), not a cursor-mask setter.
- I: the byte at record +6 with bit 0x20 selects a shape that is not a simple radius, because the code switches to the direction builders when it is set.
- ?: the names of the individual shapes; the four builders were not decoded here.

## State touched

- Calls: [AbilityAction_GetRecord](AbilityAction_GetRecord.md)

## Referenced by

- Called by: [BattleRange_ApplyShape](BattleRange_ApplyShape.md)

## Notes

Whole function read (912 bytes).

## Open questions

None recorded.
