# Music_StartSceneTracks

- **Address:** `0x140234990`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int Music_StartSceneTracks(int track1, int track2)`
- **Callers:** EventScript_Run, sub_1401EF0D8, sub_1401F014C, sub_140210AF0, Scene_StartMusic
- **Callees:** EventSlots_ResetAll, SceneCallback_Dispatch

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a scene's music: resets the event slots, loads the two tracks into music slots 1 and 2, then starts slot 1.

## Behavior

- V: first calls EventSlots_ResetAll.
- V: for each non-zero track it points the text-command slot pointer at EventSlot_LoadTrack and dispatches a scene callback of kind 2 with (track, slot 1 or 2); EventSlot_LoadTrack stores the track number in dword_142E7FB08[slot].
- V: when track 1 is non-zero it points the slot pointer at MusicSlot_FetchRecord and dispatches a scene callback of kind 3 with (1, 127): music slot 1 starts at volume 127 from the music slot record of the track. Track 2 is only loaded, never started here.
- V: the two arguments come from the scenario setup record bytes +5 and +6 (the caller Scene_StartMusic reads them from the scene words it holds), or from the saved pair in qword_140816CD0 on a resume.

## State touched

- Calls: [EventSlots_ResetAll](EventSlots_ResetAll.md), [SceneCallback_Dispatch](SceneCallback_Dispatch.md)

## Referenced by

- Called by: [Scene_StartMusic](Scene_StartMusic.md)

## Notes

Return value: the last callback result, or the reset result when both tracks are 0.

## Open questions

? what the kind 2 and kind 3 scene callbacks do beyond reaching the two handlers named above.
