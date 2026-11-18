# SceneTransition_CheckTables

- **Address:** `0x1402391C4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneTransition_CheckTables(int64_t a1, int64_t a2, int64_t a3, int a4)`
- **Callers:** EventScript_Run (the 0xE3 transition test)
- **Callees:** SceneVar_Write, `sub_140239294`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs a transition check over the scene group tables and, in one case, writes scene variable 39; the value it returns is not used by its caller in EventScript_Run.

## Behavior

- V: when the low dword of qword_142FF9E4C is non-zero and dword_142FF9F4C is non-zero, it writes dword_142FF9F4C to scene variable 39 with SceneVar_Write and returns 1.
- V: otherwise it writes 0 to the byte at qword_143CD9DD0 plus 108.
- V: it then goes through entries 0 to 15 of the table word_140D40040. It stops at the first entry after entry 0 whose value is 0; for each entry it walks the word table word_140D3F550 (indexed by entry value divided by 2), calling sub_140239294 on each record and advancing by the record length from byte_140672140, until the call returns something other than 1.
- V: when a call returns 2 the function returns 1 at once.
- V: when no call returns 2 the function returns 0.
- V: in EventScript_Run the call is part of a comma expression: EventScript_Run sets dword_1407DC494 to 255, calls this function and ignores its result, then tests the result of EventScript_LoadCurrent.

## State touched

- Calls: [SceneVar_Write](SceneVar_Write.md)

## Referenced by

- Reads tables: [TriggerConditionArgCounts](../tables/TriggerConditionArgCounts.md)

## Notes

Its return value is not read by EventScript_Run; only its side effects matter there.

## Open questions

What sub_140239294 returns; what the tables word_140D40040, word_140D3F550 and byte_140672140 contain; what qword_143CD9DD0 plus 108 is.
