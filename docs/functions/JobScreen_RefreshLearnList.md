# JobScreen_RefreshLearnList

- **Address:** `0x1402B9C20`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobScreen_RefreshLearnList(void)`
- **Callers:** sub_1402B9B30
- **Callees:** sub_14031EA20, sub_140303E4C, JobAbilityList_Build, sub_140327854, Input_TestAction, sub_140303E8C, sub_1402C0554, sub_1403278EC, sub_14031DA24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Refreshes the Learn page list after the job screen state changes, rebuilding the ability rows from the job list without spending JP.

## Behavior

- V: it runs the same list setup as the Learn page builder but never calls Unit_SpendJp.
- V: the one-shot flag at 0x140D407C2 guards the initial callback setup.
- V: JobAbilityList_Build rebuilds the rows and sub_14031DA24 refreshes the detail line.
- V: the list words are masked with 0x3FF at the same site pattern as the builder.
- V: the function is called from the job screen state machine after a page change.
- I: this is the cheap refresh twin of the Learn page builder; the difference is the missing JP spend and the different guard byte.
- ?: whether the refresh preserves the cursor row; the list gadget state is not read here.

## State touched

- Calls: [JobAbilityList_Build](JobAbilityList_Build.md), [Input_TestAction](Input_TestAction.md), [sub_1402C0554](sub_1402C0554.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md), [g_JobTable](../globals/g_JobTable.md)

## Notes

Whole function read (917 bytes).

## Open questions

None recorded.
