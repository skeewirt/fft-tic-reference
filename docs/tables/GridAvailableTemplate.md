# GridAvailableTemplate

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408ECA20`
- **Rows:** 54 rows of 1 bytes
- **Keyed by:** selectable slot
- **Read by:** [GridAvailability_Reset](../functions/GridAvailability_Reset.md)
- **Row layout:** [AvailabilityFlag](../structs/AvailabilityFlag.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Initial availability flags of the grid screen entries. Verdict: engine-data.

## Behavior

- V: copied as 54 bytes into the live flag area, then flags of placed units are cleared

## Notes

Our names. Tags: V copy, I role.

## Open questions

None recorded.
