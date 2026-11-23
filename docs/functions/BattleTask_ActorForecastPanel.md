# BattleTask_ActorForecastPanel

- **Address:** `0x140229DD4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 BattleTask_ActorForecastPanel(void)`
- **Callers:** No direct code callers. `g_BattleScriptTable` record 5 (0x140672350) slot 2, started by `BattleAction_RunScript` as scene task slot 12 with tag 19; record 5 comes from the script-5 start site `sub_1401FFC48`.
- **Callees:** SceneObject_FindByUnitIndex, Ability_GetAuxRecord, sub_140305264, Battle_ExecuteSecondaryAction (through g_TextCommandSlot), SceneCallback_Dispatch, SceneTask_WaitFrame, sub_140226E44, sub_1400E538C, Battle_UnitStatusFillAlt

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task entry for the battle status panel's acting-unit variant B: refreshes the shared status work area, runs the acting unit's pending secondary action, pre-seeds the panel's projected HP/MP and tail-calls Battle_UnitStatusFillAlt with mode 1.

## Behavior

- V: scene task entry with no direct code caller; `g_BattleScriptTable` record 5 (0x140672350) holds it in slot 2, and `BattleAction_RunScript` starts it as scene task slot 12 with tag 19.
- V: record 5 is the script-5 program; the script-5 start site `sub_1401FFC48` takes that path only when it has a second unit node, otherwise it starts record 2.
- V: the acting slot is the high half of `dword_1407DCF98` and the target slot is `word_1407DCFAA`; a value 0..20 selects a 512-byte record of `g_PreviewUnitTable`, a value above 20 yields a null record pointer.
- V: the acting unit's scene object carries a 20-byte action request at +0x178; the task reads the action type at +0x179 and the ability id from the low 9 bits of the word at +0x17A, and resolves the ability's auxiliary record with `Ability_GetAuxRecord`. It also stores a byte at +0x178; the pseudocode shows an uninitialised register as the source, so that value is not established.
- V: it clears the two five-byte status sets at `g_BattleControl+693675` and +693680, the word at +693392, and the render-manager bytes at +13501 and +13503.
- V: it calls `sub_140305264` on the two unit records; that helper compares their zodiac nibbles and writes a small compatibility code to 0x14186AFFC.
- V: it skips the secondary action for a plain attack (action type 3), or when the word at +0x17A is below 368 and the auxiliary record has bit 2 of byte +5 set; in that case it clears the local result pointer and the +6 qword of both result records.
- V: otherwise it installs `Battle_ExecuteSecondaryAction` in `g_TextCommandSlot` and dispatches mode 3 with the acting record, the target record and the request; the result lands in the target's result record at +0x1BE, whose address it keeps at 0x142FF3CF8.
- V: it waits two frames and then refreshes the shared status work area with `sub_140226E44`.
- V: it sets a flag when the result reports full hit chance (word +44 = 100), HP damage (signed byte +39 negative) and damage at least equal to the target's current HP; `sub_1400E538C` uses the flag to choose between the panel's two GUI state groups at +57624 and +58344.
- V: it computes the acting unit's projected HP and MP as the preview record's current HP/MP (+0x30/+0x34) plus the caster result's heal-minus-damage deltas (+8 minus +6, +12 minus +10), clamped to zero and to the maxima at +0x32/+0x36; the deltas are applied only when `g_BattleCasterResult` is non-null, otherwise the current values are written unchanged.
- V: it writes that pair to the first 212-byte panel block's +208/+210 (screen +65672/+65674) and writes no other panel field before the tail call.
- V: it tail-calls `Battle_UnitStatusFillAlt` with the anchor record at 0x1408081E8, mode 1, `tbl_UiStatusNumbersActorB` and the work area at 0x1407832A0; the anchor's four words are 0x0089, 0x00AA, 0x0023 and 0x0034.
- V: it has no termination of its own; it ends only when `Battle_UnitStatusFillAlt` terminates the scene task.
- I: the anchor is the panel's four-word frame block, origin plus right/bottom extension, the form the fill consumes (rests on the fill's frame arithmetic; the 35x52 extent matches its 33x50 inset plus the 2-pixel border).
- I: the compatibility code at 0x14186AFFC is what the mode-2 fill later reads for its percentage line, so the target panel depends on this call having run (rests on the acting task's call and the mode-2 branch).

## State touched

- Calls: [SceneObject_FindByUnitIndex](SceneObject_FindByUnitIndex.md), [Ability_GetAuxRecord](Ability_GetAuxRecord.md), [SceneCallback_Dispatch](SceneCallback_Dispatch.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [sub_140226E44](sub_140226E44.md), [Battle_UnitStatusFillAlt](Battle_UnitStatusFillAlt.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md), [g_BattleCasterResult](../globals/g_BattleCasterResult.md), [g_BattleActionBlock](../globals/g_BattleActionBlock.md)
- Writes: [g_TextCommandSlot](../globals/g_TextCommandSlot.md), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_BattleControl](../globals/g_BattleControl.md)

## Notes

Whole body read (589 bytes). The battle-side twin of the event-window `MessageWindow_OpenMode1`: same request check, same two-frame wait and the same projected HP/MP pair, a different panel builder and work area. The 78-byte mode-3 wrapper `sub_140229D84` has no page; the four variants belong to the variant registry. Named for what it does: it runs the action preview and projects the actor's HP/MP for the forecast panel.

## Open questions

0x14186AFFC (the compatibility code) and 0x142FF3CF8 (the target result pointer) have no global record. What the panel's GUI states at +57624 and +58344 represent is open; the KO flag's exact purpose (warning or state switch) is not established. The compatibility code is 0..5; what its 0 and 4 values mean is open.
