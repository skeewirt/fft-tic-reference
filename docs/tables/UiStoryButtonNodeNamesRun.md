# UiStoryButtonNodeNamesRun

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14070EEF0`
- **Rows:** 10 rows of 8 bytes at the head (the sweep run holds 451 slots)
- **Keyed by:** name slot
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Head list of 10 node name pointers (ButtonArazlamL00..L02, S00..S03, Darlavon00..02); the run continues into class vtables (27 class vtables: brave story top, achievement notifications, novel manager callback, world map (town / route grow effects, menus, lists, main map, base class), agent). Verdict: code-table for the whole run, the head is a text pointer list.

## Behavior

- V: the head strings are node names handed to the UI node lookup; the pointers after them are run-time type locators and virtual functions of the UI classes

## Notes

Our names. Tags: V layout, I class use.

## Open questions

- ?: vtable slot meanings of the classes
