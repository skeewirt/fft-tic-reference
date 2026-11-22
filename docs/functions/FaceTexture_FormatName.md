# FaceTexture_FormatName

- **Address:** `0x1400FC22C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int FaceTexture_FormatName(char *out, unsigned face, int colour)`
- **Callers:** FaceWidget_SetFace, sub_14010ABE4, sub_1401389C4, sub_140144E24, SortieScreen_SetArea0Face, SortieScreen_SetArea1Face
- **Callees:** UITexturePath_FromRow, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Formats the texture name of a face: the format string of UI texture path row 4 with the face number and the colour.

## Behavior

- V: UITexturePath_FromRow(4, format, 260) fetches the format; Str_Format(out, 256, format, face, colour) fills out.
- V (live 2026-11-10): the name is a texture-parts path (UITexturePath_FromRow puts the 'UITextureParts' scheme before the row's text) to the part file ui/ffto/common/face/textureparts/wldface_<face>_<colour>_uitx.utexpt, the face with at least 3 digits and the colour with 2. The part file names the texture (ui/ffto/common/face/texture/wldface_<face>_<colour>_uitx.tex) and cuts it into 9 parts: the whole 520 x 388 picture ('TexturePart'), Eye00..02, Mouth00..03 and 'All'.
- V (game files): the shipped faces are wldface_001..204 (sparse) in colours 08..12; a texture with no part file is not drawn (the slot stays blank).

## State touched

- Calls: [UITexturePath_FromRow](UITexturePath_FromRow.md), [Str_Format](Str_Format.md)

## Referenced by

- Appears in flows: [PartyMenuFaceChain](../flows/PartyMenuFaceChain.md)
- Called by: [FaceWidget_SetFace](FaceWidget_SetFace.md), [SortieScreen_SetArea0Face](SortieScreen_SetArea0Face.md), [SortieScreen_SetArea1Face](SortieScreen_SetArea1Face.md)
- Observed behaviours: [SpriteSheetPortraitAndPartFiles](../behaviors/SpriteSheetPortraitAndPartFiles.md)

## Notes

No bound on the face number (1300 works). The name is ours (IDB: sub_1400FC22C).

## Open questions

None recorded.
