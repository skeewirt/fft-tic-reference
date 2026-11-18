# UiLauncherControllerGuideLabelsRun

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14070A9B0`
- **Rows:** 15 rows of 8 bytes at the head (the sweep run holds 25 slots)
- **Keyed by:** name slot
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Head list of 15 node name pointers (Controller button label nodes (L2, L1, select, d-pad, left stick, L3, R2, R1, right buttons, right stick, R3, start)); the run continues into class vtables (UIAddonFFTOLauncher (second vtable)). Verdict: code-table for the whole run, the head is a text pointer list.

## Behavior

- V: the head strings are node names handed to the UI node lookup; the pointers after them are run-time type locators and virtual functions of the UI classes

## Notes

Our names. Tags: V layout, I class use.

## Open questions

- ?: vtable slot meanings of the classes
