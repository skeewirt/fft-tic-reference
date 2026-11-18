# UiRadioButtonNodeNamesRun

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14070FD10`
- **Rows:** 4 rows of 8 bytes at the head (the sweep run holds 659 slots)
- **Keyed by:** name slot
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Head list of 4 node name pointers (RadioButton01 to RadioButton04); the run continues into class vtables (39 class vtables: system message, battle command, warning, announce, battle (continuous, dialog, flytext, join, sortie, result, game over, objective), loading, saving, pause, chapter, event caption). Verdict: code-table for the whole run, the head is a text pointer list.

## Behavior

- V: the head strings are node names handed to the UI node lookup; the pointers after them are run-time type locators and virtual functions of the UI classes

## Notes

Our names. Tags: V layout, I class use.

## Open questions

- ?: vtable slot meanings of the classes
