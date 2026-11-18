# SpriteNumberTables

- **Kind:** registry
- **Area:** [Graphics](../areas/graphics.md)
- **Resolved by:** [CharaRender_BuildAtlasTexture](../functions/CharaRender_BuildAtlasTexture.md), [CharaPalette_LoadClassic](../functions/CharaPalette_LoadClassic.md), [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every table the executable indexes by sprite number, with the row count, the bound the code applies.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="hd_entry"></a>1 | `hd_entry` | `0x1407151F0, 170 rows x 4` | V | Signed first g2d entry per sprite (-1 none). Bounds 0xA9 (three 32-bit compares, in CharaRender_BuildAtlasTexture and twice in SceneUnit_BuildFromQueueEntry) and 0xAA (four byte compares on the scene unit's sprite byte). 7 sites (1 rip, 6 img): the eighth operand of the address-range count is not a reader (behaviour UnitFaceIndexReadsTheTableAfterTheHdTable). |
| <a id="classic_kind"></a>2 | `classic_kind` | `0x784690, 170 rows x 8` | V | Classic file number and size per sprite. No bound in code except the load pass replacing values above 170 by 1 (CharaPalette_ReloadForShape). |
| <a id="classic_kind_twin"></a>3 | `classic_kind_twin` | `0x784BE0, 170 rows x 8` | V | Language-0 twin of the table above (same rows). |
| <a id="attribute"></a>4 | `attribute` | `0x673300, 170 rows x 4` | V | Frame file type, sequence file type, pose-remap flag and a byte of 0, 0x24, 0x3C or 0x78 per sprite; row 170 is the first row of another table; 24 reading sites (17 rip, 7 img; four of the lea sites point at byte 1, 2 or 3 of row 0); no bound. |
| <a id="portrait_code_a"></a>5 | `portrait_code_a` | `0x680070, 211 rows x 2` | V | Portrait code per sprite, read by PartyUnit_BuildJobRecord with bound 0xD3. |
| <a id="portrait_code_b"></a>6 | `portrait_code_b` | `0x6807C0, 211 rows x 2` | V | Same words, read by Unit_GetSpriteSetId with bound 0xD3. |
| <a id="portrait_code_c"></a>7 | `portrait_code_c` | `0x680C00, 211 rows x 2` | V | Same words; no reader: no code operand and no data pointer reaches it. |
| <a id="portrait_code_d"></a>8 | `portrait_code_d` | `0x681A90, 211 rows x 2` | V | Same words, read by EventMessage_Scripted with bound 0xD3. The byte read of sub_1402F8188 at row 210 is a different table that starts there. |
| <a id="portrait_code_e"></a>9 | `portrait_code_e` | `0x6829F0, 211 rows x 2` | V | Same words, read by sub_140300768 and sub_140300D74, each with bound 0xD3. |
| <a id="portrait_code_f"></a>10 | `portrait_code_f` | `0x683A70, 211 rows x 2` | V | Same words, read by sub_14032AB3C with bound 0xD3. |
| <a id="code_to_face"></a>11 | `code_to_face` | `0x7146D0, 160 rows x 4` | V | Face number per portrait code up to 0x9F (g_SpriteIdToShape); eleven reading sites; face numbers above 0xCD become -1. |
| <a id="charshape_nxd"></a>12 | `charshape_nxd` | `NXD table 174 (0xAE), key = sprite` | V | Row per sprite (colour override id at +12, other fields); rows exist for keys 0 to 158; twelve functions look it up; CharShape_ApplyClut takes the key as a byte. |
| <a id="frame_files"></a>13 | `frame_files` | `0x785130 and twin 0x785180, 9 rows x 8` | V | File and size per attribute byte 0 value; the load pass reads a row when the value is 5 or more. Indexed by an attribute value, not a look. |
| <a id="sequence_files"></a>14 | `sequence_files` | `0x784610 and twin 0x7845B0, 8 rows x 8` | V | File and size per attribute byte 1 value; read when the value is 5 or more. Indexed by an attribute value, not a look. |

## Behavior

- V: entry 7 has no reader; entries 12 to 14 are not indexed in the exe by a look number or are game data.

## Open questions

None recorded.
