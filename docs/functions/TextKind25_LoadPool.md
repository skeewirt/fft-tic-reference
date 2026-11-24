# TextKind25_LoadPool

- **Address:** `0x140284098`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void TextKind25_LoadPool(void)`
- **Callers:** sub_1402841D0, BattleLoad_StepFresh, sub_14030476C
- **Callees:** ResourcePool_AllocBlocks, GameData_ReadSectors

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the text pool that serves text kind 25 (base 0xC800): it sizes the buffer from the current pool count, allocates it, and reads one of five sectors into it.

## Behavior

- V: the current pool selector is the dword at 0x141856930; a zero selector returns without loading.
- V: a selector of 0x200 or more allocates 0xC800 bytes and reads sector 0x37C.
- V: a selector below 0x80 reads 0x14000 bytes from sector 0xE0; 0x80..0xFF uses 0xE1, 0x100..0x17F uses 0xE2 and 0x180..0x1FF uses 0xE3 (the ranges are written as the compare bounds 0x100, 0x180 and 0x200).
- V: the buffer pointer is stored at 0x141856938 and the allocation is checked for null before the read.
- V: GameData_ReadSectors performs the actual read; the function returns without a value.
- V: the three callers are the text decoder, the NXD loader and the second event text path, so the pool is shared.
- I: the five sectors are size variants of the same text pool, selected by the pool count rather than by language.
- ?: what the selector at 0x141856930 counts; this body only compares it with the four thresholds.

## State touched

- Calls: [ResourcePool_AllocBlocks](ResourcePool_AllocBlocks.md), [GameData_ReadSectors](GameData_ReadSectors.md)

## Referenced by

- Called by: [BattleLoad_StepFresh](BattleLoad_StepFresh.md), [Party_RebuildFromBattleEntry](Party_RebuildFromBattleEntry.md), [sub_14030476C](sub_14030476C.md)
- Observed behaviours: [BattleEntryDataIsFiveFilesByKey](../behaviors/BattleEntryDataIsFiveFilesByKey.md)

## Notes

Whole function read (210 bytes). The address is one of the two producers of kind 25 text.

## Open questions

None recorded.
