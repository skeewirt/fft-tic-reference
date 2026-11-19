# SaveBlockUiMarks

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)
- **Size:** 7780 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The parts of the save block behind qword_143CD9DC8 that hold the 'new' marks and the current position of the Zodiac Stone, Chronicle, Events and glossary screens. Only the offsets the screens' code uses are listed.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="zodiac_marks"></a>`0x19D0` | zodiac_marks | `uint8[4][13]` | I | Four bytes per stone (set) and row index at +6608 + 4 * set + index: the row's new mark. Read by ZodiacStone_AnyMetAndNew, cleared by ZodiacStone_ClearNewMarks. |
| <a id="journal_keys"></a>`0x1A0A` | journal_keys | `uint16[128]` | V | Word list at +6666: the Journal keys the screen keeps marks for; action 1 of the Events screen looks the entry's key up here. |
| <a id="journal_new_marks"></a>`0x1B0A` | journal_new_marks | `uint8[128]` | V | Bytes at +6922 + i, one per key of the list above: cleared by action 1 of the Events screen; copied into each Events list entry by JournalList_Build. |
| <a id="journal_seen_marks"></a>`0x1B8A` | journal_seen_marks | `uint8[128]` | V | Bytes at +7050 + i: set to 1 by action 1 of the Events screen; copied into each Events list entry by JournalList_Build. |
| <a id="glossary_marks"></a>`0x1C0B` | glossary_marks | `uint8[150][2]` | I | Two bytes per glossary entry at +7179 + 2 * index: the entry's new mark. Cleared by LoreDictionary_ClearNewMarks. |
| <a id="chronicle_period"></a>`0x1E62` | chronicle_period | `uint16` | V | At +7778: its low byte is the current Chronicle period (capped at 28 by ChronicleTimeline_Setup). |

## Behavior

- V: the offsets are read from the code of the screens named in each field; the block's own identity was not followed (the global qword_143CD9DC8 is read through a pointer).

## Notes

Partial. Sizes of the arrays are bounds of the loops that touch them.

## Open questions

? what the block is called in the save; ? what the +7050 'seen' bytes are used for after they are copied.
