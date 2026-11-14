# BattleFaceIsThePoolSpriteByte

- **Kind:** observed behaviour
- **Scope:** engine (battle faces)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_14026E838](../functions/sub_14026E838.md), [sub_14022AA88](../functions/sub_14022AA88.md), [sub_140214134](../functions/sub_140214134.md), [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md), [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md), [sub_1402DF374](../functions/sub_1402DF374.md), [sub_1401F3858](../functions/sub_1401F3858.md), [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle unit's face is not a portrait code: the look pool's sprite byte is stored as the pool's face value and ten readers use it as the face number behind the 0xCD cap; a separate code exists only for one special unit.

## Behavior

- V: sub_14026E838 stores the scene unit's byte +0xA into g_LookPoolFaceValue[pool index] in both branches; sub_140210AF0 clears the ten dwords to -1; Battle_SaveCapture and Battle_RestoreCapture copy them (sub_140304BEC).
- V: readers: sub_1401F3858, sub_140214134, TurnPanel_SetUnitPanel, TurnPanel_SetTag, Battle_UnitStatusFillAlt and sub_1402DF374 take it as the face when the unit's code is -1 and cap it at 0xCD (above: -1); sub_140221798 returns it; sub_14021FA50 hands it raw to the dialogue slot writer; sub_140338A28 and sub_1403980AC write it to g_DialogueFaceSlot0 and g_HdFaceSlotValues.
- V: the code comes from sub_14022AA88 only for a unit whose +401 equals byte_140C6AD76 (code byte_140C6AD7A); the 0x9F guards of five readers (0x140214188, 0x1402150B4, 0x14021569D, 0x14022994C, 0x1402E0556) test that code, never the pool value.
- I: so in battle numbering a stock look's face number is its sprite number (0..169); a sprite of 170..205 would draw the stock face of that number and 206..254 no face.
- V (live 2026-11-10): the battle portraits are UI faces (FaceTexture_FormatName, the same wldface part files as the menus), not g2d entries: the active-unit panel through Battle_UnitStatusFill -> sub_140214134(slot, colour), the turn order through TurnPanel_SetTag's inline copy (face in ebx after the cap at 0x1402157A0, slot in r13), the panel of a unit under the cursor through Battle_UnitStatusFillAlt's inline copy (face in r11d and edx at 0x140229A5E, slot = word +0xA of argument 4 saved at rsp+0x6C; sub_1402DF374 the same at 0x1402E0668), TurnPanel_SetUnitPanel's at 0x1402151B3 (edi; slot saved at rsp+0xB0).
- V: the store indexes the ten dwords by the pool index, which runs to 14: pools 10..14 store past the table (0x1437A5A08..0x1437A5A18).

## Open questions

None recorded.
