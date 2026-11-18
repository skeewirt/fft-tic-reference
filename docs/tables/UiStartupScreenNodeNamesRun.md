# UiStartupScreenNodeNamesRun

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14070ADB0`
- **Rows:** 3 rows of 8 bytes at the head (the sweep run holds 557 slots)
- **Keyed by:** name slot
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Head list of 3 node name pointers (ShowEnFrDe, ShowJa, ShowTitle); the run continues into class vtables (41 class vtables: startup, text input, poach, employ and item screens, guide). Verdict: code-table for the whole run, the head is a text pointer list.

## Behavior

- V: the head strings are node names handed to the UI node lookup; the pointers after them are run-time type locators and virtual functions of the UI classes

## Notes

Our names. Tags: V layout, I class use.

## Open questions

- ?: vtable slot meanings of the classes
