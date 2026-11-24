# EventViewer_StartReplay

- **Address:** `0x1402D28C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void EventViewer_StartReplay(int event, int movie)`
- **Callers:** JournalPanel_Tick
- **Callees:** EventVar_Write, EventChain_Find

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the replay of an event from the Chronicle.

## Behavior

- V: EventVar_Write(508, 1), EventVar_Write(39, event), EventChain_Find(event) into g_EventViewerChained; sets the skip flags.
- V: copies the user situation bytes 97..99 to 177..179; sets bit 0 of g_UserSituation +16 (the bank bit: replays use the second counter bank); dword_141D32EE4 = event.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [EventChain_Find](EventChain_Find.md)
- Writes: [g_UserSituation](../globals/g_UserSituation.md)

## Referenced by

- Appears in flows: [ChronicleEventReplay](../flows/ChronicleEventReplay.md)
- Called by: [JournalPanel_Tick](JournalPanel_Tick.md)
- Observed behaviours: [EventVariableWriteLock](../behaviors/EventVariableWriteLock.md)

## Open questions

? what the user situation bytes 97..99 / 177..179 are.
