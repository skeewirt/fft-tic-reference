# GuideLesson_MarkRead

- **Address:** `0x1400D6EA8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideLesson_MarkRead(int id)`
- **Callers:** not recorded
- **Callees:** Guide_GetEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks a lesson (window types 4..6) as read.

## Behavior

- V: sets the read bit (+146 of g_UnitJobFlags); called from sub_14017CFF0 when a lesson is opened.

## State touched

- Calls: [Guide_GetEntry](Guide_GetEntry.md)
- Writes: [g_GuideLessonReadBits](../globals/g_GuideLessonReadBits.md)

## Referenced by

- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
