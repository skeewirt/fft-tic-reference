# JournalReplay_StartMovie

- **Address:** `0x140169854`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalReplay_StartMovie(void *screen)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetRowById, sub_1400F4BCC, sub_14040D200

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the replay of a movie entry (action 3).

## Behavior

- V: like JournalReplay_StartEvent but only for rows with movie (+0x24) set; panel +112 = +0x18, +116 = +0x20, +120 = list cursor, +124 = 1, +126 = 1; then UI sound 0x73.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md), [sub_1400F4BCC](sub_1400F4BCC.md)

## Referenced by

- Called by: [JournalScreen_OnAction](JournalScreen_OnAction.md)

## Open questions

None recorded.
