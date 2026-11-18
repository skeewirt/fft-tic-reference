# UiGuideTipPageNamesRun

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14070BF20`
- **Rows:** 6 rows of 8 bytes at the head (the sweep run holds 896 slots)
- **Keyed by:** name slot
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Head list of 6 node name pointers (page01 to page06); the run continues into class vtables (54 class vtables: guide, bar (profit, gossip, main list), menu base, shop, end slate, classic band / loading / subtitles, ending save, bonus item). Verdict: code-table for the whole run, the head is a text pointer list.

## Behavior

- V: the head strings are node names handed to the UI node lookup; the pointers after them are run-time type locators and virtual functions of the UI classes

## Notes

Our names. Tags: V layout, I class use.

## Open questions

- ?: vtable slot meanings of the classes
