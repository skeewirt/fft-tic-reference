# GuideListsAndAutoShowRule

- **Kind:** observed behaviour
- **Scope:** engine (tutorials and lessons)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [Guide_TryAutoShow](../functions/Guide_TryAutoShow.md), [Guide_IsUnlocked](../functions/Guide_IsUnlocked.md), [Guide_MarkShown](../functions/Guide_MarkShown.md), [GuideLesson_MarkRead](../functions/GuideLesson_MarkRead.md), [GuideLessons_UpdateUnlocked](../functions/GuideLessons_UpdateUnlocked.md), [GuideList_BuildCategory](../functions/GuideList_BuildCategory.md), [GuideList_BuildLessons](../functions/GuideList_BuildLessons.md), [Guide_OpenWindow](../functions/Guide_OpenWindow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A guide's window type, category and bit number decide where it is listed, where its seen or unlocked bit lives and when it opens by itself.

## Behavior

- V: window_type 1 opens the add-on of UI row 181, 2 that of UI row 182 (both pause the game), 3 the GuideTip (UI row 184); types 1 / 2 keep their seen bit in the config bits (g_ConfigData +204), types 4..6 in the job flag block (+146 read, +169 unlocked).
- V: category 1..3 are the tutorial tabs (category - 1), 7..12 the lesson tabs (category - 7); lists skip keys of 3001 and above for tutorials, and hold at most 128 entries.
- V: seen_bit is a 1-based bit number n: byte n / 8, bit (n - 1) % 8; values below 80 for the config bits, below 184 for the job flag bits.
- V: job_type non-zero hides the lesson while the job type's disable flag (g_UnitJobFlags +21 + value) is set; user_situation is the lesson's unlock condition; user_situation_2 is the auto-show condition.
- V: a guide opens by itself when seen_bit is 0, or when it is not yet unlocked and user_situation_2 is 0 or met; delay is an input pause before it opens (Input_PauseFor(delay + 1/30 s)); unlocked_by_story counts the guide as unlocked once UserSituation 10200 is met.
- V: the lists are sorted by sort_order, ascending.

## Open questions

? where the lesson bit arrays are saved (they follow the 146-byte job flag block in memory).
