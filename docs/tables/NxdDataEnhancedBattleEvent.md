# NxdDataEnhancedBattleEvent

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** NXD file
- **NXD table id:** 163
- **Rows:** 2274 rows of 40 bytes
- **Keyed by:** three keys: id (0..170) x id2 (0..14) x id3 (0..10)
- **Row layout:** [NxdDataEnhancedBattleEventRow](../structs/NxdDataEnhancedBattleEventRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle event scripting rows keyed by battle, step and sub-step: event type and character control id with other parameters. Verdict: designer-data.

## Behavior

- V: 2274 rows, three keys id (0..170) x id2 (0..14) x id3 (0..10); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 13 of 14 columns not decoded (see the row layout)
