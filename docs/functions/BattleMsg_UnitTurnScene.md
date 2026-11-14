# BattleMsg_UnitTurnScene

- **Address:** `0x140237494`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleMsg_UnitTurnScene(void)`
- **Callers:** no direct call site (0 xref); a function pointer from sub_140234468 and four tables (0x140801500, 0x140802AB0, 0x140804060, 0x140805610)
- **Callees:** BattleMsg_SetKind6, SceneTask_Start, SceneTask_Terminate, GUINode_FindState, GUINode_StopState, UIName_Key, sub_1402371F8, sub_14023286C, sub_14022CBE4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task that refreshes the battle message when a unit's turn starts: writes the acting unit's command or ability into record entry 0, starts the message scene tasks and resets the action-list widget states.

## Behavior

- V: the acting unit is g_BattleUnitTable + 512 * SHIWORD(dword_1407DCF98) when the index is at most 0x14.
- V: when unit byte +0x61 has bit 3 set: if byte +0x1A1 maps (through byte_14067E010) to 10, entry 0 becomes kind 5 with id = that byte + 0xB000; otherwise the signed word at unit +0x1A2 is written into entry 0 as kind 6 with id = word + 0x7000 through BattleMsg_SetKind6.
- V: this ability path has no 9-bit mask, so the ability id reaches the banner whole.
- V: the function then stops and starts the action-list widget states (UIName keys ActionListPosition2 and ActionListPosition3), stores qword_140D40940 = sub_1402371F8 and calls it, and runs scene tasks.
- V: 0x434 bytes; no direct call site: its address is loaded in sub_140234468 and stored in the pointer tables at 0x140801500, 0x140802AB0, 0x140804060 and 0x140805610.
- I: it is the scene task behind the unit turn message; the name is ours.
- ?: which scene task invokes it; what unit +0x61 bit 3 is.

## State touched

- Calls: [BattleMsg_SetKind6](BattleMsg_SetKind6.md), [SceneTask_Start](SceneTask_Start.md), [SceneTask_Terminate](SceneTask_Terminate.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_StopState](GUINode_StopState.md), [UIName_Key](UIName_Key.md), [sub_1402371F8](sub_1402371F8.md)

## Referenced by

- Observed behaviours: [SkillsetNamesAndHelpAreKeyedBySetId](../behaviors/SkillsetNamesAndHelpAreKeyedBySetId.md)

## Notes

The name is ours (IDB: sub_140237494). The twin with another message global is sub_1402EB408 (same shape, xmmword_14078D9C0 / byte_14184B2C0).

## Open questions

Which scene task calls it; the role of unit +0x61 bit 3; what sub_1402371F8 does (it writes kind 5 entries from the action list).
