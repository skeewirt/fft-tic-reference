# DissolveOffsets

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407BE720`
- **Rows:** 32 rows of 64 bytes
- **Keyed by:** dissolve step
- **Read by:** [ImageDissolve_Step](../functions/ImageDissolve_Step.md)
- **Row layout:** [DissolveStep](../structs/DissolveStep.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Pixel-order table of a dissolve (reveal) effect: 32 steps, each with 32 offsets. Verdict: engine-data.

## Behavior

- V: 0x800 bytes = 32 x 32 x 2; the reader multiplies the step counter by 64 and walks 32 entries
- V: ImageDissolve_Step (0x140372518): for step n copies 32 bytes of the new image at the listed offsets, per line group, into the displayed buffer; after step 49 the effect ends

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which screen uses the dissolve (a legacy menu picture transition)
