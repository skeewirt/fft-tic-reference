# UiLauncherFocusNeighborsAlt

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14070A800`
- **Rows:** 7 rows of 24 bytes
- **Keyed by:** button 0..6
- **Row layout:** [LauncherFocusRow](../structs/LauncherFocusRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Directional focus neighbours of the seven buttons of the start launcher, alternate layout (the default layout of the same shape is at 0x14070A8D0). Verdict: designer-data.

## Behavior

- V: the launcher reads row 24 * button from 0x14070A8D0, or from this table when its byte +4165 is non-zero

## Notes

Our names. Tags: V reader, I fields.

## Open questions

- ?: which direction each of the four neighbours is
