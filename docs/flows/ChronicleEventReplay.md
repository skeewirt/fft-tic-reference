# ChronicleEventReplay

- **Kind:** flow
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What happens when the player replays an entry of the Chronicle Events list: from the action to the event running.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1 action"></a>1 action | [JournalScreen_OnAction](../functions/JournalScreen_OnAction.md) | V | Action 2 replays the event, action 3 the movie (only for rows with movie set); action 1 only clears the new mark. |
| <a id="2 request"></a>2 request | [JournalReplay_StartEvent](../functions/JournalReplay_StartEvent.md) | V | The panel stores event_id (+112), event_id_2 (+116), the list cursor (+120), start = 1 (+124) and the movie flag (+126); UI sound 0x73. |
| <a id="3 prepare"></a>3 prepare | [JournalPanel_Tick](../functions/JournalPanel_Tick.md) | V | State 1: input paused, list closed, the guide hidden, a fade started. |
| <a id="4 start"></a>4 start | [EventViewer_StartReplay](../functions/EventViewer_StartReplay.md) | V | After the fade: event variables 508 = 1 and 39 = the event; the event chain is looked up; the skip flags are set; the second counter bank is switched on. |
| <a id="5 return"></a>5 return | [JournalList_RestoreCursor](../functions/JournalList_RestoreCursor.md) | V | Back in the list the entry is found again by event_id / event_id_2 and the cursor is restored. |

## Behavior

- V: the event_id_2 column is written back to event variable 39 when the replay hands control back (SceneTransition_CheckTables).

## Open questions

? the later states of the panel after state 3.
