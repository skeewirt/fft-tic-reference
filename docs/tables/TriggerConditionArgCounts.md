# TriggerConditionArgCounts

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140672140`
- **Rows:** 40 rows of 1 bytes
- **Keyed by:** trigger condition opcode (u16 word of a condition record)
- **Read by:** [SceneTransition_CheckTables](../functions/SceneTransition_CheckTables.md)
- **Row layout:** [TriggerConditionArgCount](../structs/TriggerConditionArgCount.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Argument count per trigger-condition opcode of the battle event condition lists. Verdict: engine-data.

## Behavior

- V: advance = table[opcode] + 1 words (V); evaluator handles opcodes 1, 4..8, 0x0B, 0x16, 0x18..0x25 (V); 40 bytes up to the next symbol
- V: SceneTransition_CheckTables: steps through each of up to 16 condition lists (word_140D3F550 via offsets word_140D40040), evaluating one condition with sub_140239294 and advancing by 1 + argc words while the result is 1 (and)

## Notes

Our names. Tags: V.

## Open questions

- ?: exact count: last evaluated opcode is 0x25 (38 entries); the remaining 2 bytes up to the next symbol may be padding (I)
