# NxdDataPause

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 282
- **Rows:** 13 rows of 24 bytes
- **Keyed by:** one key: id (0..12)
- **Read by:** [PauseManager_Tick](../functions/PauseManager_Tick.md)
- **Row layout:** [NxdDataPauseRow](../structs/NxdDataPauseRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pause overlay settings (13) with a sound event link. Verdict: designer-data.

## Behavior

- V: 13 rows, one key id (0..12); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 9 of 12 columns not decoded (see the row layout)
