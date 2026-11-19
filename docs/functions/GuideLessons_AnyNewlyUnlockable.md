# GuideLessons_AnyNewlyUnlockable

- **Address:** `0x1400DB384`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GuideLessons_AnyNewlyUnlockable(void)`
- **Callers:** sub_140163968
- **Callees:** UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether a lesson could be unlocked now but is not yet.

## Behavior

- V: the same walk as GuideLessons_UpdateUnlocked; returns 1 at the first lesson that passes the tests and whose +169 bit is still clear.

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md)
- Reads: [g_GuideLessonUnlockedBits](../globals/g_GuideLessonUnlockedBits.md)

## Open questions

None recorded.
