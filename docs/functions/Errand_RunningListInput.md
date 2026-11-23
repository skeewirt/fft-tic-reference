# Errand_RunningListInput

- **Address:** `0x140371174`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_RunningListInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 18)
- **Callees:** sub_14037131C, HelpMessage_Open, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of the list of running errands (table index 18): confirm opens a question about the entry (kind 19), unless the entry is flagged.

## Behavior

- V: cancel sets record dword 0 to 0 and clears 0x140D49628; the help action opens HelpMessage_Open(4194).
- V: confirm on an entry whose byte in the list-flag buffer g_PageListFlags is nonzero plays cue 5 and prints text id 47132; otherwise it sets dword 0 to 1, stores the cursor and starts the close.
- V: after the close it pops; a choice calls sub_14037131C with the entry's number (record + 52 + 4 x row), which pushes kind 19; a cancel re-opens the screen below.
- I: the entries are the errands in progress, because kind 19 edits g_ErrandActive.

## State touched

- Calls: [HelpMessage_Open](HelpMessage_Open.md), [Input_TestAction](Input_TestAction.md)

## Notes

g_PageListFlags is a list buffer shared by several list builders.

## Open questions

None recorded.
