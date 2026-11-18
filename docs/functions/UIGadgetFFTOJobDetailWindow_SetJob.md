# UIGadgetFFTOJobDetailWindow_SetJob

- **Address:** `0x1402A7474`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `char UIGadgetFFTOJobDetailWindow_SetJob(UIGadgetFFTOJobDetailWindow *w, JobDetailRec *rec)`
- **Callers:** sub_140132B34 (record copy; called from JobList_StoreCell twice, sub_14012FC6C twice, sub_1401312C8)
- **Callees:** GUITextNode_SetTextById, JobTreePanel_FillTexts, sub_14029BCD4, UIName_Key, GUINode_StopState, GUINode_FindState, GUINode_PlayState, sub_1400F638C, Str_Format, AbilityTable_GetRow, GUITextNode_SetString, vtable +64

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the job detail window for one job record: the name / level texts, the job icon, the Show / Hide / ShowNext states and the up to four innate ability slots (Sp0..Sp3, with Good / Bad colouring); then calls virtual +64 so the derived class can add its own arguments.

## Behavior

- V (arguments): rec is a 148-byte-style record built by sub_140132B34 from the job list addon record at addon+8832+148*cursor (+19016): copies +0..63 and +64..87, qword +92 (the icon record: dword id, byte hide), byte +100 = addon+19032, byte +101 = source +141 (the 'showUse' byte, see JobTree_FillJobRecords), byte +102 = source +140, byte +103 = (addon byte +19012 is 1, 2 or 3). In the window: rec+68 = job level, rec+72 = job id, rec+92 = icon, rec+101 / +102 = show flags, rec+103 = blank flag.
- V (rec+103 != 0, 'blank'): for the four text bindings at w+80, +184, +288, +392 (104 bytes each: +16 node, +32 string, +64 argument vector, +96 text id) the string is emptied, the argument vector reset (end = begin), the text id = 80 ('--' per JobTreePanel_FillTexts) and, when the node exists, GUITextNode_SetTextById(node, 80, args). The binding pointer array at w+664 / +672 / +680 is zeroed. Skips the state code and goes on to FillTexts.
- V (rec+103 == 0): text ids are set to 3882 (binding 0, w+176), 1021 (binding 1, w+280) and 1023 (binding 3, w+488); binding 2 (w+384) gets 1022 when rec+68 (level) < 8, otherwise its string is emptied, its id is 80 and the text is set to '--' (and its pointer slot is 0). The binding pointers w+664 = binding 0, +672 = binding 3, +680 = binding 1, +688 = binding 2 (or 0).
- V: then JobTreePanel_FillTexts(w+24, w+648, rec, 0) fills the level texts from the record, and sub_14029BCD4(w+496, rec+92, 0) sets the job icon.
- V (node w+40): stops 'Hide' / 'Show' and plays 'Show' when rec+101 != 0 else 'Hide' (state +104 = 1, GUINode_PlayState). Node w+64: plays 'ShowNext' (found by FindState). Node w+72: sub_1400F638C(node, rec+102, 0, 0, 0) = show / hide that node (Show / Hide states, animated).
- V (innate abilities, only when node w+32 exists): the job id rec+72 (>= 0xAE is replaced by a dummy pointer) indexes g_JobTable (0x140785E30, 49-byte rows): the pointer used is row + 1 = the four u16 innate ability ids (the JobTable layout). For j = 0..3: stops state 'Sp<j>' on node w+32; when the id != 0: sets the ability name string into the name node at w+704+16*k (k = count of non-zero ids so far, AbilityTable_GetRow(id): string at row + *(int)(row+8) + 8; the node's text-id dword +248 is cleared and its dirty byte +316 set first) and plays 'Good' or 'Bad' on the node at w+696+16*k ('Good' when the ability row's dword +48 equals 2, else 'Bad'); k += 1. Empty ids are skipped, so the shown abilities are packed.
- V: after the loop plays state 'Sp<k>' on node w+32 (k = number of shown innate abilities, 0..4), then calls virtual +64 of the window (a1, rec) (UIGadgetFFTOJobDetailWindowWithButton slot 8 = sub_1402A7C38 passes the job id and a flag as text arguments).

## State touched

- Calls: [GUITextNode_SetTextById](GUITextNode_SetTextById.md), [JobTreePanel_FillTexts](JobTreePanel_FillTexts.md), [sub_14029BCD4](sub_14029BCD4.md), [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [Str_Format](Str_Format.md), [AbilityTable_GetRow](AbilityTable_GetRow.md), [GUITextNode_SetString](GUITextNode_SetString.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Reads tables: [JobTable](../tables/JobTable.md)

## Notes

Name proposed (IDB: sub_1402A7474). This is what the hover shows beside the job list: job name / level texts, the job icon, and the job's four INNATE ability names (JobTable row + 1) with a Good / Bad frame. 'Sp<k>' state selects the layout for k slots. The text ids 3882 / 1021 / 1022 / 1023 are UI-table ids (strings not read here).

- V (2026-10-29): one of the 15 JobTable bound-readers (the `0xAE` guard at 0x1402A7765); it reads the whole 49-byte row (all 23 fields: stats, innate abilities, equipment, statuses, elements) through the table pointer.

## Open questions

? the text strings behind 3882, 1021, 1022, 1023 and which binding is the job name. ? why the level threshold is 8 (rec+68 < 8: text 1022 shown, else '--': likely 'next level / master' text). ? the meaning of rec+100 (addon+19032), +102 and +103 (addon state byte 1..3). ? which window classes use the base implementation versus the WithButton override.
