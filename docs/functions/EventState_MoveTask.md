# EventState_MoveTask

- **Address:** `0x14023F520`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventState_MoveTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x19
- **Callees:** SceneVar_Read, SceneVar_Write, SceneTask_WaitFrame, SceneTask_Terminate, `sub_140380310`, `sub_140380208`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x19: moves up to seven state-block values toward the operand targets over the operand step count, then writes the final values and ends.

## Behavior

- V: tags its task slot with the value 4 in `qword_140D40B38[256 * index]`, where index is `dword_140D40948`.
- V: reads eight signed 16-bit words from the operand bytes at the task block pointer: words 0 to 6 are targets for state-block indices 26 to 32 (through the table `word_1406726B0`), and word 7 is the step count.
- V: a target of 10000 leaves that value unchanged.
- V: reads the global `dword_142FEC520`: bits 0-1 select a curve mode (1 uses one formula, other non-zero values another), bits 2-3 select a second mode, and bits 4-7 give a weight from 0 to 15.
- V: when `dword_142FF8280` is non-zero it clears it, reads scene variable 30, and writes back that value or the value plus 4096, whichever is nearer to target word 4 (an angle unwrap).
- V: reads the current values of the seven state entries; the first three are converted to 1/256 units by clearing their low 12 bits and dividing by 4.
- V: for each step and each of the seven values it skips a value whose target is 10000, and skips the first three values too when `word_140D4090C` is non-zero; it also leaves a value alone when it is within 1536 units (6 in whole units) of its target for the first three, or within 96 units for the others.
- V: otherwise it computes the new value by linear interpolation (`current + (target - current) * step / steps`, through `sub_140380310`) for mode 0, and by the curve formulas of the other modes, which use the weight and the step count.
- V: each step clears bit 0 of state entry 32, then waits one frame with SceneTask_WaitFrame. The loop stops early when the high dword of `qword_142FF9E08` is non-zero and the high dword of `qword_142FF9E00` equals 3, which is the skip test the interpreter uses.
- V: at the end, when `word_140D4090C` is zero, targets 0 to 2 are written to state indices 26 to 28 shifted left by 10; targets 3 to 6 are written to indices 29 to 32 unshifted; then bit 0 of index 32 is cleared, one frame is waited, and the task ends through SceneTask_Terminate.
- I: the first three state values carry 10 fractional bits and the other four are whole values, which matches the shifts above.
- I: `sub_140380310` and `sub_140380208` are signed (a * b) / c helpers, inferred from their 64-bit product and division loops; `sub_140380310` sets `dword_140D4093C` on some negative results (not fully traced).

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x19](../opcodes/README.md)

## Notes

The opcode record for 0x19 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the seven state indices are in scene terms (camera, actor or screen), which curve each mode bit selects, and the exact formulas of the two curve modes.
