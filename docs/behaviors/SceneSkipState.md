# SceneSkipState

- **Kind:** observed behaviour
- **Scope:** every skippable story scene: event scripts (world map, town, battle) and movies
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventSkip_IsAvailable](../functions/EventSkip_IsAvailable.md), [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md), [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md), [MovieControl_TryOpenPause](../functions/MovieControl_TryOpenPause.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Whether the scene on screen can be skipped with the pause overlay + hold, and which kind of scene it is, read from memory without any input.

## Behavior

- V: only two objects consume the hold action 0x5D (Input_TestAction / sub_1400F144C / sub_1400F1510 / sub_1400F0E98 with 0x5D): EventControl (EventControl_PausedTick, EventControl_TryOpenPause) and MovieControl (MovieControl_PausedTick, MovieControl_TryOpenPause). Any scene the overlay can skip is an event script or a movie.
- V: event script: running = low dword of g_EventScriptActive (u32 0x142FF9EC0) == 1. Skippable = EventSkip_IsAvailable: viewer case (event variable 508 != 0, variable 39 not in 410..425, u32 0x141849E10 == 0) or u32 0x142E7FB3C != 0 and u32 0x142FF9E54 == 0 and u32 0x142FF9E50 != 0 and u32 0x142FF9E0C == 0 and u32 0x142FF9EBC != 2. All inputs are plain globals set before the overlay exists; opening the overlay writes none of them.
- V: the event's armed flag (u32 0x142FF9E50) is decided when EventScript_LoadCurrent loads an event whose number (variable 39) differs from the last loaded one (s32 0x140782A94): 1 when EventId (NXD 156) byte +32 is set, when the event is one of 517, 530, 549, 551, 524, 553, 569, 579, or in the viewer case; otherwise 0. EventScript_Run clears it when the script ends.
- V (data): EventId byte +32 is set for 72 events: 2, 8, 14, 25, 27, 29, 38, 43, 45, 52, 54, 56, 58, 60, 69, 77, 90, 117, 138, 147, 149, 154, 156, 158, 160, 165, 170, 172, 174, 190, 201, 203, 209, 211, 213, 215, 217, 224, 231, 233, 249, 255, 260, 270, 275, 283, 290, 296, 298, 300, 309, 327, 329, 331, 345, 352, 358, 366, 374, 376, 384, 389, 427, 429, 430, 432, 434, 442, 457, 463, 483, 489.
- V: skip-once: EventScript_Run sets u32 0x142FF9EBC to 1 at its start for events with EventId byte +36 (117, 170, 179, 213, 222, 298, 374, 427, 483, 489), for battles whose NXD 96 row has byte +147/+148/+149 set, and for events 524, 530, 569; else 0. Taking a skip turns 1 into 2, after which EventSkip_IsAvailable is false for the rest of that script.
- I: an event script that runs again under the same event number (LoadCurrent sees no change) is not re-armed: armed was cleared at the previous script end, so it reads 0 and the scene is not skippable. Battle message events started by BattleMsg_Dispatch go through the same EventScript_TaskMain path and follow this rule.
- V: event pause gate: EventControl_Update runs only while 0x142FF9EC0 != 0, g_ShopModeGate (0x1407D453C, enhanced flag) != 0 and u32 at qword_143CD9DD0 + 92 == 0; the overlay opens only while EventControl bytes +0x31, +0x34, +0x39 are 0. These say whether the overlay can open now, not whether the scene is skippable.
- V: movie: g_MovieControl (u64 0x143CDA078) non-null after Movie_Start. Skippable = u8 at g_MovieControl + 0x19, rewritten every frame from movie flag 0x10 (u32 at u64(0x143CD9DC8) + 0xC8 + 0x18). Readable without input; the overlay only reads it.
- V (data): MovieData (NXD 65) rows 5, 6, 7 and 9..15 (movie/enhanced/19, 10, 08, 01..07.usm) have bytes +36 and +37 set (pausable and skippable); rows 1..4 (09_ja, 20, 22, 21_ja) and 16..22 have byte +38 set and +37 clear (not skippable).
- I: the requested / playing movie id is s32 0x142E7FB04 (-1 none): Boot_UpdateVideo starts that MovieData row.
- V: the overlay's button guide is UIButtonGuide 502 (Resume + Skip); both overlays pass mask -3 instead of -1 when the scene is not skippable (I: bit 1 = the Skip entry), so an overlay that shows only Resume is the same answer as the passive read.
- ?: which kind each on-screen scene is (prologue narration, Orbonne chapel): the narration is not an event script loaded by number (event number reads -1 there, live 2026-10-30), so by the exhaustion above it is a movie (I), unproven live.

## Notes

Debugger reads (dbg.py _event_info): 'allowed' = low dword of 0x142FF9E4C is the viewer flag, 0 in normal play by design; 'armed' = 0x142FF9E50 is the real per-event flag; 'veto' = 0x142FF9E54 is 1 only while a battle scene is built; 'state' = 0x142FF9E0C is the skip state (0 none, 1 requested, 2 skipping). Detail and evidence: the function sheets named on this page.

## Open questions

? Live: armed / skip-once / event number during the Orbonne chapel scene and a world-map event; g_MovieControl + 0x19 during the prologue narration; whether mid-battle balloons reuse the battle's event number.
