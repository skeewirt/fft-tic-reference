# SurfacePairConstants

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x14067E110`
- **Rows:** 63 rows of 2 bytes
- **Keyed by:** tile surface type (low 6 bits of tile byte 0)
- **Row layout:** [SurfacePairConstant](../structs/SurfacePairConstant.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per surface type, two bytes that are 25 everywhere; their two destination words have no other reader. Verdict: engine-data.

## Behavior

- V: 0x7E bytes to the next symbol; all entries equal
- V: sub_140236468 (battle cursor tile info): surface = tile byte 0 & 0x3F, copies the two bytes into two words

## Notes

Our names. Tags: V.

## Open questions

- ?: what the two values meant (no reader of the destination words found in this build)
