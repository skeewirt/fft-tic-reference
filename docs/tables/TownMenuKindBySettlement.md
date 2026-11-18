# TownMenuKindBySettlement

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140693530`
- **Rows:** 44 rows of 4 bytes
- **Keyed by:** settlement id (the argument of TownMenu_BuildItems)
- **Read by:** [TownMenu_BuildItems](../functions/TownMenu_BuildItems.md)
- **Row layout:** [TownMenuKind](../structs/TownMenuKind.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per settlement, whether it offers the three-row town menu (Outfitter, Tavern, Warriors' Guild). Verdict: designer-data.

## Behavior

- V: TownMenu_BuildItems tests the 4th byte of the row (== 1) before it lists the three rows and the optional fourth
- I: 44 rows: the next table starts 0xB0 bytes after this one

## Notes

Our names. Found beside the table at 0x140693533; tags V layout, I count.

## Open questions

None recorded.
