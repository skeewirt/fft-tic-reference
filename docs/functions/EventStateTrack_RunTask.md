# EventStateTrack_RunTask

- **Address:** `0x140234E04`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventStateTrack_RunTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x1D
- **Callees:** SceneTask_WaitFrame, SceneTask_Terminate, `sub_1402202C8`, `sub_1402203AC`, `sub_1402404CC`, `sub_140240438`, `sub_14024075C`, `sub_140235180`, memset, EventScript_InstructionLength

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x1D: turns the 0x19 instructions of the block up to the next 0x1E into seven piecewise tracks, one per state value, and plays them frame by frame until the last track ends or the skip test fires.

## Behavior

- V: tags its task slot with the value 4 in `qword_140D40B38[256 * index]`, the same tag value as the 0x19 task.
- V: allocates a 1148-byte block with `sub_1402202C8` and zeroes it with memset. The block holds seven tracks of 41 dwords (164 bytes each), one per state value.
- V: walks the instruction stream from its operand pointer to the first 0x1E byte, counting the 0x19 instructions; the segment count is that count plus one, stored at dword 32 of each track.
- V: sets `dword_142FEC53C` to the 4096-unit window base that contains the current angle (state index 30), searching windows from -16384 up to 12288.
- V: segment 0 starts from the current state: each track's dword 1 is set to the current value, divided by 1024 for the first three values.
- V: then it runs the block's instructions in order and records one segment per 0x19. For each of the seven values the target is the operand word, or for 10000 the running last-target value (divided by 1024 for the first three). Each segment stores a frame stamp equal to the previous stamp plus the 0x19 step count (operand word 7), and the target.
- V: for the angle (index 4) the window base `dword_142FEC53C` is updated from the target.
- V: opcode 0x1F is handled by `sub_1402404CC`: it resolves two unit ids; when either is missing it overwrites the opcode byte of the following 0x19 with 0xC0, which disables that instruction in the script bytes; otherwise it writes the next 0x19's three position targets from the two units' positions.
- V: opcode 0x73 is handled by `sub_140240438`: the next 0x19's seven targets become its own seven operand words added to the running values, with 10000 kept as is.
- V: opcode 0x38 is handled by `sub_14024075C`: it computes a frame count from the square root of a sum of squared differences, divided by its own signed 16-bit operand, and writes it to the following 0x19's frame count (operand bytes 15 and 16).
- V: other opcodes in the block are skipped by their length with EventScript_InstructionLength.
- V: each frame it evaluates the seven tracks with `sub_140235180` (indices 0 to 2 only when `word_140D4090C` is zero) and writes the results to the state entries 26 to 32.
- V: when the skip test fires, it sets the track 3 done word (dword 163, which is the last dword of track 3) to 1 and ends after that update; when that word is already 1 it ends; otherwise it clears bit 0 of state entry 32 and waits one frame with SceneTask_WaitFrame.
- V: `sub_140235180` returns the current value of one track in state units. Each call advances a frame counter; when the current segment is used up it moves to the next, and when it passes the last segment it sets the track done word (dword 40 of the track). Track 3's done word is the end condition of this task.
- V: the task ends by freeing its block with `sub_1402203AC` and calling SceneTask_Terminate.
- I: each segment uses three frame stamps and three values (at 4k, 4k+4, 4k+8 and 4k+1, 4k+5, 4k+9), so the tracks are piecewise quadratic through a middle value; this layout was read from `sub_140235180` and not fully traced.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md), [EventScript_InstructionLength](EventScript_InstructionLength.md)

## Referenced by

- Started by event opcodes: [0x1D](../opcodes/README.md)

## Notes

The opcode record for 0x1D (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

The exact field layout of a track segment and the curve used by `sub_140235180`, the angle values that `sub_1402404CC` writes when its mode byte is zero (two helpers not traced), and the meaning of `word_140D4090C`.
