# UISaveLoad_OnEvent

- **Address:** `0x1401833C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void __fastcall UISaveLoad_OnEvent(UIAgentFFTOSaveLoad *agent, int event, int arg, int flag)`
- **Callers:** sub_140182F30 (0x140182F5B)
- **Callees:** sub_1401835E8, UIAgent_SetState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps the save/load screen's event numbers 0..8 to state changes, stored selection values and pause-style prompts. The events arrive through the agent's event virtual, which only forwards those sent by the list add-on.

## Behavior

- V: called from the event virtual `sub_140182F30` (vtable slot 6). That virtual forwards only when the list-addon pointer at +1576 exists and the event source's dword at +32 equals the list add-on's dword at +32.
- V: event 0: if block-A state is 0, sets agent state 9 (close).
- V: event 1: if state is 0, stores arg at +228, stores (flag != 0) at +244 and sets state 5 (load).
- V: event 2: if state is 0, stores arg at +228 and sets state 6 (save).
- V: event 3: if state is 0, stores arg at +228 and sets state 8 (New Game + pick).
- V: event 4: stores (flag != 0) at +244, stores arg at +228, then opens prompt 3 through `sub_1401835E8(agent, 3, 0, 0, 0)`. It has no state gate.
- V: event 5: stores 0 at +244, stores arg at +228, then opens prompt 4. It has no state gate.
- V: event 6: stores arg at +228, then opens prompt 1. It has no state gate.
- V: event 7: stores arg at +228, then opens prompt 2. It has no state gate.
- V: event 8: opens prompt 5, writes no selection value, and returns the prompt call. It has no state gate.
- V: the prompt number is not the event number: `sub_1401835E8` builds a callback record ({`sub_1401834B8`, agent}) and calls `UIAddon_PauseSetup` on the pause add-on of UI agent slot 16. These calls pass 0 as the setup's "push pause" argument, so only the error prompts built in `sub_140182F68` push pause id 9.
- V: the prompt callback `sub_1401834B8` maps the chosen command to a state: 1 -> state 6 (save), 2 -> state 7 (erase), 3 -> +240 = 5, +236 = 1, +232 = 13, state 10 (deferred load), 4 -> +240 = 8, +236 = 1, +232 = 13, state 10 (deferred New Game +). Commands 6 and 7 clear the interlocked +224 flag; other commands do nothing.
- V: the list add-on's item-action virtual sends 1, 2, 3, 4, 5, 6 and 8: 1 or 4 on the auto tab, 3 or 5 on the New Game + tab, and 2, 6 or 8 on the manual tab. Its input virtual sends 0 on the back action and 7 on action 0xFB (manual tab only). The saving overlay and the dialog block send no events.
- V: events 0..3 are accepted only while block-A state is 0; events 4..8 run in any state.
- I: events 4 and 5 are raised for a save whose language differs from the current one, resting on the add-on taking those branches only when `sub_140186454` is true and on `SaveLoadList_FillItem` using the same test for its ColorDiffLang row state.
- ?: the on-screen labels and command counts of prompts 1..5; ? whether any sender outside the list add-on reaches this map (none was found); ? what the +224 flag means.

## State touched

- Calls: [UIAgent_SetState](UIAgent_SetState.md)

## Referenced by

- Appears in flows: [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md)

## Notes

Whole function read (243 bytes), with the senders read in the list add-on's item-action and input virtuals. The event and prompt sequences are separate: prompt 1 is opened by event 6, prompt 2 by event 7, prompt 3 by event 4, prompt 4 by event 5 and prompt 5 by event 8. Events 4..8 bypass the state-0 gate that events 0..3 enforce. The +244 flag comes from the source entry's +233 byte (the byte `SaveLoadList_FillItem` uses for its ShowAuto/HideAuto state). The state handlers' bodies are covered by their own sheets; this page covers only the event map.

## Open questions

? the labels and command counts of prompts 1..5; ? whether any code outside the list add-on sends these events; ? what +224 means.
