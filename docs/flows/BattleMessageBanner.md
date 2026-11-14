# BattleMessageBanner

- **Kind:** flow
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a message descriptor becomes text in the battle's centre banner: a battle handler calls the banner function, which resolves the descriptor to a message id and a template, fills the format arguments, sets the text node's expanded text, and the node is laid out and drawn. The last step is gated: a node whose gate is closed is still called but draws nothing.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 |  | V | A battle message handler calls the banner function (sub_140111D20): the two handlers at sub_1400E8930 / sub_1400E8A84 do so after the agent's vfunc +16 returns true (decompile). |
| <a id="2"></a>2 |  | V | UIMessageBanner_Show (sub_140111D20; proposed name) resolves the node named Title on the banner object (decompile). |
| <a id="3"></a>3 |  | V | BattleMsg_IdFromDescriptor (BattleMsg_IdFromDescriptor): class 0 subtype 2 -> 1000 x kind + (word & 0x7FF) for the kinds in registry BattleMsgKindBase, any other descriptor -> 0xFFFFFFFF (decompile). |
| <a id="4"></a>4 |  | V | BattleMsg_TextFromDescriptor (sub_1400FCBB4): class 0 subtype 2 -> the message text of the id from step 3; class 1 subtype 27 -> UIText_Get(word); class 1 subtype 171 -> the table-172 text of word; anything else null (decompile). |
| <a id="5"></a>5 |  | V | CMesId_GetText (CMesId_GetText) reads the row named by the message id from NXD table 172 through g_CMesIdTable; a missing row gives null (decompile). |
| <a id="6"></a>6 |  | V | BattleMsg_FillArgs (sub_1401EC074) resets the format-argument vector and either calls BattleMsg_BuildArgs for the descriptor or copies up to 40 stored entries from the message object at a 524-byte stride (decompile). |
| <a id="7"></a>7 |  | V | BattleMsg_BuildArgs (BattleMsg_BuildArgs) switches on the message id and pushes the arguments that fill the template's <string=lstrN> and <num=...> markers, read from the battle message record; for message id 10098 the item name, for 10141 and 10145 and up the actor name and a status or ability value (decompile). |
| <a id="8"></a>8 | [GUITextNode_SetTextExpanded](../functions/GUITextNode_SetTextExpanded.md) | V | UIMessageBanner_Show calls GUITextNode_SetTextExpanded with the template and the argument vector at 0x140111E98; it substitutes the arguments into the markers and the node ends with the expanded string (GUITextNode_SetString is called from inside it) (decompile, live trace 2026-10-31). |
| <a id="9"></a>9 |  | V | The banner function stores the expanded text on the node; with no descriptor or with enable clear it stores the literal ? instead. It then picks the banner state from the object's +80 (1 ParameterUp, 2 ParameterDown, 3 Item, 4 Trap, 5 TreasureBoxCrystal, 6 DestroySteal, 7..8 the NineGrid variants) and starts it (decompile). |
| <a id="10"></a>10 | [GUITextNode_Layout](../functions/GUITextNode_Layout.md) | I | The text node is laid out before it is drawn (GUITextNode_Layout); the exact call site in this path was not traced. |
| <a id="11"></a>11 | [GUITextNode_Draw](../functions/GUITextNode_Draw.md) | V | GUITextNode_Draw draws the node; it returns before emitting anything when one of its four gate conditions fails (decompile and disassembly; see the behavior TextNodeDrawGate). |

## Notes

Steps 1-7 name functions whose sheets are separate; the proposed names are used here. M (owner observation 2026-10-31): the same bubble style also serves the level-up banner and the select-a-facing-direction prompt.

## Open questions

? what triggers each of the two battle message handlers; ? the producer of the descriptor for an ability cast; ? whether the state at +80 follows the message kind or the caller.
