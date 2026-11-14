# UnitColoursAreATintThenAFade

- **Kind:** observed behaviour
- **Scope:** engine (battle unit colours)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SceneUnit_ApplyStatusTint](../functions/SceneUnit_ApplyStatusTint.md), [SceneUnit_TintOwnRow](../functions/SceneUnit_TintOwnRow.md), [SceneUnit_RunPlacement](../functions/SceneUnit_RunPlacement.md), [UnitClut_TintRow](../functions/UnitClut_TintRow.md), [UnitClut_TintRowPlain](../functions/UnitClut_TintRowPlain.md), [ClutFade_SetTarget](../functions/ClutFade_SetTarget.md), [ClutManager_Update](../functions/ClutManager_Update.md), [ClutManager_Upload](../functions/ClutManager_Upload.md), [HdLayer_BuildTextures](../functions/HdLayer_BuildTextures.md), [sub_14026E838](../functions/sub_14026E838.md), [g_ClutManager](../globals/g_ClutManager.md), [g_ClutImage](../globals/g_ClutImage.md), [ClutBank](../structs/ClutBank.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle unit's 16 colours are its palette row put through one tint rule (status tints, ambient light), then moved by the palette manager's timed fades; the result is uploaded to the emulated video memory, where the HD layer reads it back to build the unit's textures.

## Behavior

- V: the row is one of the 16 rows of 16 colours of the classic sprite file, kept in the unit's look pool record (sub_14026E838 copies them and applies the CharShape colour override); the scene unit's byte +11 picks the row.
- V: SceneUnit_ApplyStatusTint picks the tint: one of eight status tints by the unit's flag dword, else SceneUnit_RunPlacement gives the plain row with ambient offsets (0, -4, -8 or -12 on all channels by its argument, adjusted by scene variables 35 and 36).
- V: the tint rule (UnitClut_TintRow) has four modes (plain, halved, grey, half grey) plus an offset per channel; the result is the unit slot's base row in bank 3.
- V: timed fades (ClutFade_SetTarget, ClutManager_Update) move the shown colours from where they are to a target computed from the base row, in 8 or 32 table steps, optionally back and forth.
- V (live 2026-11-11): the unit under the cursor at deployment pulses by such a fade: target = base row + 8 on all channels, 8 steps each way. The brightest colour of the test row (red 26, green 25, blue 23) moved by (0,0,1) (1,1,2) (1,2,3) (2,3,4) (3,3,5) (3,4,6) (4,5,7) on the seven steps, as the 8-step table gives for the distances 5, 6 and 8.
- V: ClutManager_Upload copies the final image into the emulated video memory; HdLayer_BuildTextures reads a draw record's 16 colours from there by the record's palette id, hashes them and keeps one texture per piece and hash.
- I: so every colour effect on a unit in battle is a change of its 16 colours before the texture pass; nothing after the pass knows the palette.

## Notes

The menu side has no manager: CharaRender_BuildAtlasTexture loads the classic file's rows itself (CharaPalette_LoadClassic) and applies the same tint rule inline by its flag bits.

## Open questions

? which status each tint flag stands for; ? other producers of unit colours (the fade callers sub_1401EAAF8.. were not read).
