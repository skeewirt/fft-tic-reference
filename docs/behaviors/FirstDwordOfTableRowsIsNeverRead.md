# FirstDwordOfTableRowsIsNeverRead

- **Kind:** observed behaviour
- **Scope:** engine (nxd table access)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [NxdTable_BinarySearchRow](../functions/NxdTable_BinarySearchRow.md), [NxdEntry_GetRow](../functions/NxdEntry_GetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

No shared code reads the first dword of a table row; a row is found through the key / offset index record, so the value there decides nothing.

## Behavior

- V: the entry array of a single-key table points at an 8-byte (key, row offset) index record; NxdTable_BinarySearchRow compares that key and NxdEntry_GetRow adds the offset.
- V: the 13 places that load from the row pointer right after NxdEntry_GetRow are string-offset loads of other tables, not reads of the row's first dword.
- M: in EventId (2 rows), CharaName (179 rows) and GameProgress (105 rows) a first dword of 1 occurs only on otherwise empty rows, but one CharaName row and 16 GameProgress rows are empty with 0, so the value does not exactly mark empty rows.

## Open questions

None recorded.
