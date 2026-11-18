# MapResourceFilesAreFileNumberAndSizePairsPerMap

- **Kind:** observed behaviour
- **Scope:** engine (battle map resources)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapResource_Read](../functions/MapResource_Read.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

MapResource_Read reads one resource file of the current map: a request record either carries a file number and a size itself, or carries the marker value 0xFEEDBACC (as a 32-bit number) and a pair number, which selects a {file number, size} pair from the list the map's pointer in the per-map table names.

## Behavior

- V: a request with its flag byte (+13) at 0 reads nothing; otherwise the file number is the dword at +2 and the size the dword at +6.
- V: when the dword at +2 holds the marker, the table of the current language (language 0 or the other) is indexed by the current map id (32-bit global at 0x140784478) to a pointer; a null pointer ends the read with nothing read, a non-null pointer is a list of 8-byte pairs {file number, size}, read at pair number = the dword at +6.
- V: a read happens only when the resulting size is not 0 and a destination is given; the read is GameData_ReadSectors(file number, 0, size, destination).
- V: the two pointer tables have 128 entries each and exactly one reader; there is no bound on the map id there.
- I: the lists live in shared read-only data, so a table row is a pointer into that pool, not a list of its own.

## Notes

A request that names its file number directly does not use the per-map list at all, so a map's resource files can be named inside the map block alone.

## Open questions

None recorded.
