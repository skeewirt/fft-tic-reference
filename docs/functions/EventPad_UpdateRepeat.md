# EventPad_UpdateRepeat

- **Address:** `0x1402EBDE0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventPad_UpdateRepeat(void)`
- **Callers:** EventTask_Terminate, EventTask_WaitFrame
- **Callees:** `sub_1400F6C8C`, `sub_1400FC598`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Updates the held-button auto-repeat state used while the event system runs; only the scheduler slot (task index 16) does the work.

## Behavior

- V: returns immediately unless the current-task index is 16.
- V: latches the current pad word `word_1437EDF80` and the previous one, and stores the current word in the repeat-mask cell `off_1408B9AB8`.
- V: reads five button-group masks through `sub_1400F6C8C` (ids 0x21, 0x22, 0x23, 0x24, 0x2D/0x2E) and, while a held button persists, counts frames in `dword_143791D30`, `dword_143791D34` and `dword_143791D38`.
- V: compares the counters with thresholds from the bytes at 0x1407829FB, 0x1407829FE and 0x1407829FF divided by `dword_14078D578`; when a threshold is reached it writes the repeat mask to the cell at `off_1408B9A48`.
- I: this is the held-button repeat: an initial delay, then a faster repeat for the directional buttons, with a different mask when the button group tested by `sub_1400FC598(.., 128, 0x1D)` is active.

## Referenced by

- Called by: [EventTask_Terminate](EventTask_Terminate.md), [EventTask_WaitFrame](EventTask_WaitFrame.md)

## Notes

The button ids are not decoded; the threshold bytes are plain data.

## Open questions

Name the button groups and the meaning of the 0x1D test.
