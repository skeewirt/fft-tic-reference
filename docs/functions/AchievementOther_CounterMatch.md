# AchievementOther_CounterMatch

- **Address:** `0x1400DE08C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool AchievementOther_CounterMatch(void *achievement)`
- **Callers:** not recorded
- **Callees:** Achievement_CounterReached

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counter test of the deep-dungeon-clear and side-story achievement classes.

## Behavior

- V: calls Achievement_CounterReached with the object's own id.

## State touched

- Calls: [Achievement_CounterReached](Achievement_CounterReached.md)

## Open questions

None recorded.
