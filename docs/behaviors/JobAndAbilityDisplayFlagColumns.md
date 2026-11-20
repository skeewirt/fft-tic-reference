# JobAndAbilityDisplayFlagColumns

- **Kind:** observed behaviour
- **Scope:** engine (job and ability windows)
- **Area:** [Job tree](../areas/job-tree.md)
- **Affects:** [UIGadgetFFTOJobDetailWindow_SetJob](../functions/UIGadgetFFTOJobDetailWindow_SetJob.md), [sub_140107914](../functions/sub_140107914.md), [sub_1402A20A4](../functions/sub_1402A20A4.md), [JobCommand_SameGroup](../functions/JobCommand_SameGroup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Small flag columns of the Job, Ability and JobCommand tables that only change how a window draws.

## Behavior

- V: Ability drawback (+0x30): in the job detail window an innate ability whose value is 2 plays the 'Bad' state, any other value plays 'Good'. Earlier text said 'Good' for 2; the code stops 'Good' and plays 'Bad' for 2. In the stock data only one ability ('Cannot Enter Water') has 2 (M).
- V: Ability shows_unknown_info (+0x3C): a value of 1 or 2 makes the battle command list cursor play its 'ShowUnknown' state for that ability, otherwise 'HideUnknown' (the state names are I).
- V: JobCommand user_situation (+0x1C): once that UserSituation holds and description_2 (+0x10) is non-empty, the job command detail window shows description_2 instead of description (+0x0C).
- V: JobCommand group (+0x14): two JobCommand rows are the same command when their group values are equal (JobCommand_SameGroup).

## Open questions

None recorded.
