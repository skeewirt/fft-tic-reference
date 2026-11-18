# BattleCommand_CommitCursor

- **Address:** `0x1402EB874`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleCommand_CommitCursor(void)`
- **Callers:** not recorded
- **Callees:** sub_1402E38E4, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Closes a battle command list: normalises its entries and stores the cursor row.

## Behavior

- V: for every entry of the list up to the list's last index turns the entry codes 1 and 60 into 1.
- V: sets the task flag, calls sub_1402E38E4 and stores the cursor row (node byte +80) into the per-unit cursor memory, then ends its task.

## State touched

- Calls: [EventTask_Terminate](EventTask_Terminate.md)

## Notes

Read in full.

## Open questions

None recorded.
