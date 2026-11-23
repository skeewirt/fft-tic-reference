# OpeningScene_Resume

- **Address:** `0x1402F0848`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void __fastcall OpeningScene_Resume(void)`
- **Callers:** tbl_OpeningTaskSteps id 13, dispatched by SceneLoop_Run (0x140331D2D) and SceneLoop_RunAlt (0x14039DE79)
- **Callees:** OpeningScene_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 13: the title's way back into the opening. It sets the scene-entry bit, resets the page index, pops itself and re-enters `OpeningScene_Start`, which pushes task 0 again.

## Behavior

- V: sets bit 6 (0x40) of `dword_141876EE8`.
- V: stores 0 in `dword_1418825EC`, the page index `SceneLoop_Run` uses to select `qword_141878C70`.
- V: decrements the task depth `dword_141877480` (a pop) and tail-jumps to `OpeningScene_Start`.
- V: `OpeningScene_Start` then clears bit 6, sets bit 1, writes the same two frame dwords and pushes task 0; it takes no stage argument.
- V: case 3 of `TitleScene_Task` replaces the top id with 13 and sets the 16-bit field at `g_UIStateFade+40` to 257.
- I: `Resume` is a restart, not a restore: the only opening-progress value task 13 clears is the page index, and the start function always seeds the same first task and frame (rests on the bodies; no saved stage is read).
- ?: which title action produces the case-3 result that pushes 13.

## State touched

- Calls: [OpeningScene_Start](OpeningScene_Start.md)

## Referenced by

- Appears in flows: [OpeningToTitle](../flows/OpeningToTitle.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)

## Notes

Whole function read (25 bytes). IDB name `OpeningScene_Resume`; the last instruction is a jump to `OpeningScene_Start`. Task 11 (`sub_14037F354`) is the same re-entry with page index 1, not 0.

## Open questions

What the title's case-3 action is (the idle timeout is one candidate, not verified), and whether any other path pushes id 13.
