# NxdDataSpellMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 146
- **Rows:** 1182 rows of 12 bytes
- **Keyed by:** two keys: id (1..77) x id2 (0..100)
- **Row layout:** [NxdDataSpellMessageRow](../structs/NxdDataSpellMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Spell voice lines keyed by spell and line, pointing at packed audio entries. Verdict: designer-data.

## Behavior

- V: 1182 rows, two keys id (1..77) x id2 (0..100); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
