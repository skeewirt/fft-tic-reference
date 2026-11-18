# NxdDataOverrideAbilityActionData

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** NXD file
- **NXD table id:** 247
- **Rows:** 368 rows of 40 bytes
- **Keyed by:** one key: id (0..367)
- **Read by:** [AbilityAction_BuildWorkingCopy](../functions/AbilityAction_BuildWorkingCopy.md)
- **Row layout:** [NxdDataOverrideAbilityActionDataRow](../structs/NxdDataOverrideAbilityActionDataRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Ability data override rows: each field is -1 (keep the stock value) or a replacement for range, area, formula, status, CT or MP cost. Verdict: designer-data.

## Behavior

- V: 368 rows, one key id (0..367); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 13 columns not decoded (see the row layout)
