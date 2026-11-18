# GridAvailability_Reset

- **Address:** `0x1402FC6D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GridAvailability_Reset(void)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets the availability flags of the grid screen entries.

## Behavior

- V: copies the 54-byte template at 0x1408ECA20 into the live flag area at 0x1437A04D0.
- V: then for each of four unit groups (25 slots each) except the current group clears the flag of every entry whose unit number appears in the 54-entry unit list at dword_1437A0510.

## Referenced by

- Reads tables: [GridAvailableTemplate](../tables/GridAvailableTemplate.md)

## Notes

Read in full (small function).

## Open questions

None recorded.
