# LegacyWorldMenu_FrameStep

- **Address:** `0x1402B4710`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int LegacyWorldMenu_FrameStep(int64_t a1, int buttons)`
- **Callers:** SceneLoop_Run, sub_140342448
- **Callees:** Input_ActionBit, LegacyWorldMenu_StepRosterRequest, WorldMenu_SetFade, sub_1402B340C, LegacyWorldMenu_StepRow4Request, sub_1402F41D0, sub_1402DEAF8, sub_1402BA660, sub_1402D7954, EventTask_WaitFrame, SoundCue_Play, EventVar_Write

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame step of the old world menu: builds the repeated input, blocks it while a request is pending, runs the request sequences and turns the request words into state bits of the classic menu state dword 0x141D32E14.

## Behavior

- V: builds the repeat input from the preset row (dword 0x140782A24 >> 9 & 7) of tbl_InputRepeatPresets and actions 33, 34, 35, 36, 45, 46 and 30, then masks it with dword 0x140808F14.
- V: while any of the six request words 0x143749F28, F2C, F30, F34, F38, F3C is nonzero the pressed-input word is cleared (no input reaches the nodes).
- V: with mask 0x1 of the state dword set and the byte g_GlobalWork +100 set it starts the abort: input cleared, dword 0x143749F40 = 1.
- V: calls LegacyWorldMenu_StepRosterRequest (word F28) and LegacyWorldMenu_StepRow4Request (word F30).
- V: word F34: 1 starts fade 3 (WorldMenu_SetFade) and goes to 2; 2 waits until mask 0x8 of the state dword clears; 3 runs sub_1402B340C and sets state mask 0x100, then 0. ClassicMenu_HubStep opens kind 28 for mask 0x100.
- V: word F2C: the same three steps; the last runs sub_1402B340C, sets state mask 0x100000 and the three dwords 0x140789368 / 6C / 70 to 128. ClassicMenu_HubStep opens kind 43 for it.
- V: word F38 = 1: sub_1402B340C, state mask 0x800000, the three dwords 128, word 0 (no fade). ClassicMenu_HubStep opens the event variable editor for it (EventVarEditor_Open).
- V: word F3C = 1: sub_1402B340C, then sub_1402F41D0(39, 83968 or 67584 by language, 0x143749F70) and sub_1402DEAF8 on that block, state mask 0x1000000, the three dwords 128, word 0. ClassicMenu_HubStep calls PartyLoader_OpenPrompt for it.
- V: the state masks are set and cleared with bit-set / bit-clear instructions by bit number (bits 8, 20, 23, 24 = masks 0x100, 0x100000, 0x800000, 0x1000000).
- V: during the abort each word is cleared together with its state mask (0x100, 0x100000, 0x800000, 0x1000000); then a fade 6, sub_1402BA660(8) and the state dword set to exactly 0x40000000.
- V: at the end it copies the input to the five input words, records the 15 task-state bytes, waits a frame, plays sound cue (dword 0x14078D638 - 1) when that word is not -1, and, when mask 0x40 of dword 0x1437FC2C0 is clear and the word 0x14078DA40 is 0 (a close left from slot 8), writes event variable 51 from word 0x14078DA42 and sets state mask 0x4000; with mask 0x40 set it sets the word to -2 instead. It returns that word (-2 when nothing was closed).
- I: the request words are set by the one-line node tasks (LegacyWorldMenu_RequestRoster and its siblings) when a row of node 4 is confirmed.

## State touched

- Calls: [LegacyWorldMenu_StepRosterRequest](LegacyWorldMenu_StepRosterRequest.md), [WorldMenu_SetFade](WorldMenu_SetFade.md), [LegacyWorldMenu_StepRow4Request](LegacyWorldMenu_StepRow4Request.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [SoundCue_Play](SoundCue_Play.md), [EventVar_Write](EventVar_Write.md)

## Notes

Mask names follow ClassicMenu_HubStep. Words F28 (roster) and F30 are handled by their own step functions; this function only blocks input for them.

## Open questions

None recorded.
