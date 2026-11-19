# g_GuideLessonReadBits

- **Kind:** global
- **Address:** `0x1411A7522`
- **Type:** `save data`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

23 bytes (184 bits) that follow the 146-byte job flag block (g_UnitJobFlags +146): the lesson read bits, one per Guide seen_bit number (1-based: byte n / 8, bit (n - 1) % 8). Set by GuideLesson_MarkRead, read by GuideList_BuildLessons (the 'new' flag). Whether the save stores them was not followed.

## Referenced by

- Read by: [GuideList_BuildLessons](../functions/GuideList_BuildLessons.md)
- Written by: [GuideLesson_MarkRead](../functions/GuideLesson_MarkRead.md)

## Open questions

None recorded.
