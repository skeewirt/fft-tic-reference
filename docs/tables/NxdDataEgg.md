# NxdDataEgg

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** NXD file
- **NXD table id:** 310
- **Rows:** 49 rows of 24 bytes
- **Keyed by:** one key: id (0..48)
- **Read by:** [Party_EggUpkeep](../functions/Party_EggUpkeep.md)
- **Row layout:** [NxdDataEggRow](../structs/NxdDataEggRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per egg (a job grouping): three job ids and a parameter. Verdict: designer-data.

## Behavior

- V: 49 rows, one key id (0..48); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
