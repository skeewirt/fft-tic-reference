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
- V (2026-11-21): the texture row is stored as one byte (the piece record's +5), so 8 * (strip + piece row) wraps past 255: no strip lies below the classic sheet's last row; the HD sheet (g2d entry 161) is the same sheet at twice the size.
- V (2026-11-21): the piece header is +4 = (frame flags & 0x60) | 9 and +6 = unit +22 + ((frame + 2) << 6) in mode 1 (state +2 = 1); mode 2 writes | 8 and leaves the strip out of the row.
- V (2026-11-21): the frame is offset per animation type (state +32 table indexed by unit +338, the type ItemSprite_LoadPalettes stores).
- V (data, 2026-11-21): the stock strips are 0..28 in steps of 2; per category see behavior HeldWeaponsDrawFromOneSheetPageByAByteRow.

## State touched

- Calls: [Item_GetEquipPalette](Item_GetEquipPalette.md), [BattleAnim_PickProjectile](BattleAnim_PickProjectile.md), [SoundCue_Play](SoundCue_Play.md)

## Referenced by

- Observed behaviours: [HeldWeaponsDrawFromOneSheetPageByAByteRow](../behaviors/HeldWeaponsDrawFromOneSheetPageByAByteRow.md), [WeaponPoseFollowsTheEquipCategory](../behaviors/WeaponPoseFollowsTheEquipCategory.md)

## Open questions

? the frame data layout (state +32 / +40 / +48 arrays).
