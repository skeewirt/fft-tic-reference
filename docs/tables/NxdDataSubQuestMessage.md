# NxdDataSubQuestMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 320
- **Rows:** 3 rows of 12 bytes
- **Keyed by:** one key: id (0..2)
- **Row layout:** [NxdDataSubQuestMessageRow](../structs/NxdDataSubQuestMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Three sub-quest message sound links. Verdict: designer-data.

## Behavior

- V: 3 rows, one key id (0..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
