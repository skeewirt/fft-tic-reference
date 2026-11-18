# MapResourceFilesLanguage0

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable
- **Address:** `0x140685050`
- **Rows:** 128 rows of 8 bytes
- **Keyed by:** battle map id (dword_140784478)
- **Read by:** [MapResource_Read](../functions/MapResource_Read.md)
- **Row layout:** [MapResourceFileListPointer](../structs/MapResourceFileListPointer.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle map, where its resource files are, for text language 0. Verdict: pointer-table.

## Behavior

- V: 128 slots, 123 non-null; slots 120..124 are null; the table is followed directly by the other-language table (MapResourceFilesDefault) at +0x400
- V: 0x400 bytes = 128 pointers; the copy for the other languages is 0x140685450
- V: sub_140251640: for a map resource request with the marker id, takes pair [n] of the current map's list and reads that many bytes from that sector

## Notes

Our names. Tags: V.

## Open questions

- ?: what each pair index n is (mesh / texture / ...)
