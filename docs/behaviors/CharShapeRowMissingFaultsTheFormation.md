# CharShapeRowMissingFaultsTheFormation

- **Kind:** observed behaviour
- **Scope:** engine (battle formation)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md), [CharShape_ApplyClut](../functions/CharShape_ApplyClut.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle formation code reads a CharShape row (NXD 174) keyed by the scene unit's sprite byte and, on one path, reads the row's byte +0x2C with no row: a sprite number without a CharShape row faults.

## Behavior

- V: sub_140216EB4 (from sub_140213F14) loads the key from the scene unit's +0xA (0x14021708E), looks the row up through NxdRegistry_Find(0xAE) and NxdTable_GetRowById, and when the entry is null sets the row pointer to 0 (0x140217157) before reading +0x2C at 0x140217172.
- V: NxdTable_GetRowById checks the key against the table's minimum and maximum, then indexes densely or searches; it has 474 references.
- I: the CharShape row is 48 bytes in column order (DLCFlags +0, comment string offset +4, ids +8..+36, bytes +40..+47, Height at +44): the offsets the readers use (+8, +12, +16, +20..+32, +44, +45, +46) match.
- V: an entry whose first qword is negative stands for the static default row at 0x1406F5ED0 (CharShape_ApplyClut, SceneUnit_BuildFromQueueEntry), so 'a row of its own' is an entry with a non-negative first qword and a non-null NxdEntry_GetRow.

## Open questions

? whether the loaded NXD rows are writable in place in the game (I: heap memory filled from the file; not observed live).
