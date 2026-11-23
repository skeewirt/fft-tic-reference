# BattleTimelineCameraFlow

- **Kind:** flow
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The four-step camera sequence of the battle timeline's focus screen. The battle frame update calls `Battle_TimelineFocusCamera` once per frame while `g_BattleState` is 91; the shared step word `dword_140D3A86C` selects placement of the timeline on the acting unit (0), the wait for the panel's first transition (1), the interactive scroll and range preview while action 0xDB is active (2), or the wait for the panel's second transition and the dispatch of the next queued battle state (3). State 3 pops that record, which writes its +16 to `g_BattleState` and its +20 to the step word; the focus then either confirms the queued state 4 or runs a short closing sequence through `Battle_TimelineRefresh`. It never pushes or pops a task of its own.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 | [Battle_TimelineFocusCamera](../functions/Battle_TimelineFocusCamera.md) | V | The battle frame update (`sub_140210AF0`) calls the focus step in battle state 91. The timeline entry `sub_1402095FC` sets the step word `dword_140D3A86C` to 0 and the counter `dword_140D40464` to 0; the battle command dispatch `sub_140208BE4` can instead reload the step word from the queued record's +20 field and write its +16 to `g_BattleState`. |
| <a id="1"></a>1 | [Battle_FindUnitNodeAt](../functions/Battle_FindUnitNodeAt.md) | V | State 0 resolves the unit under the three cursor tile coordinates (0x140C6AFB8/0x140C6ADAC/0x140C6AFBC). The lookup prefers the current actor when more than one scene object matches. |
| <a id="2"></a>2 | [Battle_TimelineFocusCamera](../functions/Battle_TimelineFocusCamera.md) | V | State 0 scans `g_TurnList` for the unit's entry. It puts the entry on row 4 when the list index allows, sets the scroll to index - 4 and clamps it at 31; low indices use row = index and scroll = 0, high indices use row = index - 31 and scroll = 31. |
| <a id="3"></a>3 | [BattleAction_StartScript](../functions/BattleAction_StartScript.md) | V | When the focused row holds a unit, state 0 starts presentation script 1, waits a frame, moves the cursor onto that unit and waits a second frame before guide page 109 is shown. The script is a battle presentation program; the focus step itself still returns to the frame update. |
| <a id="4"></a>4 | [Battle_TimelineFocusCamera](../functions/Battle_TimelineFocusCamera.md) | V | State 0 increments the counter and, on the pass where it reaches 5, calls the panel transition helper with 0 (I: the +57192 transition) and sets the step word to 1. State 0 therefore runs six passes. State 1 resets the counter and waits until the +57192 state stops running. |
| <a id="5"></a>5 | [Battle_TimelineFocusCamera](../functions/Battle_TimelineFocusCamera.md) | V | State 2 follows action 0xDB, the input that opens the timeline from the map cursor. While the input is active, the scroll helper `sub_14010F27C` moves the row and scroll and the step redraws the focused unit. When the input is not active, the step peeks the next queued battle record, calls the panel transition helper with -1 (I: the +57368 transition) and sets the step word to 3. |
| <a id="5a"></a>5a | [BattleRange_ApplyShape](../functions/BattleRange_ApplyShape.md) | V | On a state-2 redraw, an entry whose first byte has bit 0x40 set and bit 0x20 clear gets the pending action's range shape applied to the cursor mask, after the cursor moves onto the unit's area. |
| <a id="6"></a>6 | [Battle_TimelineFocusCamera](../functions/Battle_TimelineFocusCamera.md) | V | State 3 waits for the +57368 state to stop, dispatches the next queued battle record (`sub_140208BE4`, which writes the record's +16 to `g_BattleState` and its +20 to the step word), starts presentation script 2 with the unit record's byte +444 as the actor slot, and handles the queued state id: 13 plays the two-state UI animation at 0, 23 plays it at -1, and 4 goes to the confirm dispatch. |
| <a id="7"></a>7 | [BattleAction_ConfirmCommand](../functions/BattleAction_ConfirmCommand.md) | I | `BattleAction_ConfirmCommand` resolves the cursor unit and chooses one of three handlers. I: two handlers set `g_BattleState` to 4, the third sets it to 5, and all three start presentation script 3 (rests on the handler bodies, outside this function). |
| <a id="8"></a>8 | [Battle_TimelineFocusCamera](../functions/Battle_TimelineFocusCamera.md) | V | When the confirm leaves `g_BattleState` at 4, the step sets the camera scale `dword_1407DC2BC` to 1 and returns without waiting a frame; the next battle frame dispatches state 4. Any other result falls into the closing sequence. |
| <a id="9"></a>9 | [Battle_TimelineRefresh](../functions/Battle_TimelineRefresh.md) | V | The closing sequence (also taken by every other result) sets the timeline-mode sentinel `dword_140D4058C` to -1, calls the timeline refresh, pauses input for 0.1 s, starts script 1, holds one frame, refreshes the guide, waits a second frame and returns. It does not restore the previous state or step word; the next frame dispatches whatever `g_BattleState` holds after the dispatch and confirm. |
| <a id="10"></a>10 | [Battle_TimelineBuildList](../functions/Battle_TimelineBuildList.md) | V | The refresh takes its 40-entry forecast from this builder before copying it into `g_TurnList` and filling the visible panel rows. |

## Behavior

- V: the focus is one of the battle frame update's state handlers: `g_BattleState` 90 and 97 run the timeline screen `sub_140209218`, 91 runs this four-step camera sequence, and 92 and 93 run further handlers that use the same step word.
- V: the step word `dword_140D3A86C` is shared with the timeline screen and with the battle load machine; it is not a private sub-state. The timeline entry sets it to 0, and the battle command dispatch reloads it from the queued record's +20 field and writes the record's +16 to `g_BattleState`.
- V: state 0 is the placement pass: it scans `g_TurnList` for the acting unit, puts it on row 4 where the index allows, sets the scroll, and starts script 1 only when the focused row holds a unit.
- V: state 1 waits for the panel's first transition (+57192); state 2 follows action 0xDB and previews the focused row's range; state 3 waits for the panel's second transition (+57368) and dispatches the next queued battle state.
- V: the queued state id 4 goes through `BattleAction_ConfirmCommand`; the dispatch has already written 4 to `g_BattleState`, and the handlers may leave it at 4 or set it to 5. The focus treats only 4 as success.
- V: the closing sequence rebuilds the timeline panel through `Battle_TimelineRefresh`, pauses input, plays script 1 and returns after two frames. It does not roll back `g_BattleState` or the step word.
- V: the sequence never pushes or pops a task of its own. Every case returns to the battle frame update; the next frame dispatches the state that state 3's record or the confirm handlers wrote, with the step word from the record. The presentation scripts started along the way run through `BattleAction_StartScript`.
- I: the four steps are one camera sequence: place, settle, scroll and confirm, finalise. (rests on the two panel state nodes, the action 0xDB test and the confirm dispatch.)
- I: the queued state id 4 is the confirm path and 13/23 are the two timeline guide states. (rests on the three confirm handlers and on the two guide-animation calls.)
- ?: what queued state ids 13 and 23 name; what `dword_140D3A840` selects; what the queued record's +24 field selects.

## Notes

Covers the focus function, the two timeline entry functions, the command dispatch, the three confirm handlers, the panel scroll helper and the two cursor-camera helpers. Addresses are build-specific.

## Open questions

? what queued state ids 13 and 23 name; ? what `dword_140D3A840` selects; ? what the queued record's +24 field selects.
