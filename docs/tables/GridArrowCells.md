# GridArrowCells

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408ECA68`
- **Rows:** 5 rows of 12 bytes
- **Keyed by:** cell number
- **Read by:** [GridScreen_Task](../functions/GridScreen_Task.md)
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Five sprite cells of the grid screen (arrows and page markers). Verdict: designer-data.

## Behavior

- V: readers address the cells at 12-byte steps from this base
- I: five cells by the size 0x40 up to the rectangle at 0x1408ECAA8

## Notes

Our names. Found beside the table at 0x1408ECA70; tags V decode, I role.

## Open questions

None recorded.
