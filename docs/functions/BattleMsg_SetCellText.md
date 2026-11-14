# BattleMsg_SetCellText

- **Address:** `0x1402EBA70`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleMsg_SetCellText(void)`
- **Callers:** none found
- **Callees:** sub_1402EB96C, EventTask_WaitFrame, EventTask_Start, sub_1402BA718, EventTask_Terminate (tail jump)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads a 2-byte word from the published unit list and writes it as the message id, with the fixed kind 6, into the battle message object the HUD draws.

## Behavior

- V: the word is read from the published unit list with a 2-byte load; the two sites are 0x1402EBB4B and 0x1402EBB90.
- V: the kind written to the battle message object field +0x4188 is the constant 6; the id goes to +0x418C.
- V: the word is loaded through the published list pointer at 0x14184A9B0, indexed by the signed word at +0x158 of the object loaded from 0x14184B230, and stored as the id with no base subtraction.
- V: it starts a helper task with EventTask_Start, waits with EventTask_WaitFrame, and ends by tail-jumping to EventTask_Terminate.
- V: the task has no direct caller; the battle HUD starts it as a task entry.
- I: the pair is the message descriptor of the currently highlighted command, because the fields are the kind/id pair the text decoder reads.
- ?: whether the same task also clears the message when the cell is empty; the zero branch was not followed.

## State touched

- Calls: [EventTask_WaitFrame](EventTask_WaitFrame.md), [EventTask_Start](EventTask_Start.md), [EventTask_Terminate](EventTask_Terminate.md)

## Notes

Whole function read (754 bytes). The two field writes are the cell-word store.

## Open questions

None recorded.
