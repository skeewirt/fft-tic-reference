# SaveLoadList_FillItem

- **Address:** `0x1401864A4`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveLoadList_FillItem(char **item, int *entry, int64_t ctx)`
- **Callers:** UIAddonFFTOSaveLoad_vfunc_7
- **Callees:** GUITextNode_SetTextById, GUITextNode_SetTextFormat, GUINode_FindDescendant, CharaRender_RegisterSlot, UITable_GetRowByKey, NxdTable_GetRowById (and others)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills one save/load list item from an entry: slot number, level, location, next event, date, play time, clear / auto marks, and registers the four preview sprites.

## Behavior

- V: level via `TextBoardNameLv` / `TextLv`, location via the UITable 0x34 row (`text_map`), next event `text_todo`, date from the timestamp (localtime), play time, clear / auto marks.
- V: `CharaRender_RegisterSlot` at 0x140187625, once per sprite record.
- V: nothing in it reads summary bytes +257..+274 (hero name, job).

## State touched

- Calls: [GUITextNode_SetTextById](GUITextNode_SetTextById.md), [GUITextNode_SetTextFormat](GUITextNode_SetTextFormat.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [CharaRender_RegisterSlot](CharaRender_RegisterSlot.md), [UITable_GetRowByKey](UITable_GetRowByKey.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Observed behaviours: [PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow](../behaviors/PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow.md), [SaveCardJobIsTheLeadersPartyJobWordLowByte](../behaviors/SaveCardJobIsTheLeadersPartyJobWordLowByte.md)
- Reads tables: [NxdDataChapter](../tables/NxdDataChapter.md), [NxdDataContinuousSortieConfirm](../tables/NxdDataContinuousSortieConfirm.md), [NxdDataEventId](../tables/NxdDataEventId.md)

## Notes

Written in the 2026-10-29 integration pass from the J7, J8, J9 and W0 research reports; each address was re-checked against the decompile.

## Open questions

None recorded.
