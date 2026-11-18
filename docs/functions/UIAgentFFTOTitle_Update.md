# UIAgentFFTOTitle_Update

- **Address:** `0x1401C2D60`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgentFFTOTitle_Update(UIAgentFFTOTitle *agent, ...)`
- **Callers:** `sub_1401C2D20` (one site)
- **Callees:** SaveSlots_LoadFromFile, sub_1400C4214, SaveSlot_LoadToLive, sub_140257354, sub_1402D03D8, TitleMenu_Build

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The title agent's state machine (state byte at +88): builds the menu, runs the fade-driven transitions and starts the loads the menu rows choose.

## Behavior

- V: one state (case 4) calls the manual-slot loader (`SaveSlots_LoadFromFile`), which is what makes the whole 50-slot image resident when the title menu opens.
- V: the load state calls the slot loader and, when the slot's situation byte at `+282` is 1, the resume materialiser instead of a plain load.
- V: it also requests the resume parts and runs the post-load reconciliation step.
- V: it calls `TitleMenu_Build` to set up the menu rows from the files that exist.
- V: Continue's save language check opens a confirm dialog with `UIAddon_PauseSetup(*(root agent)+128, 3, 0, {callback, context, callback2}, 0, 0)`, passing 0x1401CCB40 and 0x1401C3494.
- I: it compares the five 264-byte records from agent +164 (resume descriptors) when Continue is chosen.

## State touched

- Calls: [SaveSlots_LoadFromFile](SaveSlots_LoadFromFile.md), [sub_1400C4214](sub_1400C4214.md), [SaveSlot_LoadToLive](SaveSlot_LoadToLive.md), [sub_140257354](sub_140257354.md), [TitleMenu_Build](TitleMenu_Build.md)

## Referenced by

- Called by: [UIAgentFFTOTitle_Tick](UIAgentFFTOTitle_Tick.md)

## Notes

This name replaces an earlier one (`sub_1401C2D60`, a sheet that described it as a save list screen). Its owner is the title agent, so the title menu, not a save list, is its screen.

## Open questions

? the full state table (only the load states were read).
