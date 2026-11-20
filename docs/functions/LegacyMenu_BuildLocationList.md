# LegacyMenu_BuildLocationList

- **Address:** `0x1402B276C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void *LegacyMenu_BuildLocationList(void)`
- **Callers:** the legacy menu tasks
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the legacy location menu's list of unlocked world map locations.

## Behavior

- V: for locations 0..42 reads event variable 512 + n; every non-zero one is appended to the live location list (the table at 0x140789550) as 0x9000 + n (computed as n minus 0x7000 in a 16-bit word).
- V: a parallel state word list gets 0 when event variable 615 + n is non-zero, otherwise 8, and 4 for the location equal to event variable 49 (the current one).
- V: splits the count into a page of 7 and the overflow, and picks the cursor row so the current location is visible.

## Notes

Name is ours.

## Open questions

None recorded.
