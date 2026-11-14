# EventUnitObject_ApplyId

- **Address:** `0x140136798`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventUnitObject_ApplyId(void *obj, uint32_t id, uint32_t arg3, uint32_t arg4)`
- **Callers:** EventScript_Run, case 0xE7 (call site 0x14023EE18).
- **Callees:** `sub_1403D325C`, `sub_1403D3AE8`, `sub_1401D1EAC`, `sub_1403D2FD8`, `sub_14013AE64`, `sub_14013AEE0`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up a 4-byte id in table 87 and applies the matching text to the UI sub-object of the object at [[qword_143CD9DA8+16]+104], closing its panel first.

## Behavior

- V: the object is [[qword_143CD9DA8+16]+104] as passed by EventScript_Run. The id is the dword read at instruction offset 1.
- V: does nothing unless the object's +80 pointer (the sub-object) is non-null.
- V: uses the cached table pointer qword_143CDA440. When it is zero it gets table 87 from the root qword_143CD9CD0 with sub_1403D325C (root, 87) and caches it.
- V: when id is nonzero, it fetches the row with sub_1403D3AE8 (table 87, id, arg3, arg4). arg3 and arg4 come from EventScript_Run locals and were not resolved.
- V: when the row exists, and the sub-object's +24 pointer is non-null with byte +74 nonzero and its +48 non-null, it calls sub_1401D1EAC on the sub-object (close the panel) first.
- V: reads the row's 16-bit type code at data +8. Type 115 and type 113 are handled. Other codes do nothing.
- V: type 115: reads the dword at data +12 and looks it up in table 86 (cached in qword_143CDA460, root key 86). When that row exists, it calls sub_14013AE64 on the sub-object with the string at (the row's data + its dword at +8) + 8.
- V: type 113: reads the dword at data +12 and looks it up in table 85 (cached in qword_143CDA318, root key 85) to get row A. String A is row A's data + its dword at +12 + 12. It then reads the dword at row A's +8 and looks it up in table 85 to get row B. String B is row B's data + its dword at +12 + 12, or the default string Str1 when row B is missing. When row A exists, it calls sub_14013AEE0 on the sub-object with string A and string B.
- I: the bodies of sub_14013AE64 and sub_14013AEE0 were only partly read. sub_14013AE64 sets byte +144 of the sub-object's +56 to 1 when the sub-object's +48 is non-null. The text effect of both is not confirmed.

## State touched

- Calls: [sub_1401D1EAC](sub_1401D1EAC.md)

## Notes

The two table-85 and table-86 lookups use the same row-field conventions as table 87, and the text offsets sit at different fields (+8 and +12) for the two type codes.

## Open questions

What sub_14013AE64 and sub_14013AEE0 do with the strings (the text setter used). What arg3 and arg4 are at the 0xE7 call site. Which codes the 115 and 113 type words stand for (the code shows only the numbers).
