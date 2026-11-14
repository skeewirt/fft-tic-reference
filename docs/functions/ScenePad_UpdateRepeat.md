# ScenePad_UpdateRepeat

- **Address:** `0x14023970C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void ScenePad_UpdateRepeat(void)`
- **Callers:** SceneTask_WaitFrame, `sub_1402F7EC8`
- **Callees:** `sub_1400F6C8C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Updates the held-button repeat for the second task table. The twin of EventPad_UpdateRepeat.

## Behavior

- V: acts only when `word_140D408E8` is 2 and the current index `dword_140D40948` is non-zero.
- V: when the current task's flag qword (`qword_140D40B38[256 * index]`) is 1, it reloads the repeat cell `off_1407DCB48` from `dword_142FEC518`, and, while the button group id 0x1D in the mask `off_1407DD348` is held, counts frames in `dword_142FF8278`.
- V: when the count reaches the threshold (the byte at 0x1407829FF divided by `dword_140782D14`) it writes the repeat mask into the cell and resets the count; otherwise it resets the count.
- I: this is the same auto-repeat idea as EventPad_UpdateRepeat, applied while a scene task owns the input.

## Referenced by

- Called by: [SceneTask_Terminate](SceneTask_Terminate.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md)

## Notes

Button ids are not decoded.

## Open questions

Name the button groups.
