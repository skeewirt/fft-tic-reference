# NovelReader_SendReadThrough

- **Address:** `0x1401DFF60`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void NovelReader_SendReadThrough(void *reader)`
- **Callers:** not recorded
- **Callees:** sub_1400DF354

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reports that the book was read to the end.

## Behavior

- V: sets bit 2 of reader +64 and sends NovelReadThroughNotification {book id = reader +80} through sub_1400DF354 on the notification object (qword_143CD9E30).
- V: the achievement class AchievementOtherNovel matches this notification (see AchievementOtherNovel_Match).

## Referenced by

- Observed behaviours: [BookPageTextIsReadFromTheNovelTableOfPageTable](../behaviors/BookPageTextIsReadFromTheNovelTableOfPageTable.md)

## Open questions

None recorded.
