# HdLayerUnitSheetsAreTenFixedGroups

- **Kind:** observed behaviour
- **Scope:** engine (Enhanced battle HD sprites)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [sub_140260CF0](../functions/sub_140260CF0.md), [HdLayer_ResolveQuadTexture](../functions/HdLayer_ResolveQuadTexture.md), [HdLayer_BindSheetTexture](../functions/HdLayer_BindSheetTexture.md), [HdLayer_BuildTextures](../functions/HdLayer_BuildTextures.md), [HdSheetGroup_ClaimClutEntry](../functions/HdSheetGroup_ClaimClutEntry.md), [HdSheetGroup_FindOrAddPiece](../functions/HdSheetGroup_FindOrAddPiece.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle HD layer draws unit sheets through fixed sheet groups, one per look pool record 0..9, each owning 16 of the HD layer's 379 texture slots; every group, slot range and slot table is in use or packed against other data, so a further unit sheet needs new groups, slots and tables, not a free one.

## Behavior

- V: a scene unit's sheet word (+0x14) is pool + 20 for pools 0..8 and 17 for pools 9..14 (SceneUnit_BuildFromQueueEntry); sub_140260CF0 turns the word into a draw id: words 20..28 -> 10115 + 16 x (word - 20) + the palette entry (group word - 16), word 17 -> 10259 + entry (group 13), words 4 / 5 -> groups 0 / 1 (18 / 19 for their alternates), word 9 -> group 2 (entry fixed 161), word 11 -> group 3 (160), word 30 -> group 14 (158); the palette entry is HdSheetGroup_ClaimClutEntry(group, the quad's CLUT word), one of 16 per group.
- V: HdLayer_ResolveQuadTexture maps each draw id range to HD slot id - 9992 and its group; the ranges reach HD slot 378 (draw id 10370), and HdLayer_BindSheetTexture binds every slot range 59..378 to a sheet slot dword (slots 16..35 of g_HdSheetEntryBySlot) or to the effect pages (sub_1400D29F0, slots 299..346).
- V: the 20 groups (g_HdSheetGroups, 21144 bytes each, 0x142EA63E0) are all referenced: 0..3 the extra pages and the sprites 160 / 161, 4..13 the ten pool sheets, 14 sprite 158, 15..17 the effect pages, 18 / 19 the alternates of words 4 / 5; qword_142F0D7C0 (other data) follows group 19.
- V: the sheet slot dwords sit inside a larger block of video state: indices 11..15 and 36.. are other variables (EventSprite_LoadTask, VideoState_InitDefaults, Video_RefreshState and others).
- V: the HD layer's per-slot tables in HdLayer_BuildTextures are exactly 379 wide and lie back to back (the entry table, the palette-id table, the texture objects of 112 bytes).

## Open questions

? whether draw ids above 10370 are used anywhere else.
