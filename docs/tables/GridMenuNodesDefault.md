# GridMenuNodesDefault

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408EC860`
- **Rows:** 5 rows of 88 bytes
- **Keyed by:** menu node number
- **Read by:** [GridScreen_Task](../functions/GridScreen_Task.md)
- **Row layout:** [LegacyMenuNode](../structs/LegacyMenuNode.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Legacy menu nodes of the grid screen, default language. Verdict: designer-data.

## Behavior

- V: chosen when the language record is not 0 and published as the live menu tree
- I: five nodes by the 0x1B8 span up to the row cursor words at 0x1408ECA18

## Notes

Our names. Found beside the table at 0x1408EC858; tags V, I count.

## Open questions

None recorded.
