# BattleVoice_TickQueue

- **Address:** `0x1401EC6F8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_TickQueue(void *controller, float frameTime)`
- **Callers:** BattleControl_FrameUpdate
- **Callees:** sub_14009C034

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counts down the delays of queued voice cues and plays the ones that are due.

## Behavior

- V: subtracts the frame time from each queued (cue, delay) pair and plays a cue whose delay is at or below 0 through sub_14009C034.
- V: called every frame from BattleControl_FrameUpdate.

## State touched

- Writes: [BattleVoiceController.cue_queue](../structs/BattleVoiceController.md#cue_queue)

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)

## Notes

Name is ours.

## Open questions

None recorded.
