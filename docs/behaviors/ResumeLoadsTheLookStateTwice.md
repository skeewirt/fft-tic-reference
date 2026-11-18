# ResumeLoadsTheLookStateTwice

- **Kind:** observed behaviour
- **Scope:** engine (battle resume)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_140210AF0](../functions/sub_140210AF0.md), [sub_140257354](../functions/sub_140257354.md), [sub_1402181EC](../functions/sub_1402181EC.md), [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md), [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [sub_14026E838](../functions/sub_14026E838.md), [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md), [g_HdSheetEntryBySlot](../globals/g_HdSheetEntryBySlot.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle resumed from a payload copies the payload twice around the scene-variable restore, builds no scene unit but restores the scene-unit records whole, and rebuilds existing scene units from the restored slot and pool indices.

## Behavior

- V: sub_140210AF0, load mode 1 (0x142FF9E2C == 1): 0x140210C4C sub_140257354 (-> sub_1402181EC), 0x140210C51 Battle_RestoreSceneVars, then 0x140210CFF sub_140257354 again and 0x140210D04 Battle_RestoreCapture: the resume payload is copied twice, the second time after the scene variables, the queue and the look pool are restored.
- V: sub_1402181EC with a battle payload (kind 1) copies 668,112 bytes into g_SaveBattleSnapshot (0x1408167A0; the region holds g_UnitLookPoolIndex 0x140822D58) and 16 dwords into g_HdSheetEntryBySlot[13..28] (0x142E7FEA0 .. 0x142E7FEE0) from the payload's header (+276), then inflates the payload's image page with PackEntry_Inflate.
- V: Battle_RestoreCapture copies the battle unit table (0x2A00 bytes from 0x140898134), the party records and the pool face values (sub_140304BEC mode 1 from 0x1408B88F0); it does not touch the look queue or g_LookPool.
- V: a resumed battle builds no scene unit: the scene load state dword_140D3A86C comes back with the capture, and Battle_RestoreCapture calls SceneUnits_SaveRestore(capture, 1), which copies the 16 scene-unit records back (0x140D30030, 0x5480 bytes), recomputes their frame / sequence table pointers (+0x220 / +0x228 and the saved copies +0x230 / +0x238) from each record's sprite byte, rebuilds the scene list from the in-use flags, links each battle unit through g_UnitSceneSlotIndex (scene +0x148 = unit) and restores g_ClutImage (0x1C00 bytes) and g_ClutManager (0x86DC bytes).
- V: SceneUnit_BuildFromQueueEntry in load mode 1 rebuilds a unit's existing scene unit (slot from g_UnitSceneSlotIndex[unit +444], none -> no build; the record is not linked again when it was in use; pool record from g_UnitLookPoolIndex); in mode 0 it takes the scene slot named by its slot argument and links it.
- V: sub_14026E838 in load mode 1 skips the classic VRAM frame uploads of pools 0..8; the palette copy into the record (+0x30D6, 512 bytes, then CharShape_ApplyClut), the face value and the record data copy (+2, 12,500 bytes from file +0x9000) run in every mode.
- V: a resumed battle restores the 15 look pool records whole (0x2FA8A bytes: claim, sprite, palette at +0x30D6, data) and g_UnitLookPoolIndex for every battle unit, benched ones (no scene unit) included; seen live 2026-11-13: benched goblins kept record 0 naming their shape while the field goblins used record 1.

## Open questions

? how g_UnitSceneSlotIndex gets its entries back between the two payload copies is covered by SceneUnits_SaveRestore (I); the queue entries' unit pointers across a process restart were not read.
