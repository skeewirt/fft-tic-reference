# NxdDataRefinedVFXCameraControl

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 317
- **Rows:** 1 rows of 20 bytes
- **Keyed by:** one key: id (1..1)
- **Read by:** [EffectNxd_LoadRow](../functions/EffectNxd_LoadRow.md)
- **Row layout:** [NxdDataRefinedVFXCameraControlRow](../structs/NxdDataRefinedVFXCameraControlRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Effect camera control parameters (one row). Verdict: engine-data.

## Behavior

- V: 1 rows, one key id (1..1); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 5 columns not decoded (see the row layout)
