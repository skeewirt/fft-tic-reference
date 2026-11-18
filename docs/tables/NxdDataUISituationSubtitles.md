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
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
