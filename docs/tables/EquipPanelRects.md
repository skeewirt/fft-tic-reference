# EquipPanelRects

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F3740`
- **Rows:** 10 rows of 8 bytes
- **Keyed by:** rectangle index (screen origin and VRAM staging rectangles of the equip panels)
- **Read by:** [sub_14032EDB8](../functions/sub_14032EDB8.md), [sub_14032F410](../functions/sub_14032F410.md), [sub_14032F9F8](../functions/sub_14032F9F8.md)
- **Row layout:** [UiRect](../structs/UiRect.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The panel origins and VRAM staging rectangles of the equip screen panels: two palette row rectangles, then screen rectangles and two texture strip rectangles. Verdict: designer-data.

## Behavior

- V: rectangle 2..4 (0x3750, 0x3758, 0x3760) are read as the panel origin by the three equip panel tasks
- V: rectangles at 0x3780 and 0x3788 are copied to VRAM as texture strips (the staging copy)
- I: ten rectangles up to the first cell table

## Notes

Our names. Found beside the table at 0x1408F3778; tags V reads, I count.

## Open questions

None recorded.
