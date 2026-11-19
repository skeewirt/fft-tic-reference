# AchievementClassesMatchByColumn

- **Kind:** observed behaviour
- **Scope:** engine (achievements)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [Achievement_CounterReached](../functions/Achievement_CounterReached.md), [AchievementOtherNovel_Match](../functions/AchievementOtherNovel_Match.md), [AchievementOtherJournal_Match](../functions/AchievementOtherJournal_Match.md), [Achievement_LookupTelemetryRow](../functions/Achievement_LookupTelemetryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which Achievement column an achievement class tests: a counter, a book or a Chronicle event.

## Behavior

- V: counter achievements: the UserSituation counter named by counter reaches threshold (threshold 0 never earns).
- V: AchievementOtherNovel: a NovelReadThroughNotification whose book id equals book.
- V: AchievementOtherJournal: a JournalNotification whose value equals event_id.
- V: telemetry_achievement is a key of table 173 (TelemetryAchievement-en).

## Open questions

None recorded.
