# WindowGrowSteps

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140681FD4`
- **Rows:** 12 rows of 1 bytes
- **Keyed by:** window style
- **Row layout:** [WindowGrowStep](../structs/WindowGrowStep.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per-frame edge movement of the window grow animation for each window style. Verdict: engine-data.

## Behavior

- V: sub_1402F8188 adds the byte to window edge bytes and words each frame
- I: 12 bytes up to the palette fade step table

## Notes

Our names. Tags: V reader, I count.

## Open questions

None recorded.
