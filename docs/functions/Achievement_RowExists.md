# Achievement_RowExists

- **Address:** `0x1400DCB3C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool Achievement_RowExists(...)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tests that the Achievement row of key 9 exists.

## Behavior

- V: the function reads only the existence of the row (key 9).

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Open questions

None recorded.
