# SceneUnit_ApplyStatusTint

- **Address:** `0x140269330`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void SceneUnit_ApplyStatusTint(SceneUnitSlot *unit, int ambient, int64_t now)`
- **Callers:** sub_14026947C
- **Callees:** SceneUnit_RunPlacement, SceneUnit_TintOwnRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives a scene unit its colours: a status tint chosen from the unit's flag dword, or the plain row with the ambient light when no tint flag is set.

## Behavior

- V: does nothing when the unit's byte +300 has any of the bits 0x30.
- V: reads the flag dword +348; when none of the bits 0x60C26020 is set it calls SceneUnit_RunPlacement(unit, ambient, now).
- V: flag 0x20: mode 6 with offsets 0, 0, 0 (grey).
- V: flag 0x20000: mode 6 with offsets 3, -1, 8.
- V: flag 0x4000: mode 4 with offsets 8, 0, 0.
- V: flag 0x400000: mode 5 with offsets 0, 8, 0.
- V: flag 0x20000000: mode 4 with offsets 0, 0, 8.
- V: flag 0x800000: mode 5 with offsets -4, -4, -4; flag 0x2000: mode 5 with offsets -8, -8, -8.
- V: flag 0x40000000, unless the sprite byte (+10) is 0x8B or 0x8C: mode 5 with offsets 4, 0, 5.
- V: the flags are tested in that order and the first one set wins; each case calls SceneUnit_TintOwnRow with the unit's slot byte (+8) as the slot. Apart from the group mask 0x60C26020 and 0x20, the code tests the flags by bit number (17, 14, 22, 29, 23, 13, 30), so their masks 0x20000, 0x4000, 0x400000, 0x20000000, 0x800000, 0x2000 and 0x40000000 are not in it as numbers; the sprite test adds 0x75 to the byte and compares with 1, which is 0x8B or 0x8C.

## State touched

- Calls: [SceneUnit_RunPlacement](SceneUnit_RunPlacement.md), [SceneUnit_TintOwnRow](SceneUnit_TintOwnRow.md)

## Referenced by

- Observed behaviours: [UnitColoursAreATintThenAFade](../behaviors/UnitColoursAreATintThenAFade.md)

## Notes

The name is ours (IDB: sub_140269330). The flag 0x40000000 with sprite 0x8B or 0x8C falls through to SceneUnit_RunPlacement.

## Open questions

? which status each flag bit stands for in play (not seen live).
