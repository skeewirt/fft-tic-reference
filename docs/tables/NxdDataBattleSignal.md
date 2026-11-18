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
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
