# NxdTableRebinding

- **Kind:** observed behaviour
- **Scope:** loaded nxd tables and the localized reload
- **Area:** [Resource](../areas/resource.md)
- **Affects:** [NxdHandle_OnLoaded](../functions/NxdHandle_OnLoaded.md), [Callback_InvokeWithHandle](../functions/Callback_InvokeWithHandle.md), [NxdTable_CreateHandle](../functions/NxdTable_CreateHandle.md), [NxdTable_BindRows](../functions/NxdTable_BindRows.md), [NxdTable_OnReady](../functions/NxdTable_OnReady.md), [ResourceManager_ReloadLocalized](../functions/ResourceManager_ReloadLocalized.md), [TextLanguage](TextLanguage.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An nxd table can take a new file while the game runs: its load callback NxdTable_BindRows may run again on a bound table, and the game's own language switch reloads every localized handle through it.

## Behavior

- V: NxdTable_CreateHandle builds a 168-byte NexResourceHandle: flags +92 |= 0x2008 (bit 3 = 8 is the flag the language reload selects); +96 / +112 the invoker (Callback_InvokeWithHandle) and NxdTable_BindRows with the table object as context; +128 / +144 the invoker and NxdTable_OnReady (sets the table's state +12 to 2 when the handle's load status +80 is 1, else 3).
- V: NxdHandle_OnLoaded (NexResourceHandle vtable 0x140721600 slot 8) calls the invoker at +96 with (context, &callback at +112, &handle), so the load callback runs as NxdTable_BindRows(table, handle).
- V: NxdTable_BindRows frees and reallocates the entry array only when the new row count is larger, otherwise rewrites the entries in place; a table without the contiguous-keys flag has its lookup arrays freed and built again on use.
- V (seen live 2026-11-14): an item name table bound again at the title screen showed the new name in the Outfitter Buy list and the main menu Inventory list on the next screen (item names are read from the bound table when a list is drawn, not cached at start), also after four rebinds in one session; no crash.
- V (seen live): the weapon power the Outfitter's detail panel shows is read from the weapon record (through the weapon record lookup, 0x1402B8C74) when the panel is drawn: a changed record at the title screen showed on the next visit.
- V (IDA, 2026-11-21): the weapon record lookup (0x1402B8C74) is the only code that reads the weapon record table (0x14080F690, 128 x 8 bytes): one rip-relative lea at 0x1402B8CBC; no other instruction or data reference reaches the table, image-base relative or not.
- I: ResourceManager_ReloadLocalized walks the resource hash for handles with flag 8, so a language change reloads the nxd tables through this path; the code says yes, it was not traced live.

## Open questions

None recorded.
