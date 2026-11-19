# EventControl

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

ffto::Game::Event::EventControl (vtable 0x140713658), the singleton at g_EventControl: the event-script pause overlay and its hold-to-skip.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="state"></a>`0x8` | state | `int32` | V | 0 off (EventControl_Reset on frames without an event tick), 1 script running, 2 paused (overlay up), 3 skip chosen; EventScript_SkipTick reads 3 as the skip request in the enhanced edition. | [EventControl_IsAutoAdvancing](../functions/EventControl_IsAutoAdvancing.md), [EventControl_Update](../functions/EventControl_Update.md) | [EventControl_PausedTick](../functions/EventControl_PausedTick.md), [EventControl_Reset](../functions/EventControl_Reset.md), [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md), [EventControl_Update](../functions/EventControl_Update.md) |
| <a id="prev_state"></a>`0xC` | prev_state | `int32` | V | State before the last change. |  | [EventControl_Reset](../functions/EventControl_Reset.md), [EventControl_Update](../functions/EventControl_Update.md) |
| <a id="guide_id"></a>`0x18` | guide_id | `int32` | V | 502 while the overlay's button guide is up (EventControl_TryOpenPause). |  | [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md) |
| <a id="overlay_open"></a>`0x20` | overlay_open | `uint8` | I | Set 1 by EventControl_TryOpenPause. |  | [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md) |
| <a id="ff_hold_time"></a>`0x24` | ff_hold_time | `float` | V | Seconds the accepted fast-forward hold has lasted; EventControl_RunningTick sets the fast-forward level once it reaches 1.0 and zeroes it on release (record FastForwardState). | [EventControl_IsAutoAdvancing](../functions/EventControl_IsAutoAdvancing.md), [EventControl_UpdateGuide](../functions/EventControl_UpdateGuide.md) | [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md), [EventControl_RunningTick](../functions/EventControl_RunningTick.md) |
| <a id="run_time"></a>`0x28` | run_time | `float` | V | Seconds since the control was reset, counted up to 0.75 by EventControl_RunningTick; a fast-forward press is accepted only after that. |  | [EventControl_RunningTick](../functions/EventControl_RunningTick.md) |
| <a id="ff_label_shown"></a>`0x2C` | ff_label_shown | `uint8` | V | 1 while the dialogue window's fast-forward label is shown (EventControl_ShowFastForwardLabel). |  | [EventControl_ShowFastForwardLabel](../functions/EventControl_ShowFastForwardLabel.md) |
| <a id="auto_mode"></a>`0x2F` | auto_mode | `uint8` | V | 1 = dialogue auto-advance is on: toggled by action 91 in EventControl_RunningTick, set by EventControl_ApplyCarry; the window's auto indicator (sub_140135DC8) follows it. | [EventControl_CarryToNextEvent](../functions/EventControl_CarryToNextEvent.md), [EventControl_IsAutoAdvancing](../functions/EventControl_IsAutoAdvancing.md), [EventControl_UpdateGuide](../functions/EventControl_UpdateGuide.md) | [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md), [EventControl_RunningTick](../functions/EventControl_RunningTick.md) |
| <a id="auto_carry"></a>`0x30` | auto_carry | `uint8` | V | auto_mode saved by EventControl_CarryToNextEvent at a script's end for a chained event. | [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md) | [EventControl_CarryToNextEvent](../functions/EventControl_CarryToNextEvent.md) |
| <a id="ff_block"></a>`0x32` | ff_block | `uint8` | V | Non-zero stops the fast-forward hold from counting (EventControl_RunningTick); set together with pause_block_a (the word 257 at +49). | [EventControl_RunningTick](../functions/EventControl_RunningTick.md) |  |
| <a id="ff_armed"></a>`0x35` | ff_armed | `uint8` | V | 1 after a fast-forward press was accepted; cleared on release. |  | [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md), [EventControl_RunningTick](../functions/EventControl_RunningTick.md) |
| <a id="ff_carry"></a>`0x36` | ff_carry | `uint8` | V | 1 when fast-forward was running at a script's end (EventControl_CarryToNextEvent); EventControl_ApplyCarry restores it in the next event. | [EventControl_ApplyCarry](../functions/EventControl_ApplyCarry.md) | [EventControl_CarryToNextEvent](../functions/EventControl_CarryToNextEvent.md) |
| <a id="pause_block_a"></a>`0x31` | pause_block_a | `uint8` | V | Non-zero blocks opening the overlay; set (word 257 at +49) by the panel, preview and message tasks, cleared after them. | [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md) | [EventControl_Reset](../functions/EventControl_Reset.md) |
| <a id="pause_block_load"></a>`0x34` | pause_block_load | `uint8` | V | Non-zero blocks opening the overlay; set 1 by EventScript_LoadCurrent when it loads a new event, cleared by EventScript_Run when the script starts. | [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md) |  |
| <a id="pause_block_b"></a>`0x39` | pause_block_b | `uint8` | V | Non-zero blocks opening the overlay (EventControl_TryOpenPause); set 1 by EventControl_ApplyCarry when the EventId no_pause column (+0x29) of the new event is non-zero; cleared by sub_14021EE0C and EventControl_Reset. | [EventControl_TryOpenPause](../functions/EventControl_TryOpenPause.md) | [EventControl_Reset](../functions/EventControl_Reset.md) |

## Behavior

- V: allocated (64 bytes) by sub_1402024A8 when g_EventControl is null; EventControl_Update steps it once per frame while an event script ticks.
- V: the state never records whether a skip is allowed; that is decided by EventSkip_IsAvailable from globals.

## Referenced by

- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Notes

Detail and evidence: the function sheets named on this page.

## Open questions

? The bytes +45, +46, +51, +55, +56 (inputs of the 'auto-advance allowed' test of EventControl_RunningTick; their writers were not all read).
