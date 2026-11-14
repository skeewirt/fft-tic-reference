# SceneUnit_TintOwnRow

- **Address:** `0x14026929C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int64_t SceneUnit_TintOwnRow(SceneUnitSlot *unit, int mode, int64_t unused, unsigned slot, int unused2, int16_t dr, int16_t dg, int16_t db, int now)`
- **Callers:** SceneUnit_ApplyStatusTint
- **Callees:** UnitClut_TintRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Picks the 16-colour row a scene unit is drawn with and passes it to UnitClut_TintRow with the caller's mode and offsets.

## Behavior

- V: the row is 32 bytes at 32 * the unit's palette byte (+11) inside the palette of the unit's look pool record: 0x140D03676 + 13014 * the pool byte (+9).
- V: for the sprite bytes 155, 156, 157 and 158 (+10) the row comes from the block at 0x140D354B0 instead, at 320, 0, 160 and 512 bytes plus 32 * the palette byte.
- V: ends in a jump to UnitClut_TintRow with the mode in the first argument and the row in the second; the other arguments pass through.

## State touched

- Calls: [UnitClut_TintRow](UnitClut_TintRow.md)

## Referenced by

- Called by: [SceneUnit_ApplyStatusTint](SceneUnit_ApplyStatusTint.md)
- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The name is ours (IDB: sub_14026929C). The call of UnitClut_TintRow is a tail jump. Structures: SceneUnitSlot, LookPoolRecord.

## Open questions

None recorded.
