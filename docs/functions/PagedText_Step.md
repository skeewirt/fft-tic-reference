# PagedText_Step

- **Address:** `0x14037A3F0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall PagedText_Step(int *info)`
- **Callers:** EventViewer_EntryPage, MenuCtl_Entry51, PagedText_WaitAndClose, Tavern_RumorTextWait, MenuCtl_Entry27, MenuCtl_Entry25, sub_140376040, Errand_FinishDayPage
- **Callees:** PagedText_DrawPage, Input_TestAction, Input_RepeatDirection, sub_1401D80A8, sub_14037AAFC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame input of a paged message window: confirm turns to the next page, cancel closes it, and holding action 57 scrolls the text line by line.

## Behavior

- V: the state is `info[12]` (info byte 48). Returns 1 while the window stays open and 0 when it has been closed; an unknown state returns 0.
- V: state 0: reads the pressed mask `dword_140D4CC18` and tests actions 26 (confirm, mask 32), 27 (cancel, mask 64) and 57 (mask 128). With neither confirm nor cancel: a press of action 57 sets state 1, copies `info[21]` to `info[22]`, calls `sub_14037AAFC` and sets bit 0x10 on the first sprite record (`info[14]`); otherwise it sets or clears that bit by whether `info[21] >= info[20]`. Returns 1.
- V: state 0, confirm: `info[21] += info[5]`. When cancel is not also pressed and `info[21] <= info[20]` it plays a sound request `(10, 0x2D)` (the id is as the pseudocode shows it; not confirmed at the instruction level), redraws with `PagedText_DrawPage(info, info[21])`, refreshes the bit on the sprite record and returns 1. Otherwise (cancel, or past the last page) it pops the records (`dword_140D4CA00 -= 4`, `--dword_140D4C974`, `dword_140D4C978 -= 5`) and returns 0.
- V: state 1 (action 57 held, read from the held mask `dword_140D4CC1C`): a direction press from `Input_RepeatDirection` moves `info[22]` one line up (when above 0) or down (while below `info[21]`), plays sound `(10, 3)`, redraws that line and calls `sub_14037AAFC`. When action 57 is released it clears `info[24]`, sets state 2 and sets bit 0x10 on the sprite records `info[15]`, `info[16]` and `info[18]`.
- V: state 2: while `info[22] != info[21]` it counts `info[24]` and each frame it reaches 1 it steps `info[22]` up by one and redraws; when equal it returns to state 0 and sets the first sprite record's bit as above.
- I: `info[21]` is the first line of the page being shown, `info[20]` the first line of the last page and `info[5]` the lines per page (rests on `PagedText_Init`).

## State touched

- Calls: [PagedText_DrawPage](PagedText_DrawPage.md), [Input_TestAction](Input_TestAction.md), [Input_RepeatDirection](Input_RepeatDirection.md), [sub_1401D80A8](sub_1401D80A8.md)

## Referenced by

- Called by: [Errand_FinishDayPage](Errand_FinishDayPage.md), [MenuCtl_Entry25](MenuCtl_Entry25.md), [MenuCtl_Entry27](MenuCtl_Entry27.md), [MenuCtl_Entry51](MenuCtl_Entry51.md), [PagedText_WaitAndClose](PagedText_WaitAndClose.md), [Tavern_RumorTextWait](Tavern_RumorTextWait.md)

## Notes

V: whole body read. The name is ours. State numbers are info[12] values.

## Open questions

?: what `sub_14037AAFC` draws and what the 0x10 bit means to the sprite renderer (hidden or shown).
