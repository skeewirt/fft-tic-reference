# NxdDataJournalRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.journal table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="sort_order"></a>`0x8` | sort_order | `int32` | V | Read in the code: Order of the Chronicle Events list: the built list is sorted ascending by this value. Observed in the stock rows: 1 to 117, 117 distinct values. |
| <a id="user_situation"></a>`0xC` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 3510 to 16000, 61 distinct values. |
| <a id="title"></a>`0x10` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 117 distinct values, 0 empty. |
| <a id="text"></a>`0x14` | text | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 117 distinct values, 0 empty. |
| <a id="event_id"></a>`0x18` | event_id | `int32` | V | Read in the code: EventId key of the event the Chronicle replays for this entry: it is written to event variable 39 (the current event number) when the replay starts; 0 = no replay, and the list shows such entries as 'Battle'. Observed in the stock rows: 0 to 488, 66 distinct values. |
| <a id="place_name"></a>`0x1C` | place_name | `int32` | V | Read in the code: PlaceName (table 85) key shown as the place of the event: non-zero plays 'ShowPlace' and sets the place text to that row's string +0xC; 0 plays 'HidePlace'. Observed in the stock rows: 0 in every row. |
| <a id="event_id_2"></a>`0x20` | event_id_2 | `int32` | V | Read in the code: A second event number kept during the replay and written back to event variable 39 when the replay hands control back (SceneTransition_CheckTables). Observed in the stock rows: 0 to 6, 2 distinct values. |
| <a id="movie"></a>`0x24` | movie | `uint8` | V | Read in the code: Marks a Chronicle event entry as a movie: the list shows it with the 'Movie' icon (instead of 'Event' / 'Battle'), and the movie replay action (action 3) works only on entries with this byte set. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="clear_mark"></a>`0x25` | clear_mark | `uint8` | V | Read in the code: When set the Events detail shows the 'Clear' mark (node 'Clear' plays 'Enable', else 'Disable'). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="quest_mark"></a>`0x26` | quest_mark | `uint8` | V | Read in the code: When set the Chronicle event list row plays 'ShowQuest' (a quest mark), otherwise 'HideQuest'. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataJournal](../tables/NxdDataJournal.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 12 columns not decoded.
