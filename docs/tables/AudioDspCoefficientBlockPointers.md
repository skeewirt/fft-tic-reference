# AudioDspCoefficientBlockPointers

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x14077C620`
- **Rows:** 80 rows of 8 bytes (82 in the sweep run)
- **Keyed by:** filter set (one of four sub-lists), then slot
- **Read by:** [AudioDsp_InitCoefficientSets](../functions/AudioDsp_InitCoefficientSets.md)
- **Row layout:** [DataBlockPointerRow](../structs/DataBlockPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pointer lists to the 1024-byte float coefficient blocks of the audio library DSP; 32 distinct blocks, the pointer pattern is a, b, b, a repeated per channel pair. Verdict: pointer-table.

## Behavior

- V: the initialiser fills a 0x2208 byte work area and copies pairs of pointers from the sub-lists at +0 and +0xC0 (more than eight channels) or at +0x180 and +0x200 (the small cases)
- I: the two pointers and two words after slot 79 end the object; their meaning is unknown

## Notes

Our names. Tags: V pointer layout, I coefficient meaning.

## Open questions

- ?: what the blocks compute
- ?: the two trailing pointers
