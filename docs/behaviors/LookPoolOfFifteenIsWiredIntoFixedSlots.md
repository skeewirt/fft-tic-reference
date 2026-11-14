# LookPoolOfFifteenIsWiredIntoFixedSlots

- **Kind:** observed behaviour
- **Scope:** engine (battle look pool size)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [LookPool_ClaimForSprite](../functions/LookPool_ClaimForSprite.md), [LookPool_ResetForBattleLoad](../functions/LookPool_ResetForBattleLoad.md), [sub_14026E838](../functions/sub_14026E838.md), [sub_14026EB74](../functions/sub_14026EB74.md), [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md), [CharaPalette_ReloadForShape](../functions/CharaPalette_ReloadForShape.md), [g_LookPool](../globals/g_LookPool.md), [g_SnapshotLookPool](../globals/g_SnapshotLookPool.md), [g_PoolFrameBuffers](../globals/g_PoolFrameBuffers.md), [g_HdSheetEntryBySlot](../globals/g_HdSheetEntryBySlot.md), [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The look pool's 15 records are not a constant that a same-length change can raise: the record block is followed at once by the scene-unit slots, each pool index owns fixed GPU upload positions or buffers, the HD sheet slots cover pools 0..9, and the battle snapshot holds exactly 15 records.

## Behavior

- V: g_LookPool spans 0x140D005A0..0x140D3002A (15 x 0x32D6); the scene-unit in-use dwords start at 0x140D30030 and g_SceneUnitSlots at 0x140D30038.
- V: 14 functions address the block (LookPool_ClaimForSprite, LookPool_ResetForBattleLoad, CharaPalette_ReloadForShape, sub_14026E838, sub_14026C2E8, SceneUnit_RunPlacement, sub_14026929C, SceneUnit_SyncSpriteFromPool, sub_14026E0F4, sub_140273468, sub_1401D4544, sub_1401D46B0, sub_140210AF0, Battle_RestoreSceneVars); the count 15 is an immediate in LookPool_ClaimForSprite and an end address in the others.
- V: sub_14026E838: pools 0..8 upload through sub_140260718 at positions derived from the index, pools 9..14 copy into 32 KB buffers 2..7 at 0x1437ADF4C + ((pool - 7) << 15) and 4 KB blocks at 0x1437B5F4C + 4096 * (pool & 7); a pool 15 would write from 0x1437EDF4C (other globals) and its pointer over dword_1411A37C8.
- V: sub_14026EB74: the HD sheet slot word is pool + 20 for pools 0..8 and 17 from 9; only pools 0..9 get an HD sheet entry (g_HdSheetEntryBySlot[20..28], dword_142E7FEE0).
- V: Battle_RestoreSceneVars copies exactly 0x2FA8A bytes (15 records) from g_SnapshotLookPool, which lies in the 668,112-byte snapshot region a resume payload fills (sub_1402181EC).
- I: a pool of more than 15 looks per load needs the records relocated, a GPU slot or buffer per new index, HD sheet slots for them, wider face values and a snapshot of its own.

## Open questions

None recorded.
