# NxdDataOverrideEntryData

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 96
- **Rows:** 516 rows of 160 bytes
- **Keyed by:** two keys: id (83..500) x id2 (0..15)
- **Read by:** [EventScript_Run](../functions/EventScript_Run.md), [OverrideEntry_LoadBattleEntries](../functions/OverrideEntry_LoadBattleEntries.md)
- **Row layout:** [NxdDataOverrideEntryDataRow](../structs/NxdDataOverrideEntryDataRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per-battle unit entry overrides (516 rows, keyed by battle and slot): sprite, job, skills, gear, level and facing. Verdict: designer-data.

## Behavior

- V: 516 rows, two keys id (83..500) x id2 (0..15); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 27 of 52 columns not decoded (see the row layout)
