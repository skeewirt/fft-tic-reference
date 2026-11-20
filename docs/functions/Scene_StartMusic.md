# Scene_StartMusic

- **Address:** `0x1402FC484`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `char Scene_StartMusic(void)`
- **Callers:** Battle_JoinUnitAndLoad, sub_14030476C
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, SceneVar_Read, SceneCallback_Dispatch, Music_StartSceneTracks, sub_1402B1E74, sub_1402CD758, sub_140226C2C, sub_14024A528, sub_140257440

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

At a scene start, keeps the running music when the scene's track is the one already playing, otherwise starts the scene's tracks.

## Behavior

- V: runs only when word_140D407CC is non-zero and scene variable 39 is not in 410..425.
- V: when the previous pair (words 0x140D4091C / 0x140D408FC) is empty and a resume capture is active (DWORD2(xmmword_142FF9E24) == 1), both tracks come from qword_140816CD0 into the scene words 0x140D407C4 / 0x140D407C8.
- V: when the previous track equals one of the new tracks it clears that music slot's record and re-dispatches the load of the new track (EventSlot_LoadTrack path) instead of restarting: the music keeps running.
- V: otherwise it calls Music_StartSceneTracks(track1, track2).
- V: afterwards the previous pair is set to the new pair, sub_14024A528(99, ...) runs, and sub_140226C2C runs unless dword_143807790 is 3.
- I: on a skip with a non-playing scene it forces track 12 when the EventId row (variable 39) has +0x1C == 2 and dword_142E8A134 is 0; the meaning of that EventId field is not decoded.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [SceneVar_Read](SceneVar_Read.md), [SceneCallback_Dispatch](SceneCallback_Dispatch.md), [Music_StartSceneTracks](Music_StartSceneTracks.md)

## Open questions

? the exact role of the previous-pair words (0x140D4091C / 0x140D408FC) and of word_140D40900.
