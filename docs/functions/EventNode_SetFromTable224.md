# EventNode_SetFromTable224

- **Address:** `0x14013B9D4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint64_t EventNode_SetFromTable224(uint64_t node, uint32_t key1, uint32_t key2)`
- **Callers:** EventScript_Run, case 0xC4 (call site 0x14023E339), and sub_140181914 (call site 0x14018196B).
- **Callees:** `sub_1403D325C`, `sub_1403D3B5C`, `sub_1403D2FD8`, `sub_1403F113C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the table-224 entry for two keys and passes its text offset to the GUI target of a UI node.

## Behavior

- V: uses the cached table pointer qword_143CDA450. When it is zero it gets table 224 from the root qword_143CD9CD0 with sub_1403D325C (root, 224) and caches it.
- V: finds the row with sub_1403D3B5C (table, key1, key2). That routine returns nothing for table mode 0, calls sub_1403D4304 with both keys packed as a pair for mode 1, and calls sub_1403D3D58 with key1 and key2 for the other modes.
- V: when a row is found, its data pointer is the sentinel 0x1406F5ED0 when the row's first qword is negative. Otherwise the data pointer comes from sub_1403D2FD8.
- V: calls sub_1403F113C with two arguments: the object at +56 of the node, and the address inside the row data at the offset stored at data +4, plus 4.
- V: the routine returns the result of sub_1403F113C.
- I: when no row is found, the data pointer stays null and the code still reads the dword at address 4 of it. The decompile shows that path, so a missing row would fault unless the table is always present. This was not checked.

## Notes

The node is the object at [[qword_143CD9DA8+16]+368]+64 as passed by the 0xC4 handler.

## Open questions

Whether the no-row path is reachable, and what sub_1403F113C does with the text offset (it was not read).
