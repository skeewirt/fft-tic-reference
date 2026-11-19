# JournalList_RestoreCursor

- **Address:** `0x1401699A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalList_RestoreCursor(void *screen)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Puts the list cursor back on the replayed entry.

## Behavior

- V: back in the list, re-finds the entry by event_id (+0x18) / event_id_2 (+0x20) to restore the cursor.

## Referenced by

- Appears in flows: [ChronicleEventReplay](../flows/ChronicleEventReplay.md)
- Called by: [JournalScreen_OnAction](JournalScreen_OnAction.md)

## Open questions

None recorded.
