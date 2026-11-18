# UnitSpritePosePack

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B1380`
- **Rows:** 107 offsets
- **Keyed by:** pose index
- **Row layout:** [UnitSpritePosePackRow](../structs/UnitSpritePosePackRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Offset index and pose records for drawing a unit sprite as a rotated quad: 107 offsets, records of 28 bytes. Verdict: pointer-table.

## Behavior

- V: offsets rise with a constant step of 0x1C from 0xD8 to 0xC70 (107 values, the first record starts right after the 214-byte index)
- V: sub_140380FB8 (unit sprite quad builder, called from the battle sprite draw): copies two bytes at +4 + 2 x pose and reads the 28-byte record at base + 4 + offset; the quad is then rotated with the sine / cosine tables

## Notes

Our names. Tags: V offsets, ? record fields.

## Open questions

- ?: the field layout of the 28-byte record
- ?: what the pose index selects (animation frame or unit shape)
