# OpeningSubmenu_Task

- **Address:** `0x14037D998`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall sub_14037D998(int *frame)`
- **Callers:** SceneLoop_Run (0x140331D2D dispatch), SceneLoop_RunAlt (0x14039DE79 dispatch); pushed by sub_14037D848 (0x14037D848), called only by sub_1402F0124
- **Callees:** Input_TestAction, Input_ActionBit, sub_14037FE58, sub_1401D80A8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A three-row scene submenu created by the four-row menu. It moves a highlight over three sprite rows; confirm or cancel tears it down, clears the parent menu's four highlights and pops back to the parent.

## Behavior

- V: table entry 3 of `SceneTaskTable` (`sub_14037D998`, 0x14037D998). Its only pusher is `sub_14037D848`, which writes id 3 at the current depth and increments the depth; that helper is called only by `sub_1402F0124` (table entry 2) in its mode 2. The only callers are the two dispatch sites, `SceneLoop_Run` at 0x140331D2D and `SceneLoop_RunAlt` at 0x14039DE79.
- V: frame layout: three row ids at +0x00, +0x04 and +0x08; the cursor at +0x1C (0..2); the state at +0x20. The creator sets cursor and state to 0 and writes 9 to the first row's sprite-entry field at +0x14.
- V: up is action bit 0xA4 passed through `sub_14037FE58`; down is 0xA5 through the same filter, or a raw `Input_TestAction` of mask 256 on action 0x20. A move writes 0 to the old row's +0x14 and 9 to the new row's +0x14, wraps the cursor 2 to 0 and 0 to 2, and calls `sub_1401D80A8` with command 0x0A and value 3.
- V: confirm tests mask 32 on action 0x1A and mask 2048 on action 0x1F and sends command 0x0A value 1; cancel tests mask 64 on action 0x1B and sends value 2. Both set state 2.
- V: state 2 drops `dword_141876EF8` and `dword_141876F90` by 3, pops itself, clears bit 0x10 of the four sprite entries in the parent frame at +0x04..+0x10, and clears the parent's timer at +0x24. It pushes no id.
- V: the handler starts no fade and reads no movie host. Its effects outside its own frame are the two counters (each down 3), the parent's four row flags and the parent's timer.
- I: the three rows are a submenu page of the four-row menu: the menu's own helper creates it, it edits the parent frame and it only pops (rests on the helper's call and the parent offset arithmetic).
- ?: the labels of the three rows, and what the parent menu's mode 2 means (the parent has no in-binary pusher).

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [sub_1401D80A8](sub_1401D80A8.md)

## Notes

Whole function read (515 bytes); the push site in sub_14037D848 and the caller list were followed. The parent is paged as OpeningMenu_Task.

## Open questions

The three row labels, and whether the parent menu is reachable at all (no store of id 2 was found). The two counters `dword_141876EF8` and `dword_141876F90` have no globals.jsonl record.
