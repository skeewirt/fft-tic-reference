# NxdDataUI

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 19
- **Rows:** 4050 rows of 8 bytes, text in 7 languages
- **Keyed by:** one key: id (0..4049)
- **Read by:** [ConfigMenu_SetHelpText](../functions/ConfigMenu_SetHelpText.md)
- **Row layout:** [NxdDataUIRow](../structs/NxdDataUIRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The general UI text table: 4050 strings keyed by UI text key. Verdict: text.

## Behavior

- V: 4050 rows, one key id (0..4049); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
