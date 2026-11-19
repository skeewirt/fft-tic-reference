# AchievementOtherNovel_Match

- **Address:** `0x1400DDF1C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool AchievementOtherNovel_Match(void *achievement, const void *notification)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Match function of the book-read achievement class (vtable 0x1407032A8).

## Behavior

- V: true for notification type 24 (NovelReadThroughNotification) whose +8 (the book id) equals Achievement book (+0x10).

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Observed behaviours: [AchievementClassesMatchByColumn](../behaviors/AchievementClassesMatchByColumn.md)
- Resolves registries: [AchievementNotificationTypes](../registries/AchievementNotificationTypes.md)

## Open questions

None recorded.
