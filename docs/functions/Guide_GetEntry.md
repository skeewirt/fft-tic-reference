# Guide_GetEntry

- **Address:** `0x1400DB81C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Guide_GetEntry(const uint8_t **out, int id)`
- **Callers:** sub_1400D6DAC, sub_1400D6EA8, sub_1400DA454, sub_1400DB2B4, sub_1400EDFBC, sub_14017D3D4, GuideWindow_ShowPage, sub_140197B14, sub_140198140, sub_1402AC878
- **Callees:** NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fetches the Guide row of an id.

## Behavior

- V: *out = NxdTable_GetRowById(187, id); 0 for id 0.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Called by: [GuideLesson_MarkRead](GuideLesson_MarkRead.md), [Guide_CompareSortOrder](Guide_CompareSortOrder.md), [Guide_MarkShown](Guide_MarkShown.md), [Guide_QueueAutoShow](Guide_QueueAutoShow.md), [Guide_TryAutoShow](Guide_TryAutoShow.md)

## Open questions

None recorded.
