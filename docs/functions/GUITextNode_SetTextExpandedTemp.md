# GUITextNode_SetTextExpandedTemp

- **Address:** `0x1403F113C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_SetTextExpandedTemp(__int64 node, _QWORD *text)`
- **Callers:** sub_14010C624, sub_140112E84, sub_140117BEC, sub_140117E1C, sub_14011C940, sub_140135FBC, sub_140136A7C, sub_1401386A4, sub_1401389C4, sub_140139138, sub_14013AE64 and many more
- **Callees:** GUITextNode_SetTextExpanded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets a node's text with expansion using a throwaway, empty argument list that is freed afterwards.

## Behavior

- V: builds an args object on the stack: allocator = qword_143CDAA80[+32] (or 0), begin = end = cap = 0 (an empty vector).
- V: calls GUITextNode_SetTextExpanded(node, text, &args).
- V: if args.begin != 0 afterwards, frees it through allocator vtable slot +24 with size 264 * ((cap - begin) / 264): the args vector has 264-byte elements.
- V: about 90 call sites (JobTreePanel_FillTexts among them).

## State touched

- Calls: [GUITextNode_SetTextExpanded](GUITextNode_SetTextExpanded.md)

## Referenced by

- Called by: [BgmMode_DrawRow](BgmMode_DrawRow.md), [ClassicSubtitles_Step](ClassicSubtitles_Step.md), [EquipDetail_SetHelpText](EquipDetail_SetHelpText.md), [GUITextNode_UpdateLayout](GUITextNode_UpdateLayout.md), [GlossaryList_DrawRow](GlossaryList_DrawRow.md), [GuideWindow_ShowPage](GuideWindow_ShowPage.md), [JournalDetail_Fill](JournalDetail_Fill.md), [JournalList_DrawRow](JournalList_DrawRow.md), [Launcher_DrawInfoPage](Launcher_DrawInfoPage.md), [Launcher_DrawStartPage](Launcher_DrawStartPage.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [UnitPanel_FillJobLine](UnitPanel_FillJobLine.md), [WorldMapBaseList_DrawRow](WorldMapBaseList_DrawRow.md), [WorldMapScreen_SetProgress](WorldMapScreen_SetProgress.md), [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md), [ZodiacStone_FillDetail](ZodiacStone_FillDetail.md), [ZodiacStone_FillTip](ZodiacStone_FillTip.md), [sub_1402A20A4](sub_1402A20A4.md), [sub_1402A6710](sub_1402A6710.md)

## Notes

Use when the text has no arguments but may contain macros.

## Open questions

? contents of a 264-byte arg element.
