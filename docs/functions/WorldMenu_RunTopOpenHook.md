# WorldMenu_RunTopOpenHook

- **Address:** `0x1402D0458`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 WorldMenu_RunTopOpenHook(void)`
- **Callers:** Errand_BoardInput, EventViewer_ListInput, MenuCtl_Entry50, MenuCtl_Entry53, MenuCtl_Entry54, sub_1402D1F24, MenuCtl_Entry44, MenuCtl_Entry45, ClassicMenu_PopTownMenu; a data reference
- **Callees:** indirect: table 0x140681220

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Calls the first-table hook of the world-menu control on top of the control stack (V: callers such as Errand_BoardInput run it right after decrementing the stack depth; I: the hook re-initialises the control that becomes the top one).

## Behavior

- V: the stack depth is `dword_140D8DBA0`; entries are 23 dwords from `dword_140D8D8C0`; the entry's type is `dword_140D4C948[depth-1]`.
- V: it calls entry [type] of the pointer table at 0x140681220 with the address of the top entry and returns its result.
- I: this table holds set-up hooks run when a control becomes the top one again (its entry 5 resets the sprite records, entry 7 stores the OR of the input bits of actions 0x20, 0x1B and 0x1A in `dword_140D498D0` and calls `sub_1402D541C(-1,-1)`); callers invoke it right after popping a level.

## Referenced by

- Called by: [ClassicMenu_PopTownMenu](ClassicMenu_PopTownMenu.md), [Errand_BoardInput](Errand_BoardInput.md), [HelpMessage_Wait](HelpMessage_Wait.md), [MenuCtl_Entry50](MenuCtl_Entry50.md), [MenuCtl_Entry51](MenuCtl_Entry51.md), [MenuCtl_Entry53](MenuCtl_Entry53.md), [MenuCtl_Entry54](MenuCtl_Entry54.md), [PagedText_WaitAndClose](PagedText_WaitAndClose.md), [UiPage_ChoicePromptInput](UiPage_ChoicePromptInput.md)

## Notes

Whole body read; entry 7 is `sub_1402ED500`, read separately (the 0x1A and 0x1B action ids are its operands).

## Open questions

Exact role of the two hook tables.
