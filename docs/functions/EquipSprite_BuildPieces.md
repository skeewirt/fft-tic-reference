# EquipSprite_BuildPieces

- **Address:** `0x14026BC60`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int EquipSprite_BuildPieces(uint8_t *unit, uint8_t *state, int16_t frame)`
- **Callers:** sub_14026CAA4
- **Callees:** Item_GetEquipPalette, BattleAnim_PickProjectile, SoundCue_Play

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the sprite piece records of a unit's held item for one animation frame.

## Behavior

- V: at the start it reads the equipment palette row of the item id at unit +336 (Item_GetEquipPalette) and keeps byte +1 of it (0 when the item has none).
- V: for each piece of the frame it writes a piece record whose texture row is 8 * (that byte + the frame piece's row value): the byte is the row of the item's picture in the equipment sheet, in steps of 8 pixels.
- V: returns 256 when the frame number is above 256 or the frame has no data (index -1).
- I: one picture per item, from the stock values of the byte; the stock rows were not re-counted here.

## State touched

- Calls: [Item_GetEquipPalette](Item_GetEquipPalette.md), [BattleAnim_PickProjectile](BattleAnim_PickProjectile.md), [SoundCue_Play](SoundCue_Play.md)

## Open questions

? the frame data layout (state +32 / +40 / +48 arrays).
