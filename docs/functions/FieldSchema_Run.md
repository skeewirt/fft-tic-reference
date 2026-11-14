# FieldSchema_Run

- **Address:** `0x1400B024C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void FieldSchema_Run(SchemaCtx *ctx, Node *node, uint8_t *record, const FieldDesc *fields, uint32_t count)`
- **Callers:** About 54 schema functions, one per saved record (see SaveFile_Serialize, SaveWorld_Serialize, SaveUnit_Serialize and SaveJobNew_Serialize).
- **Callees:** Seven scalar helpers (`sub_1400B09B0`, `sub_1400B0A90`, `sub_1400B0B70`, `sub_1400B0C50`, `sub_1400B0D30`, `sub_1400B0E10`, `sub_1400B0EFC`), the node builders `sub_1405A483C`, `sub_1405A4690`, `sub_1405A6014`, the logger `sub_140026BD4`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The generic walker behind the game's save and config records: it takes a table of field descriptors and turns one in-memory record into a tree of named value nodes (or, for the other direction, fills a record from such a tree). About 54 schema functions call it, one per record type.

## Behavior

- V: `ctx+8` selects the direction. 0 builds the tree from the record (this routine); 1 hands over to `sub_1400B059C` for the reverse; any other value returns at once.
- V: a null node, record, field table or a zero count logs error 0x96090001 and stops.
- V: each descriptor is 88 bytes: a name pointer at +0, a type code at +8, the field's offset in the record at +12, an element size (16-bit) at +16 and an element count (16-bit) at +18, plus callback slots at +24/+32 and a lookup callback at +56/+64.
- V: for every descriptor it creates a child node named after the descriptor, fills it by type, then appends it to the parent.
- V: types 1-5 read a scalar from the record and store it in a child named `v`: 1 is an unsigned byte, 2 a signed byte, 3 a signed 16-bit value, 4 a 32-bit value, 5 a 64-bit value. A count above 1 repeats this as `var` children.
- V: type 0 calls the descriptor's own callback with the record address at the field's offset, so a field can be a nested record; with a count above 1 it builds that many `var` children, advancing by the element size.
- V: type 6 and 7 write a value-only child without reading the record; type 8 passes the record's own bytes as the node value; type 9 maps the stored value through a lookup table (pairs of text and value) returned by the descriptor's callback.
- V: errors: 0x96090000 node creation failed, 0x96090005 empty lookup table or no match and no default, 0x96090006 unknown type code. All are reported through the logger `sub_140026BD4`.
- I: the element named `v` suggests an XML-like or JSON-like tree; type 6 and 7 are probably flag or constant nodes.

## Referenced by

- Called by: [ConfigFile_Serialize](ConfigFile_Serialize.md), [ConfigGuideFlag_Serialize](ConfigGuideFlag_Serialize.md), [ConfigRoot_Serialize](ConfigRoot_Serialize.md), [ConfigSettings_Serialize](ConfigSettings_Serialize.md), [ConfigVolume_Serialize](ConfigVolume_Serialize.md), [SaveAnimUnit_Serialize](SaveAnimUnit_Serialize.md), [SaveBattleCamera_Serialize](SaveBattleCamera_Serialize.md), [SaveBlockHeader_Serialize](SaveBlockHeader_Serialize.md), [SaveCameraSettings_Serialize](SaveCameraSettings_Serialize.md), [SaveCard_Serialize](SaveCard_Serialize.md), [SaveDarlavon_Serialize](SaveDarlavon_Serialize.md), [SaveDifficulty_Serialize](SaveDifficulty_Serialize.md), [SaveEquipSet_Serialize](SaveEquipSet_Serialize.md), [SaveEquipSort_Serialize](SaveEquipSort_Serialize.md), [SaveFftPsp_Serialize](SaveFftPsp_Serialize.md), [SaveFile_Serialize](SaveFile_Serialize.md), [SaveGameFlow_Serialize](SaveGameFlow_Serialize.md), [SaveGameProgress_Serialize](SaveGameProgress_Serialize.md), [SaveIdPair_Serialize](SaveIdPair_Serialize.md), [SaveInfo_Serialize](SaveInfo_Serialize.md), [SaveIsNew_Serialize](SaveIsNew_Serialize.md), [SaveItemOpened_Serialize](SaveItemOpened_Serialize.md), [SaveJobNew_Serialize](SaveJobNew_Serialize.md), [SaveKeyNew_Serialize](SaveKeyNew_Serialize.md), [SaveLatestKey_Serialize](SaveLatestKey_Serialize.md), [SaveLibrary_Serialize](SaveLibrary_Serialize.md), [SaveMarkerTown_Serialize](SaveMarkerTown_Serialize.md), [SaveMenuNewA_Serialize](SaveMenuNewA_Serialize.md), [SaveMenuNewB_Serialize](SaveMenuNewB_Serialize.md), [SaveMenuNewC_Serialize](SaveMenuNewC_Serialize.md), [SaveMenuNewLast_Serialize](SaveMenuNewLast_Serialize.md), [SaveMoukeState_Serialize](SaveMoukeState_Serialize.md), [SaveNewArrivalListA_Serialize](SaveNewArrivalListA_Serialize.md), [SaveNewArrivalListB_Serialize](SaveNewArrivalListB_Serialize.md), [SaveNewArrivalSub_Serialize](SaveNewArrivalSub_Serialize.md), [SaveNewArrival_Serialize](SaveNewArrival_Serialize.md), [SaveNewFlags_Serialize](SaveNewFlags_Serialize.md), [SaveOpenedFlag_Serialize](SaveOpenedFlag_Serialize.md), [SavePageState_Serialize](SavePageState_Serialize.md), [SaveShopPoach_Serialize](SaveShopPoach_Serialize.md), [SaveSortie_Serialize](SaveSortie_Serialize.md), [SaveSummary_Serialize](SaveSummary_Serialize.md), [SaveUnitJobInfo_Serialize](SaveUnitJobInfo_Serialize.md), [SaveUnit_Serialize](SaveUnit_Serialize.md), [SaveUnlockProgress_Serialize](SaveUnlockProgress_Serialize.md), [SaveUwasaMouke_Serialize](SaveUwasaMouke_Serialize.md), [SaveWalkRoute_Serialize](SaveWalkRoute_Serialize.md), [SaveWork_Serialize](SaveWork_Serialize.md), [SaveWorldEvents_Serialize](SaveWorldEvents_Serialize.md), [SaveWorldMap_Serialize](SaveWorldMap_Serialize.md), [SaveWorld_Serialize](SaveWorld_Serialize.md)

## Notes

This is the engine's reflection layer for save data: adding a field to a record means adding a descriptor to its schema function.

- Correction (J7 report): the load direction (`ctx+8 == 1`) calls FieldSchema_LoadFromNode per descriptor; an absent node is skipped (error recorded, field untouched) and the return value is discarded. J9: the manual save `fftsave.bin` does not use this tree (it is a flat memory image).

## Open questions

What tree format the nodes produce and where the tree is written; what types 6 and 7 write.
