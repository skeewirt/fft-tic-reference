# JournalReplay_StartEvent

- **Address:** `0x140169724`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalReplay_StartEvent(void *screen)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetRowById, sub_1400F4BCC, sub_14040D200

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the replay of the chosen Events entry (action 2).

## Behavior

- V: panel +112 = event_id (+0x18), +116 = event_id_2 (+0x20), +120 = list cursor, +124 = 1 (start), +126 = 0; then plays UI sound 0x73.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md), [sub_1400F4BCC](sub_1400F4BCC.md)

## Referenced by

- Appears in flows: [ChronicleEventReplay](../flows/ChronicleEventReplay.md)
- Called by: [JournalScreen_OnAction](JournalScreen_OnAction.md)

## Open questions

None recorded.
