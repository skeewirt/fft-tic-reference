# NxdDataUISituationSubtitles

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 224
- **Rows:** 74 rows of 8 bytes, text in 7 languages
- **Keyed by:** two keys: id (1..10110) x id2 (1..15)
- **Read by:** [EventNode_SetFromTable224](../functions/EventNode_SetFromTable224.md)
- **Row layout:** [NxdDataUISituationSubtitlesRow](../structs/NxdDataUISituationSubtitlesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Situation subtitle captions keyed by situation and line. Verdict: text.

## Behavior

- V: 74 rows, two keys id (1..10110) x id2 (1..15); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
