# UIMessageBanner_Show

- **Address:** `0x140111D20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIMessageBanner_Show(void *banner, BattleMsgDescriptor *desc, int enable)`
- **Callers:** BattleMsg_BannerHandlerA and BattleMsg_BannerHandlerB (both call it after the agent vfunc +16 returns true); further callers were not enumerated
- **Callees:** BattleMsg_FillArgs, BattleMsg_TextFromDescriptor, sub_14028F728, sub_14028F6AC, GUITextNode_SetTextExpanded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows a message in the centre banner: resolves the banner's 'Title' text node, fills the format arguments and stores the template text, then starts the banner state selected by the dword at banner+80. This is where the banner's text is set.

## Behavior

- V: a1 is the banner object; the function resolves the node named 'Title' under it.
- V: with a non-null descriptor and a non-zero enable, BattleMsg_FillArgs(qword_143CDA388, a1+152, desc) fills the format-argument vector, BattleMsg_TextFromDescriptor(desc) supplies the template text, and sub_14028F728(a1+88, text) stores it.
- V: with a null descriptor or a zero enable, sub_14028F6AC(.., "?") is used instead, so the board shows a question mark.
- V: the banner state comes from the dword at a1+80: 1 ParameterUp, 2 ParameterDown, 3 Item, 4 Trap, 5 TreasureBoxCrystal, 6 DestroySteal, 7 and 8 NineGrid variants. The function starts the selected state.
- V (live read, 2026-10-31): the text node is Widget/LayerCenter/TextBoardAutoText/TextBoardAutoText/LayerRoot/Title in ui/ffto/battle/ffto_battle_menu_info_upper_02.uib.
- V: the text reaches the node through GUITextNode_SetTextExpanded(node, "<string=lstr0>", args), called from inside this function at 0x140111E98; GUITextNode_SetString is then called from inside SetTextExpanded.
- V: the stored value is the template text (for example '<string=lstr0>'), not the expanded string; the arguments are expanded inside the text node.
- I: the name is ours (IDB: sub_140111D20); the role is read from the two handlers that call it after their agent vfunc +16 test.

## State touched

- Calls: [BattleMsg_FillArgs](BattleMsg_FillArgs.md), [BattleMsg_TextFromDescriptor](BattleMsg_TextFromDescriptor.md), [GUITextNode_SetTextExpanded](GUITextNode_SetTextExpanded.md)

## Referenced by

- Called by: [BattleMsg_BannerHandlerA](BattleMsg_BannerHandlerA.md), [BattleMsg_BannerHandlerB](BattleMsg_BannerHandlerB.md), [BattleMsg_ShowPrompt](BattleMsg_ShowPrompt.md)

## Notes

The name is ours (IDB: sub_140111D20). The function is 944 bytes. The banner object is reached as [[[qword_143CD9DA8+16]+72]+88] by the two handlers.

## Open questions

What sets the banner state dword at a1+80; what each banner state does; which code builds the banner descriptor for an ability cast (unknown).
