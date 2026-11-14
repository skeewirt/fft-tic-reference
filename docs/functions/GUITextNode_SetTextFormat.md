# GUITextNode_SetTextFormat

- **Address:** `0x1403F1004`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUITextNode_SetTextFormat(__int64 node, char *fmt, ...)`
- **Callers:** UIAddonFFTOBattleMain4_vfunc_4, sub_140108828, sub_140109134, sub_14010ABE4, sub_14010C624, sub_14011C940, sub_14014B4B8, sub_14014C224 and more
- **Callees:** sub_140026084, GUITextNode_SetString

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

printf-style setter: formats into a 2048-byte stack buffer and sets the node string.

## Behavior

- V: Buffer[2048]; sub_140026084(Buffer, 0x800, fmt, va) (a vsnprintf-style call, limit 0x800).
- V: returns GUITextNode_SetString(node, Buffer).
- V: no placeholder / macro expansion here (compare GUITextNode_SetTextExpanded).
- V: used by battle UI (UIAddonFFTOBattleMain4_vfunc_4 x3), sub_140108828, sub_140109134, sub_14010ABE4 and others (numbers in HUDs).

## State touched

- Calls: [GUITextNode_SetString](GUITextNode_SetString.md)

## Referenced by

- Called by: [SaveLoadList_FillItem](SaveLoadList_FillItem.md)

## Notes

Truncates at 2047 characters (I: limit passed is 0x800 including terminator).

## Open questions

? whether sub_140026084 always terminates on truncation.
