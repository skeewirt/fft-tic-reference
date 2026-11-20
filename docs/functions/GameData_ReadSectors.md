# GameData_ReadSectors

- **Address:** `0x1402F40C4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t GameData_ReadSectors(int kind, int sectorIndex, uint32_t size, void *buffer)`
- **Callers:** About 24 callers, including CharaRender_InitTargets, CharaRender_BuildAtlasTexture and `sub_14023A868`.
- **Callees:** EventScript_LoadFile, `sub_1402F3A3C`, `sub_1402F3D58`, `sub_1403D2358`, `sub_14033D6B0`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The game's general data read entry point, expressed in the original disc layout: it reads a run of 2048-byte sectors of one kind of game file, and sends event scripts (kind 17) to EventScript_LoadFile.

## Behavior

- V: the first call runs `sub_1402F3A3C(kind)` once and sets `byte_142FEC54E`; a non-zero result is returned at once.
- V: kind 17 calls EventScript_LoadFile(sectorIndex, buffer); kind 767 reads nothing.
- V: any other kind is looked up in an 18-entry table (language-dependent: `unk_140681F90` or `unk_1408EABE0`); a match calls the per-kind loader `sub_1402F3D58(kind, buffer)`.
- V: otherwise it reads `size` bytes from the open data pack (`qword_143793118`) at the kind's start offset plus `sectorIndex * 2048`.
- V: afterwards it clears the high dword of `qword_141856AB0`, calls the hook `sub_14033D6B0(kind, sectorIndex, kind)`, and returns 0.
- V: about 24 callers, among them the sprite-texture loaders CharaRender_InitTargets and CharaRender_BuildAtlasTexture and the event-script users.
- V (2026-11-10): sub_14033D6B0 does nothing for a kind above 0x303 other than 772 and 876; CharaPalette_LoadClassic reads a sprite's classic file through here (kind and size from SpriteClassicFilesByShape row of the shape, both u32).
- V (2026-11-12): EventDataLoad_Poll reads a battle effect file through here: GameData_ReadSectors(file number, 0, the table's size, unk_1418A2E00), the file number from EffectFile_GetTrackRow.

## State touched

- Calls: [EventScript_LoadFile](EventScript_LoadFile.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [CharaPalette_LoadClassic](CharaPalette_LoadClassic.md), [CharaPalette_ReloadForShape](CharaPalette_ReloadForShape.md), [EventDataLoad_Poll](EventDataLoad_Poll.md), [EventScript_LoadIntoBuffer](EventScript_LoadIntoBuffer.md), [EventSprite_LoadTask](EventSprite_LoadTask.md), [MapResource_Read](MapResource_Read.md), [Map_LoadBattleData](Map_LoadBattleData.md), [Save_BootClear](Save_BootClear.md), [TextKind25_LoadPool](TextKind25_LoadPool.md), [sub_140300D74](sub_140300D74.md)
- Called by event opcodes: [0x50](../opcodes/README.md)
- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md), [ClassicSpriteFilesByNumber](../behaviors/ClassicSpriteFilesByNumber.md), [EnhancedDrawsHdSheetsWithTheClassicFilePalette](../behaviors/EnhancedDrawsHdSheetsWithTheClassicFilePalette.md), [MapLoaderIndexesThreeTablesByASixteenBitMapId](../behaviors/MapLoaderIndexesThreeTablesByASixteenBitMapId.md), [MapResourceFilesAreFileNumberAndSizePairsPerMap](../behaviors/MapResourceFilesAreFileNumberAndSizePairsPerMap.md), [SpriteSheetPortraitAndPartFiles](../behaviors/SpriteSheetPortraitAndPartFiles.md), [SpriteSheetsAndClassicFilesByNumber](../behaviors/SpriteSheetsAndClassicFilesByNumber.md)
- Reads file formats: [SpriteSheetEntries](../formats/SpriteSheetEntries.md)

## Notes

Keeps the engine's original sector-based addressing on top of the remastered file layout.

## Open questions

What the 18 special kinds are and what `sub_1402F3A3C` initialises.
