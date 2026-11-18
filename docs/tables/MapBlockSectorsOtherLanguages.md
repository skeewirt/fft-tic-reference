# MapBlockSectorsOtherLanguages

- **Kind:** table
- **Area:** [Resource](../areas/resource.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B7130`
- **Rows:** 128 rows of 4 bytes
- **Keyed by:** battle map id
- **Read by:** [Map_LoadBattleData](../functions/Map_LoadBattleData.md)
- **Row layout:** [SectorOnly](../structs/SectorOnly.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle map, where its 4096-byte map block is, for the other text languages. Verdict: pointer-table.

## Behavior

- V: four more words follow the 128 sector values; they are not sectors
- V: same layout as the language-0 copy (128 dwords); 16 more bytes follow before the next symbol
- V: sub_140251584: as above for languages other than 0

## Notes

Our names. Tags: V.

## Open questions

- ?: the 4 trailing dwords
