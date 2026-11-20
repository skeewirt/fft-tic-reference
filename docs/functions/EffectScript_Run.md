# EffectScript_Run

- **Address:** `0x14031D658`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char EffectScript_Run(short slot)`
- **Callers:** the effect state machine
- **Callees:** the opcode handlers, reached only through the table (two of them are the callback opcodes documented as EffectScript_OpSetCallback and EffectScript_OpCallCallback)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the opcodes of one effect script until it yields or ends.

## Behavior

- V: the script context of a slot is a 312-byte record (156 words); +6 is the instruction offset and +8 the script base pointer.
- V: loops: opcode = the word at the instruction offset masked with 0x1FF, handler = the 120-slot table (0x1406830F0), called with the context.
- V: a handler result of 0 yields for this frame (the function returns 1), a non-zero result goes on with the next opcode and a result of 2 ends the script (clears the running-script global and returns 0).
- V: when the pause manager flag 8 or the stepping flag 2 is set it restores the saved instruction position afterwards, so a paused script does not advance.

## State touched

- Calls: [EffectScript_OpSetCallback](EffectScript_OpSetCallback.md), [EffectScript_OpCallCallback](EffectScript_OpCallCallback.md)

## Notes

Name is ours. The table has 120 slots although the opcode is masked with 0x1FF.

## Open questions

?: the meaning of the individual opcodes.
