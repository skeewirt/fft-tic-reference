# FastForwardState

- **Kind:** observed behaviour
- **Scope:** battle, event scripts (story scenes, battle dialogue) and the world map, enhanced edition
- **Area:** [Application and startup](../areas/app-startup.md)
- **Affects:** [GlobalWork_GetFastForwardMode](../functions/GlobalWork_GetFastForwardMode.md), [GlobalWork_GetSpeedMultiplier](../functions/GlobalWork_GetSpeedMultiplier.md), [GameTasks_RunFrameSteps](../functions/GameTasks_RunFrameSteps.md), [BattleControl_FrameUpdate](../functions/BattleControl_FrameUpdate.md), [EventControl_RunningTick](../functions/EventControl_RunningTick.md), [WorldMap_UpdateFastForward](../functions/WorldMap_UpdateFastForward.md), [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md), [GlobalWork](../structs/GlobalWork.md), [EventControl](../structs/EventControl.md), [InputActionRow](../structs/InputActionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the fast-forward hold and the dialogue auto-advance toggle become state, how to read 'fast-forward is active now' from memory with no input, what gates a hold, and what the state changes.

## Behavior

- V: recipe. gw = u64 at g_GlobalWork (0x143CD9DD0); level = u32 at gw + 0x58; mode = u32 at gw + 0x60; setting = u8 at (u64 at g_ConfigData 0x140C69690) + 0x37. Effective mode = 0 when setting is 1, or when setting is 2 and mode is 2; else mode. Fast-forward is active now when the effective mode is not 0 and level is 1 or 2; the game then runs 3 (level 1) or 5 (level 2) steps per displayed frame.
- V: mode, written by the battle frame routine sub_140210AF0 every frame: in battle states 52 and 58 (an event script is running) mode = 2, or 0 while the event pause overlay is up (EventControl state 2); in every other state mode = 1 when g_FastForwardStateTable[g_BattleState] is non-zero, else mode = 0 and level = 0. The world map set-up writes mode 3; the battle control's destructor writes 0.
- V (data, GameModeTypes byte +16): fast-forward is off in battle states 0, 4, 12, 21, 22, 23, 27, 31..36, 83, 84, 87, 88, 90, 91, 93 and 97, on in the other states up to 105.
- V: battle (mode 1): level = 2 while action 90 is held, else 1 while action 89 is held, else 0, written every battle frame by BattleControl_FrameUpdate (enhanced edition, PauseManager byte +24 bit 4 clear, dword_140D3A840 == 0). A plain level test of the held byte: a button that is already down counts, there is no delay.
- V: event script (mode 2), EventControl_RunningTick, once per displayed frame while the overlay state is 1: a press edge of action 89 or 90 is accepted only when the control's run timer (EventControl +0x28) has reached 0.75 s; it sets armed (+0x35). While armed and held (and +0x32 is 0) the hold timer +0x24 grows and the 'Fast-forwarding' label is shown (+0x2C = 1); when the hold timer reaches 1.0 s the level becomes 1 (2 with action 90 held). Releasing clears armed, the timer, the label and the level.
- I: this is why a button held from before a scene never starts fast-forward (no press edge after the 0.75 s mark), why a fresh press shows the label at once, and why the first balloon advances about 1.2 s after the press (1.0 s ramp, then the page) and later ones faster (measured live 2026-11-09: label within 0.09 s, first advance about 1.2 s, later about 0.4 s).
- V: EventControl_Reset zeroes both timers and the flags on every frame without an event tick, so the 0.75 s count restarts with each event script; EventControl_ApplyCarry restores a running fast-forward (armed, timer 1.0, level 1) at the start of a chained event whose EventId row has byte +35 set, and auto-advance when it has byte +34 set.
- V: auto-advance: action 91 pressed toggles EventControl +0x2F (1 = on) when the event allows it; the dialogue window's auto indicator follows it. With the setting enableEventKeepAuto (config byte +0x3B) the latch g_EventKeepAutoLatch (u8 0x140C6AD73) switches it on again in the next event. It is not consulted while fast-forward is held.
- V: world map (mode 3): level = 1 while action 89 is held (WorldMap_UpdateFastForward), cleared when a world panel opens.
- V: what the level changes: GameTasks_RunFrameSteps repeats the whole task step 3 or 5 times per displayed frame and draws only the last; the UI animation time step is multiplied by the same number (UI_FrameUpdate); EventMessage_Task and EventMessage_Scripted stop waiting for a button on a finished page while the level is non-zero; the timed battle message closes after 180 / multiplier frames, not below 30 (sub_14020C30C); battle and event voices are not started (sub_1401EC958, EventVoice_PlayTask); the sound manager switches a state per level (sub_1401D6988).
- I: predicted speed-up: frame-counted waits (animation, walking, effects, script waits) take 1/3 of the wall time at level 1 and 1/5 at level 2, as long as the machine can run the extra steps inside one frame; the text typing rate is also set from the multiplier (sub_14022280C passes it to the event window).
- V: the pause overlays clear the level when they open (EventControl_TryOpenPause, MovieControl_TryOpenPause).
- V: one more reader of action 89 outside these three handlers: the text-typing tick sub_1401E0688 (caller sub_1401DFB90) multiplies its time step by 4 while action 89 is held and dword_140D8DBA8 is not above 0; it never touches the level. ?: which screen that typed text belongs to (the UI object at +248 of the UI root).
- ?: no code that draws a fast-forward indicator in battle outside dialogue was found; the only label is the dialogue window's node.

## Notes

Buttons: action 89 = Ctrl, fifth mouse button, pad RB; action 90 = the 5 key, or pad Y while RB is held; action 91 = Shift, pad X (pad ids decoded from the pad mask builder, see Input_UpdateActionRow). Detail and evidence: the function sheets linked from this page.

## Open questions

? Live: every read of the recipe (level and mode while holding and not holding, in an enemy turn, in a dialogue and on the world map); the EventControl timers during a hold; level 2 with Y + RB or the 5 key. ? What dword_140D3A840 is, and so in which battle moments the level is not refreshed.
