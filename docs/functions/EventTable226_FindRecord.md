# EventTable226_FindRecord

- **Address:** `0x140245A2C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint64_t *EventTable226_FindRecord(uint64_t *out, uint32_t key, uint32_t arg3, uint32_t arg4)`
- **Callers:** EventScript_Run, case 0xC4 (call site 0x14023E2EB).
- **Callees:** `sub_1403D325C`, `sub_1403D3AE8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Looks up one record of table 226 by key and stores the record pointer in the output slot.

## Behavior

- V: sets the output slot *out to 0 first.
- V: uses the cached table pointer qword_143CDA820. When that is zero it gets table 226 from the root qword_143CD9CD0 with sub_1403D325C (root, 226) and caches it. If the table is still missing, nothing else happens.
- V: when the table exists, it stores in *out the result of sub_1403D3AE8 (table, key, arg3, arg4). That is the generic row fetch, and the two extra arguments are passed through.
- V: returns the output pointer.
- I: EventScript_Run sets only the key (edx) before the call (the third operand from opcode 0xC4). The register values for arg3 and arg4 were not set in the disassembly, so their values are unresolved.

## Referenced by

- Reads tables: [NxdDataUISituationSubtitlesShowtime](../tables/NxdDataUISituationSubtitlesShowtime.md)

## Open questions

What arg3 and arg4 hold at the 0xC4 call site, and what sub_1403D3AE8 does with them when the table is in its mode 1 or other modes.
