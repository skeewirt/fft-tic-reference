# HdSheetGroups_DestroyAll

- **Address:** `0x14060FDB8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void HdSheetGroups_DestroyAll(void)`
- **Callers:** not recorded
- **Callees:** sub_1403D0E10

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The exit-time destructor of the 20 battle HD sheet groups, last to first.

## Behavior

- V: from the array's end (qword_142F0D7C0, a separate global, at 0x14060FDC7) backwards, twenty times (count at 0x14060FDC2): the previous group (-0x5298), then sub_1403D0E10 on it.

## Referenced by

- Observed behaviours: [WordSeventeensArithmeticReachesNewSheetGroups](../behaviors/WordSeventeensArithmeticReachesNewSheetGroups.md)

## Open questions

None recorded.
