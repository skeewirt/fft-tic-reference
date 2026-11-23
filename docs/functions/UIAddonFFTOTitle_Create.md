# UIAddonFFTOTitle_Create

- **Address:** `0x1401CB9B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `UIAddonFFTOTitle *UIAddonFFTOTitle_Create(UIAgentFFTOTitle *agent)`
- **Callers:** UITitle_ShowMenu
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates and builds the title menu add-on (the screen of uiaddon row 244) and attaches it to the title agent.

## Behavior

- V: `Mem_Alloc(240)` for the add-on, base constructor `sub_14019CD74` (the `UIAddonMenuBase` part), then sets both vtables (primary 0x14070A4B0, and 0x14070A460 at +48 for the `UIFFTOMenuFunctionBase` part).
- V: attaches it with `UIAgent_AttachAddon` and loads its layout with `UIAddon_LoadByRow` (row 244).
- V: the allocation clears +72..+215 (six rows) and +216..+230 (count, current row, last input tick, flags).

## Referenced by

- Called by: [TitleScene_Update](TitleScene_Update.md), [UITitle_ShowMenu](UITitle_ShowMenu.md)

## Notes

Struct: UIAddonFFTOTitle.

## Open questions

None recorded.
