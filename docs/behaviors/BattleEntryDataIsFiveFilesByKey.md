# BattleEntryDataIsFiveFilesByKey

- **Kind:** observed behaviour
- **Scope:** engine (battle unit entries)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [TextKind25_LoadPool](../functions/TextKind25_LoadPool.md), [Battle_GetEntryBlock](../functions/Battle_GetEntryBlock.md), [Battle_BuildEntryUnits](../functions/Battle_BuildEntryUnits.md), [OverrideEntry_LoadBattleEntries](../functions/OverrideEntry_LoadBattleEntries.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The entry key (variable 50) selects 16 entries of 40 bytes: keys 1..127 read from file 224, 128..255 from 225, 256..383 from 226, 384..511 from 227 (81,920 bytes each, 128 keys), and keys 512..591 from file 892 (51,200 bytes, 80 keys); the block address has no bound.

## Behavior

- V: TextKind25_LoadPool allocates 0x14000 bytes and reads 81,920 bytes of file 224 + (key div 128) for keys below 512, and allocates 0xC800 bytes and reads 51,200 bytes of file 892 for keys of 512 and above.
- V: Battle_GetEntryBlock returns the loaded base + 640 x index, with the index the key reduced below 128 (or the key minus 512); there is no comparison with the file's key count, so key 592 or more addresses memory past the buffer.
- V: key 0 means no entries.
- V: the OverrideEntryData rows are looked up with the same key (and index 0..15) and overwrite the entries in place.
- I: the entry tiles are absolute map coordinates; no table maps an entry key to a map id.

## Notes

The entry keys of the stock scenario records reach 585; the random formations are below 229.

## Open questions

? the offsets of the tile and facing bytes inside the 40-byte entry.
