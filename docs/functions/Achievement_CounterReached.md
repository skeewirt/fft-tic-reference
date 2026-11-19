# Achievement_CounterReached

- **Address:** `0x1400DC984`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool Achievement_CounterReached(int id)`
- **Callers:** the story-chapter achievement classes (sub_1400DCAA0..sub_1400DCAD0), AchievementOther_CounterMatch
- **Callees:** NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether an achievement's counter has reached its threshold.

## Behavior

- V: row = NxdTable_GetRowById(195, id); true when threshold (+0xC) is non-zero and the UserSituation counter named by counter (+8) is at least threshold.
- V: the counter is read from g_UserSituation +24 + 4 * id, or +104 + 4 * id when bit 0 of +16 is set.
- V: called with fixed ids by the story-chapter achievement classes (Prologue 2, Chapter1 3, Chapter2 4, Chapter3 5, Chapter4 6) and with the object's own id by AchievementOther_CounterMatch (the deep-dungeon and side-story classes).

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Called by: [AchievementOther_CounterMatch](AchievementOther_CounterMatch.md)
- Observed behaviours: [AchievementClassesMatchByColumn](../behaviors/AchievementClassesMatchByColumn.md)

## Open questions

None recorded.
