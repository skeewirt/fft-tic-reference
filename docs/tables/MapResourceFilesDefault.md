# MapResourceFilesDefault

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x140685450`
- **Rows:** 128 rows of 8 bytes
- **Keyed by:** battle map id (dword_140784478)
- **Read by:** [MapResource_Read](../functions/MapResource_Read.md)
- **Row layout:** [MapResourceFileListPointer](../structs/MapResourceFileListPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle map, where its resource files are, for text languages other than 0 (the copy of MapResourceFilesLanguage0 that the reader picks when the language record is not 0). Verdict: pointer-table.

## Behavior

- V: CORRECTION: the table starts at 0x140685450, not at 0x140685438; the review address is slot 125 of the language 0 table, and its first three entries are the last three of that table
- V: 128 slots, slots 120..124 null; two non-pointer words follow it
- V: the reader takes this table (off_140685450) unless the language record says language 0, then reads pair [n] of the current map's list from its sector
- V: 123 of 128 slots are non-null and the empty slots are 120..124 as in the language 0 table; every sector list differs from the language 0 list of the same map
- I: the sweep candidate 0x140685438 began three slots early, inside the last entries of the language 0 table

## Notes

Our names. Tags: V layout, V reader.

## Open questions

- ?: what each pair index n is (mesh / texture / ...)
