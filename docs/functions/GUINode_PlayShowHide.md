# GUINode_PlayShowHide

- **Address:** `0x1400F638C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int *GUINode_PlayShowHide(GUINode *node, char show, unsigned char instant, const char *showName, const char *hideName)`
- **Callers:** about 70 sites (EquipDetail_Refresh, JobTree_SetPanelRecord, WorldMapScreen_BindNodes and many panels)
- **Callees:** UIName_Key, GUINode_StopState, sub_140409824, sub_14002620C, memset, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays a node's Show or Hide animation (default state names 'Show' and 'Hide'): stops the opposite one and starts the wanted one, optionally jumping to its end frame.

## Behavior

- V: node == 0 does nothing. Copies showName (default 'Show') and hideName (default 'Hide') into two 260-byte local buffers (memset 0x104; sub_14002620C copy, max 259).
- V: the state stopped first is: show == 0 -> the Show buffer, show != 0 -> the Hide buffer. The state then played (UIName_Key + sub_140409824(node, key, (instant ^ 1) - 1)) is: show == 0 -> the Hide buffer, show != 0 -> the Show buffer (as decompiled: v11 = a2 ? Hide-buffer : Show-buffer is stopped, v12 = a2 ? Show-buffer : Hide-buffer is played).
- V: sub_140409824(node, key, frame): find state, +104 = 1, GUINode_PlayState, then frame < 0 -> the state's own value at +88 (its length), else min(frame, +88); that value is stored as float at +80 and +84, and /60.0 at +76; +106 = 1. (x ^ 1) - 1 is 0 for instant = 1 and -1 for instant = 0; so instant = 1 passes frame 0 and instant = 0 passes -1 (the state's own value). Which of these is 'jump to end' versus 'play from start' depends on what the +80 / +84 / +76 fields mean (I: current frame / duration), not decoded.
- V: both element keys are released.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md), [sub_14002620C](sub_14002620C.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [JobList_ApplyCellRecord](JobList_ApplyCellRecord.md), [TavernRumourPage_Show](TavernRumourPage_Show.md), [sub_1402A20A4](sub_1402A20A4.md)

## Notes

JobTree_SetPanelRecord uses it for each job panel's Show / Hide. The 'instant' parameter jumps the animation to its end frame (frame = state length), i.e. it makes the panel appear / disappear with no visible fade.

## Open questions

? the exact start-frame rule for sub_140409824 when a3 >= 0 (min with the state length at +88; read from the decompile, not the disassembly).
