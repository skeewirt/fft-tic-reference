# UnitPanelScriptBlock0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F5118`
- **Rows:** 1 rectangle and 1 script block
- **Keyed by:** block
- **Row layout:** [UiScriptRecord](../structs/UiScriptRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A panel window rectangle followed by a UI script block of the unit panel page (block 0). Verdict: designer-data.

## Behavior

- V: sub_14033AE90 (unit panel page task): passes the block's first eight bytes (or 0x1408F52F8 / 0x1408F5498 / 0x1408F5638 and their +0xD0, +0x1A0 neighbours) as window rectangles to the panel builders
- V: the first eight bytes parse as a rectangle, the next 194 bytes as a complete script (terminator at byte 202); the interpreter is not called from the panel task, so who runs this script is not known

## Notes

Our names. Tags: V rectangle and script shape, ? who runs it.

## Open questions

- ?: who runs the script
- ?: why the block lengths differ (0x1B78 for block 3)
