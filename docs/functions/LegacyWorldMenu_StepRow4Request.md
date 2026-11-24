# LegacyWorldMenu_StepRow4Request

- **Address:** `0x1402B425C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int16_t LegacyWorldMenu_StepRow4Request(void)`
- **Callers:** LegacyWorldMenu_FrameStep
- **Callees:** WorldMenu_SetFade, sub_1402B340C, sub_14021A030, sub_1402B44A4, LegacyWorldMenu_OpenNode, sub_14033F7B0, memset, sub_1402CD758

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the request of row 4 of the old main world menu (word 0x143749F30) as a counted sequence around a call of sub_14021A030(1).

## Behavior

- V: with the word at 0 it only moves dword 0x142E7FF68 from 1 to 2.
- V: 1: fade 3; 2: waits for mask 0x8 of the state dword; 3: sub_1402B340C, the three dwords = 128, v = sub_14021A030(1), sub_1402B340C again; saves the state dword, sets masks 0x3E70 and selects the node table of the language; v = 1 sets the byte g_GlobalWork +102, any other value reopens node word 0x143749F24 and clears the 0x1E000-byte buffer.
- V: 4..7 count up; 8 restores the state dword and calls sub_1402CD758; later steps clear g_ScreenFadeMode and return to 0 once mask 0x8 is clear.
- V: whenever the byte g_GlobalWork +102 is set at the end it clears the word and that byte and either clears mask 0x1 of the state dword (when dword 0x142E7FF68 was set) or sets mask 0x10000 (bit-set of bit 16).
- ?: what sub_14021A030 runs; the row's purpose is not named here.

## State touched

- Calls: [WorldMenu_SetFade](WorldMenu_SetFade.md), [sub_14021A030](sub_14021A030.md), [LegacyWorldMenu_OpenNode](LegacyWorldMenu_OpenNode.md)

## Referenced by

- Called by: [LegacyWorldMenu_FrameStep](LegacyWorldMenu_FrameStep.md)

## Open questions

None recorded.
