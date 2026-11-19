# MainTab_SelectTab

- **Address:** `0x1402AC2E8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MainTab_SelectTab(MainTabCtl *ctl, int index)`
- **Callers:** JobTree_RefreshAddon (index 1) and the other screen builders
- **Callees:** GUINode_FindState, GUINode_PlayState, GUINode_StopState, UIName_Key

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the header state that belongs to tab `index` and stops the other three.

## Behavior

- V: the four states are 'Hide02', 'Hide03', 'Hide04', 'Show04' for index 1..4; the selected one gets +104 = 1 and GUINode_PlayState, the others GUINode_StopState.

## State touched

- Calls: [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [GUINode_StopState](GUINode_StopState.md), [UIName_Key](UIName_Key.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md), [sub_140197BCC](sub_140197BCC.md)

## Notes

The Job Tree plays 'Hide02' (only its own title board shows).

## Open questions

What the states change on the boards (not read from the file yet).
