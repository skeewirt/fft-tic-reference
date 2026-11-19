# NxdDataBattleSignal

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 214
- **Rows:** 71 rows of 16 bytes, text in 7 languages
- **Keyed by:** one key: id (0..70)
- **Row layout:** [NxdDataBattleSignalRow](../structs/NxdDataBattleSignalRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Short in-battle banner texts (titles) with a flag for evasion messages. Verdict: designer-data.

## Behavior

- V: 71 rows, one key id (0..70); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
