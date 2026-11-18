# UiEventWindowFontAndNameNodeRun

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1407111B0`
- **Rows:** 2 rows of 8 bytes at the head (the sweep run holds 182 slots)
- **Keyed by:** name slot
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Head list of 2 node name pointers (Normalfont, TextName); the run continues into class vtables (13 class vtables: event, common parts, gil and character number, notice dialog, main menu parts, horoscope affinity, job tree). Verdict: code-table for the whole run, the head is a text pointer list.

## Behavior

- V: the head strings are node names handed to the UI node lookup; the pointers after them are run-time type locators and virtual functions of the UI classes

## Notes

Our names. Tags: V layout, I class use.

## Open questions

- ?: vtable slot meanings of the classes
