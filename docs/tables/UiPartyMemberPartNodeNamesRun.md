# UiPartyMemberPartNodeNamesRun

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14070DC60`
- **Rows:** 6 rows of 8 bytes at the head (the sweep run holds 353 slots)
- **Keyed by:** name slot
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Head list of 6 node name pointers (six party member part nodes (parts, parts00 to parts04)); the run continues into class vtables (19 class vtables: save / load, system top, subtitles, novel, brave story (Darlavon, trophy, world situation)). Verdict: code-table for the whole run, the head is a text pointer list.

## Behavior

- V: the head strings are node names handed to the UI node lookup; the pointers after them are run-time type locators and virtual functions of the UI classes

## Notes

Our names. Tags: V layout, I class use.

## Open questions

- ?: vtable slot meanings of the classes
