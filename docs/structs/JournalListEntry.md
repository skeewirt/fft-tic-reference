# JournalListEntry

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 12-byte entry of the Chronicle Events list that JournalList_Build fills for each Journal row that is met.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="key"></a>`0x0` | key | `int32` | V | The Journal key. |
| <a id="sort_order"></a>`0x4` | sort_order | `int32` | V | Journal sort_order (+8); the list is insertion-sorted by it. |
| <a id="kind"></a>`0x8` | kind | `uint8` | V | 1 when the row's movie byte is set, 2 when its event_id is 0, else 0; the row plays 'Movie', 'Battle' or 'Event'. |
| <a id="new_mark"></a>`0x9` | new_mark | `uint8` | V | The row's new mark (from the save block's journal_new_marks); cleared by action 1. |
| <a id="seen_mark"></a>`0xA` | seen_mark | `uint8` | I | From the save block's journal_seen_marks. |

## Behavior

- V: JournalList_DrawRow passes byte +9 to sub_14016B31C; JournalScreen_OnAction clears it on action 1.

## Notes

Sheets: JournalList_Build, JournalList_DrawRow, JournalScreen_OnAction.

## Open questions

? bytes +10 and +11 (the order of the last two pushed values).
