# LegacyWorldMenu_StepRosterRequest

- **Address:** `0x1402B4038`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void LegacyWorldMenu_StepRosterRequest(void)`
- **Callers:** LegacyWorldMenu_FrameStep
- **Callees:** WorldMenu_SetFade, WorldMapAgent_IsMapShown, sub_1400EDCB4, sub_1402B340C, sub_1402B803C, sub_1402B44A4, LegacyWorldMenu_OpenNode, sub_14033F7B0, sub_1402B8690, sub_1402CD758

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the roster request of the old world menu (request word 0x143749F28, set by row 1 of node 4) as a counted sequence: fade out, run the roster, reopen the menu node, fade back.

## Behavior

- V: 1: word 0x143749F20 = 1, fade 3 and, with the world map shown, sub_1400EDCB4(9); 2: waits for mask 0x8 of the state dword to clear, then g_ScreenFadeMode = 1.
- V: 3: sub_1402B340C, the three dwords 0x140789368 / 6C / 70 = 128, then sub_1402B803C (I: the roster itself). Unless the byte g_GlobalWork +102 is set it reopens node word 0x143749F24 (LegacyWorldMenu_OpenNode), selects the node table of the language, saves the state dword to 0x143749F54 and sets its masks 0x3E70, clears a 0x1E000-byte buffer and calls sub_1402B8690.
- V: 4..7 count up with g_ScreenFadeMode = 1; 8 restores the saved state dword and calls sub_1402CD758; from 9 on, each pass counts up to at most 11 (reaching 10 clears g_ScreenFadeMode) and, in the same pass, returns the word to 0 once mask 0x8 is clear, so the reset can come at 9 or 10.
- V: the abort dword 0x143749F40 clears the word at any step.
- V: LegacyWorldMenu_MainMenuTask ends once this word reaches 9.

## State touched

- Calls: [WorldMenu_SetFade](WorldMenu_SetFade.md), [WorldMapAgent_IsMapShown](WorldMapAgent_IsMapShown.md), [LegacyWorldMenu_OpenNode](LegacyWorldMenu_OpenNode.md)

## Referenced by

- Called by: [LegacyWorldMenu_FrameStep](LegacyWorldMenu_FrameStep.md)

## Open questions

None recorded.
