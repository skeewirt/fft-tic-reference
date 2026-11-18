# MapBlockSectorsLanguage0

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B6F30`
- **Rows:** 128 rows of 4 bytes
- **Keyed by:** battle map id
- **Read by:** [Map_LoadBattleData](../functions/Map_LoadBattleData.md)
- **Row layout:** [SectorOnly](../structs/SectorOnly.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle map, where its 4096-byte map block is, for text language 0. Verdict: pointer-table.

## Behavior

- V: the 128 values are sector numbers, not pointers; the other-language copy differs by one in every filled row
- V: 0x200 = 128 dwords to the other-language copy
- V: sub_140251584 (map loader): reads the block for language 0 (0x1407B7130 otherwise); 123 of 128 maps have one

## Notes

Our names. Tags: V.

## Open questions

- ?: what the 4096-byte block holds
