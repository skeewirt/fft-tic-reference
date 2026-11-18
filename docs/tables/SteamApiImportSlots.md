# SteamApiImportSlots

- **Kind:** table
- **Area:** [Application and startup](../areas/app-startup.md)
- **Storage:** Executable
- **Address:** `0x14091F968`
- **Rows:** 11 rows of 8 bytes (the tail of the import table)
- **Keyed by:** import slot
- **Row layout:** [ImportSlotRow](../structs/ImportSlotRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Import address slots of eleven functions of the Steam API library (find or create user interface, unregister call result, context init, get user handle, restart app if necessary, API init, register / unregister callback, shutdown, run callbacks, register call result). Verdict: pointer-table.

## Behavior

- V: filled by the loader; calls reach the library through the slots (first call site in sub_140025D50)

## Notes

Our names. Tags: V.

## Open questions

- I: five more slots of the same import table sit just before this address
