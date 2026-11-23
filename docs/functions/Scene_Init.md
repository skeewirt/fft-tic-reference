# Scene_Init

- **Address:** `0x14037F510`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall Scene_Init(int mode)`
- **Callers:** SceneLoop_Run (0x140331C2C), Opening_EndToTitle (0x14037DE74)
- **Callees:** EventSlots_ResetAll, sub_14037F5E4, sub_14038ED68, TitleScene_Start, OpeningScene_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The scene-global reset: it seeds the scene flags, task stack and page buffer, then starts the title path directly for a non-zero mode or through the opening bootstrap for mode 0.

## Behavior

- V: calls `EventSlots_ResetAll`, then sets 0x14187A3F4, 0x141876EF0, 0x141877778, 0x1418825E8 and 0x141876EFC to 0, and 0x141876EF4 to -1.
- V: points `qword_141876F98` at `unk_141C82E00`, writes 4161 to `dword_141876EE8` (bits 0, 6 and 12), sets 0x141876F10 and 0x141876F14 to 2 and 0x14187A5D4 to 4.
- V: calls `sub_14037F5E4` and `sub_14038ED68`, clears `qword_14187A408` and `unk_14187A404`, and zeroes the task-stack depth `dword_141877480`.
- V: copies `byte_1407829FB` into `dword_14187A3F8` and `byte_1407829FE` into `qword_14187A3FC`.
- V: a non-zero mode calls `TitleScene_Start` and returns its result.
- V: mode 0 clears `dword_1418825EC` and calls `OpeningScene_Start`, returning its result.
- I: the mode is a start selector, not a scene id: the mode-0 path pushes opening task 0, which immediately starts the title task (rests on `OpeningScene_Start` and the task 0 body).
- ?: what the two copied bytes configure, and what each cleared counter controls.

## State touched

- Calls: [EventSlots_ResetAll](EventSlots_ResetAll.md), [TitleScene_Start](TitleScene_Start.md), [OpeningScene_Start](OpeningScene_Start.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md), [ApplicationLifecycle](../flows/ApplicationLifecycle.md), [OpeningToTitle](../flows/OpeningToTitle.md), [SceneTaskDispatch](../flows/SceneTaskDispatch.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)
- Called by: [Opening_EndToTitle](Opening_EndToTitle.md), [SceneLoop_Run](SceneLoop_Run.md)

## Notes

Whole function read (210 bytes). The scene flag word starts at 4161, so the run bit is set before the loop is entered. The two copied bytes come from the block the scene setup rewrites with the default status values.

## Open questions

The meaning of the two copied bytes and of each reset scene counter.
