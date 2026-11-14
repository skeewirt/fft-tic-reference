# StoryChoiceBalloon

- **Kind:** observed behaviour
- **Scope:** story scenes: a dialogue balloon with several selectable lines
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventMessage_Task](../functions/EventMessage_Task.md), [EventMessage_Scripted](../functions/EventMessage_Scripted.md), [sub_1401365AC](../functions/sub_1401365AC.md), [sub_140136654](../functions/sub_140136654.md), [EventSkip_IsAvailable](../functions/EventSkip_IsAvailable.md), [EventText_NextChar](../functions/EventText_NextChar.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A choice balloon is an ordinary message whose text contains the control code 0xFB (options start on this line) and 0xFC (run the choice). Each frame the message window task focuses one of two option nodes of the event window and shows the finger cursor, moves the cursor with up / down, and on confirm stores the 0-based index in event variable 24; the event script branches on it. No opcode and no message flag is involved. Seen live at the Mandalia opening: that choice is not skippable and fast-forward does nothing.

## Behavior

- V: authoring: code 0xFB stores the current line number as the first option row (0xFFFF = none); code 0xFC runs the choice loop; with no 0xFB before it the 0xFC does nothing (EventMessage_Task and EventMessage_Scripted byte switches). Opcode 0x10 only starts the window.
- V: the choice loop runs one frame at a time: it calls sub_1401365AC and sub_140136654 (next bullets), waits one frame, leaves on task tag 3 or word_142FEC554, else reads action 0x21 (up, mask 0x1000), 0x22 (down, mask 0x4000), 0x1A (confirm, mask 0x20) with Input_TestAction on g_EventButtonMask1. Cancel (0x1B) is not read; no fast-forward or auto-advance test is in the loop.
- V: the cursor starts on the first option row, up stops at it, down stops at the last line reached so far (option count = last line - first option row + 1, I). The digits '1.' and '2.' are plain message text. Seen live 2026-11-09: DOWN moved the cursor from option 1 to option 2, UP moved it back, and the cursor does not wrap.
- V: the UI path (code, both functions read in full in IDA): each frame sub_1401365AC(event agent, window variant, window size, cursor) takes the option node of the event window selected by the cursor (an option node exists for the cursor values 0 and 1 only; a larger value does nothing) and gives it the input focus through GUICore_FocusNode; sub_140136654(event agent) then shows the finger cursor with UIAgentCursor_Show when the window's six node pointers are all set. So this build has two option nodes per choice window.
- V (seen live 2026-11-09, Mandalia Plain opening, event 16): while the choice waits the focused widget is the event window (ui/ffto/event/ffto_event.uib) and the finger cursor is shown, at (575, 183) on option 1 and (575, 235) on option 2 (52 px per line). After the confirm the next balloon of the same event keeps that focus but has no finger cursor, and an ordinary balloon of a battle opening never showed one. Recognition used by the tools: the focused widget is the event window AND the finger cursor is shown.
- V (seen live 2026-11-09): the balloon ran in the first task table (slot 2 of the table at 0x140D40AA0): task entry EventMessage_Task, block +0x90 = 1, tag 1. The second table (0x14184B3C0) had no running entry. The text id at block +8 (0x49435, kind 18, index 1077) points at an unrelated pool string: the drawn text is the event window's own text node, so scanning the pool string of the running task does NOT find the choice and is not a recognition.
- V: on confirm the task writes cursor - first option row to dword 24 of the event variable store (off_1407830D8 and g_EventWorkPtr both point to 0x140D40060): event variable 24 at 0x140D40078; sound id 1 on confirm, 3 on a cursor move. Seen live 2026-11-09: pad A confirmed (three times); variable 24 read 0 before and 0 after choosing option 1, so that case does not show the write; option 2 was not chosen (it changes the battle's objective).
- V (seen live 2026-11-09): at this choice the skip gate read: event script running 1, armed 0, veto 0, skip state 0, skip-once 0 = not skippable; a skip request did nothing and a held fast-forward did nothing (3 runs, the hold lasted until stopped by hand). By the code EventSkip_IsAvailable has no message or choice test, so whether a choice can be skipped depends only on armed per event (0 at this one).
- V: while skip runs (word_142FEC554, or g_EventSkipEnabled with the skip state set) the task replaces every text byte by 0xFE, so a choice is passed unanswered and variable 24 keeps its old value (code; not seen live because the Mandalia choice cannot be skipped).
- V: fast-forward (RB / Ctrl) and auto-advance act only in the ordinary page wait loop, never on a waiting choice (code; seen live 2026-11-09: a held fast-forward did nothing at the choice).
- V: a normal balloon page wait is a different loop (codes 0xFE / 0xFD, tests 0x1A, 0x1B, 0x20, 0x39, up / down only to scroll). dword_140D4081C is set in both loops by the code, but read live it was 0 on every read while the choice waited (2026-11-09, two tools, several reads): it is not usable as a 'waiting' flag from outside the game thread.
- V (seen live 2026-11-09): the 584-byte glove sprite records at 0x142FEF870 stayed hidden (x = 512) and nothing in those records, the task blocks or the event globals changed when DOWN moved the cursor: this build draws the cursor through the UI, so the sprite record y is NOT the cursor.

## Notes

Detail and evidence: the function sheets linked from this page (EventMessage_Task, EventMessage_Scripted, sub_1401365AC, sub_140136654). Live results of 2026-11-09 (Mandalia Plain opening, event 16) are tagged in the bullets.

## Open questions

? Where the task's 0xFB / 0xFC text bytes come from for this balloon (the pool string at the text id is unrelated; the drawn text is the event window node). ? What option 2 writes to event variable 24 (only option 1 was chosen: 0 before and after). ? Whether keyboard Enter confirms (only pad A tried). ? A choice outside a battle (world or town event). ? A choice with more than two options (the UI call handles the cursor values 0 and 1 only). ? Which opcodes read variable 24 afterwards.
