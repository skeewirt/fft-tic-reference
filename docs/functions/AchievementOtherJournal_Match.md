# AchievementOtherJournal_Match

- **Address:** `0x1400DDFD4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool AchievementOtherJournal_Match(void *achievement, const void *notification)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Match function of the Chronicle-event achievement class (vtable 0x1407031E8).

## Behavior

- V: true for notification type 25 (JournalNotification) whose +8 equals Achievement event_id (+0x14).
- V: that value is Journal event_id (+0x18); for example Journal key 310 ('Seekers of the Stone') has +0x18 = 159.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Observed behaviours: [AchievementClassesMatchByColumn](../behaviors/AchievementClassesMatchByColumn.md)
- Resolves registries: [AchievementNotificationTypes](../registries/AchievementNotificationTypes.md)

## Open questions

None recorded.
