# HdSheetGroups_ConstructAll

- **Address:** `0x14000F094`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int HdSheetGroups_ConstructAll(void)`
- **Callers:** not recorded
- **Callees:** HdSheetGroup_Construct

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A static initializer: builds the 20 battle HD sheet groups (HdSheetGroup_Construct on each) and registers HdSheetGroups_DestroyAll to run at exit.

## Behavior

- V: from g_HdSheetGroups, twenty times (count at 0x14000F0A5): HdSheetGroup_Construct on the group, then the next group (+0x5298); then atexit(HdSheetGroups_DestroyAll).
- I: it runs from the C runtime's initializer table, before the game's main code.

## State touched

- Calls: [HdSheetGroup_Construct](HdSheetGroup_Construct.md)

## Referenced by

- Observed behaviours: [WordSeventeensArithmeticReachesNewSheetGroups](../behaviors/WordSeventeensArithmeticReachesNewSheetGroups.md)

## Open questions

None recorded.
