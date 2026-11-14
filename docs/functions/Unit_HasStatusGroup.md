# Unit_HasStatusGroup

- **Address:** `0x140278FA8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Unit_HasStatusGroup(const void *unit, int group)`
- **Callers:** sub_140239294, sub_14027ADB8, sub_140282A7C, sub_140282BDC, sub_140282E38, sub_14030AF88, sub_14030AFEC, sub_14030C5A0, sub_14030CD08, sub_14030D1CC, sub_14030EE00, BTurn_StatusFlags, sub_14030FC00, sub_1403888D8, sub_140389554
- **Callees:** none found

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests whether a unit carries any status of one of the ten party-wide status groups by ANDing its five status bytes against that group's five-byte mask.

## Behavior

- V: the second argument indexes the ten 5-byte masks at 0x1411A6A70; the mask stride is five bytes.
- V: the unit status bytes at +0x61, +0x62, +0x63, +0x64 and +0x65 are tested one at a time against the matching mask byte (the pointer is incremented from +0x61, so only +0x61 is an immediate).
- V: it returns 1 as soon as one byte shares a bit, and 0 after all five bytes.
- V: a group index outside 0..9 is not bounded by this body; the address arithmetic simply reads whatever follows the mask table.
- V: the masks are built once by Status_BuildFlagMasks; this function only reads them.
- I: group 3 is the Crystal/Stone/Chest/Stop/Sleep set used by the turn-start status check, and group 4 is the "can learn" test.
- ?: the meaning of the remaining eight groups; the mask bytes are data and were not decoded here.

## State touched

- Reads: [g_StatusGroupMasks](../globals/g_StatusGroupMasks.md), [UnitWorkRecord](../structs/UnitWorkRecord.md)

## Referenced by

- Called by: [Battle_IsTileOccupied](Battle_IsTileOccupied.md), [Battle_MoveRangeSetup](Battle_MoveRangeSetup.md), [Battle_PreviewUnitAction](Battle_PreviewUnitAction.md), [Formula_ReactionPrecheck](Formula_ReactionPrecheck.md)

## Notes

Head and whole body read (0x7C bytes, no unwind entry); the 17 call sites were counted from the image.

## Open questions

None recorded.
