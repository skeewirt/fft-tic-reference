# LegacyItemCursorTemplates

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406931C0`
- **Rows:** 5 rows of 8 bytes
- **Keyed by:** kind 0..4
- **Row layout:** [LegacyItemCursorTemplatesRow](../structs/LegacyItemCursorTemplatesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Five pointer slots (first empty) to the cursor window templates of the legacy item pages. Verdict: pointer-table.

## Behavior

- V: 0x26 bytes to the next object; the four pointers target the template block at 0x1407B2540..0x1407B2710
- V: sub_140396FEC: loads qword [kind] to pick a cursor template for the item page
- V: sub_140394940: also references the table

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: the exact slot count (the last slot is partly overlapped by the next object)
