# CrystalAbilityLearning

- **Kind:** flow
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A unit that stops on a Crystal or Chest unit's tile triggers a roll of the abilities the dead unit had learned in jobs the picker has unlocked, a window where a player-controlled unit chooses between learning them and restoring HP and MP, and the application of that choice to the picker's battle record. The roll, the window's list and the application all work on the 19 stock job indices.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [sub_14020B90C](../functions/sub_14020B90C.md) | V | The unit's move ends (battle state 18); the function places the unit and computes the tile flags. |
| <a id="2"></a>2 | [sub_140271AC0](../functions/sub_140271AC0.md) | V | Flag 1 is set when a unit with status Crystal or Chest is on the tile (Battle_IsTileOccupied flag 65); no team test. |
| <a id="3"></a>3 | [sub_14020435C](../functions/sub_14020435C.md) | V | Sets battle state 21 and, for flag 1, runs the roll for the picker (the first scene object's unit) and stores the result pointer. |
| <a id="4"></a>4 | [sub_140271EFC](../functions/sub_140271EFC.md) | V | Rolls each ability the dead unit learned (in a job the picker has unlocked and has not learned) against its learn percent, writing the result block; a chest unit only gets an item id from sub_1402723EC. |
| <a id="5"></a>5 | [sub_1402723EC](../functions/sub_1402723EC.md) | V | Chest only: picks one of the dead unit's valid equipment ids (record +26..+39) or a random fallback id. |
| <a id="6"></a>6 | [sub_140324658](../functions/sub_140324658.md) | I | A player-controlled unit (record +494 has no 0x30 bit and has bit 0x08) gets the crystal window through the message command (mode 2); other units are restored at once with sub_1402722D8 flag 2. |
| <a id="7"></a>7 | [sub_140323D1C](../functions/sub_140323D1C.md) | V | The window lists the abilities from the result block and stores the answer in dword_140D40958: 1 learn, 2 restore, 4 chest item, 0 none. |
| <a id="8"></a>8 | [sub_140237FA4](../functions/sub_140237FA4.md) | V | For message command 105 the answer becomes the choice word xmmword_142FD35A0. |
| <a id="9"></a>9 | [sub_14020BFD4](../functions/sub_14020BFD4.md) | V | State 21 reads the choice word and calls sub_1402722D8 with it, then runs sub_14020435C again for the next pending flag. |
| <a id="10"></a>10 | [sub_1402722D8](../functions/sub_1402722D8.md) | V | Choice 1 ORs the 57 learned-slot bytes into the picker's record at +162 (19 jobs x 3 bytes) and sends the learned-by-succession notification; choice 2 restores HP and MP to full; choice 4 adds the chest item to the inventory. |

## Behavior

- V: the learned bits go into the picker's battle record only (g_PreviewUnitTable); no JP, level or other store is touched by this flow.
- V: a class (job index 24 and up) appears nowhere: the roll walks indices 0..18, the result block holds 19 job entries, and the application loop is 19 x 3 bytes.

## Notes

Evidence: IDA decompile and disassembly of every function above on 2026-11-10; the window's drawing helpers and the write-back of record +162 to the save at the end of a battle were not read.

## Open questions

? where the picker's record +162 bits reach the save after the battle; ? what sets bit 0x08 of record +494.
