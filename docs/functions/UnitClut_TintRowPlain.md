# UnitClut_TintRowPlain

- **Address:** `0x1402F78A4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int16_t UnitClut_TintRowPlain(uint16_t *row, int unused, unsigned slot, int unused2, int16_t dr, int16_t dg, int16_t db, int now)`
- **Callers:** SceneUnit_RunPlacement
- **Callees:** UnitClut_TintRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Calls UnitClut_TintRow with mode 8 (the channels as they are plus the offsets) for a row and a slot.

## Behavior

- V: one call: UnitClut_TintRow(8, row, slot, slot, _, dr, dg, db, now).

## State touched

- Calls: [UnitClut_TintRow](UnitClut_TintRow.md)

## Referenced by

- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The name is ours (IDB: sub_1402F78A4). SceneUnit_RunPlacement hands it the unit's own row and the ambient offsets it worked out.

## Open questions

None recorded.
