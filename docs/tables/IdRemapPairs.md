# IdRemapPairs

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** Executable
- **Address:** `0x140718C50`
- **Rows:** 406 rows of 56 bytes (2842 pairs)
- **Keyed by:** scanned linearly by id (ids above 0xA7)
- **Read by:** [IdRemap_Lookup](../functions/IdRemap_Lookup.md)
- **Row layout:** [IdRemapRow](../structs/IdRemapRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An id alias table: IdRemap_Lookup scans every row for the id; an unknown id maps to itself.

## Behavior

- V: the lookup scans all rows (no sort order assumed).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: what the ids and their replacements are
