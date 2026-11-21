# WordSeventeensArithmeticReachesNewSheetGroups

- **Kind:** observed behaviour
- **Scope:** engine (battle unit looks, Enhanced HD)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [HdLayer_ResolveQuadTexture](../functions/HdLayer_ResolveQuadTexture.md), [HdLayer_BindSheetTexture](../functions/HdLayer_BindSheetTexture.md), [HdLayer_BuildTextures](../functions/HdLayer_BuildTextures.md), [HdQuad_CopyFromDrawQuad](../functions/HdQuad_CopyFromDrawQuad.md), [sub_140260CF0](../functions/sub_140260CF0.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md), [HdSheetGroups_ConstructAll](../functions/HdSheetGroups_ConstructAll.md), [HdSheetGroups_ClearUsedMarks](../functions/HdSheetGroups_ClearUsedMarks.md), [HdSheetGroups_DestroyAll](../functions/HdSheetGroups_DestroyAll.md), [HdSheetGroup_Construct](../functions/HdSheetGroup_Construct.md), [g_HdSheetGroups](../globals/g_HdSheetGroups.md), [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every look past the 10th draws correctly in HD, with its own portrait, once it has a sheet group of its own: the code of sheet word 17 computes slot and group from the draw id by arithmetic that continues past its stock end, so a look 10 + k reached through draw ids 10371 + 16k lands on HD slots 379 + 16k and group 20 + k with no new code.

## Behavior

- V: word 17 takes draw id 10259 + palette entry (sub_140260CF0, after HdSheetGroup_ClaimClutEntry(13, ...)); its branches compute slot = id - 9992 (HdLayer_ResolveQuadTexture: r15 + 267 from r15 = id - 10259) and group = (id - 10259) / 16 + 13 (HdLayer_ResolveQuadTexture, HdLayer_BuildTextures at 0x1404163B5, HdLayer_BindSheetTexture at 0x14041D8D6, each after a range test of that value against 15); so ids 10259 + 16 (g - 13) + entry address group g for any g.
- V: the ids after the last stock range (10370) and the slots after the last stock slot (378) are used by no range test of HdLayer_ResolveQuadTexture, HdQuad_CopyFromDrawQuad, HdLayer_BindSheetTexture or HdLayer_BuildTextures; a group's pieces get their textures from the group itself (HdSheetGroup_Construct layout), so the per-slot tables of the texture pass (379 wide) are not used for them; the texture pass caps a record's slot at 378 (0x1404161E5) and marks every handle 0x800 + slot in a stack array of 380 dwords (0x140415EC7).
- V: the groups are built by a static initializer (HdSheetGroups_ConstructAll, count 20) and destroyed at exit (HdSheetGroups_DestroyAll, count 20 and the array's end); three loops stop at the array's end (sub_1401E7440's reset at battle release, the piece aging in HdLayer_BuildTextures, the destructor) and one counts 20 (HdSheetGroups_ClearUsedMarks).
- V: HdLayer_BindSheetTexture takes the sheet entry of word 17's groups from dword_142E7FEE0 + 4 x (group - 13); only group 13's dword is word 17's (SceneUnit_BuildFromQueueEntry writes it for record 9), the dwords after it are other state.
- V (tested 2026-11-21, random battle at Mandalia Plain, the battle's entries replaced with 11 distinct monster families, variable 57 forced to -7, 4 party units: 15 distinct looks): with the group array moved in memory to room for 31 groups (its 43 operands, the three end pointers and the three counts), the slot cap raised to 554, the mark loop skipping handles from 0x800 + 379, word 17's four range tests also accepting the values 112..287, the palette claim and the draw id of records 10.. taken to group 20 + k (record 10 + k) with the record's own sheet entry kept beside the stock one, and g_LookPoolFaceValue moved to 21 entries with its ten readers' tests raised to 21: the Dryad (record 10) and the four party units (records 11..14) drew correctly in HD, at deployment and in battle, and showed their own portraits in the deployment list, the unit panels and the Combat Timeline; the other ten looks were unchanged; from Commence through the enemies' opening turns no fault was recorded.

## Open questions

? a mid-battle resume with looks past the 10th (the capture copies 10 face values); ? the classic (low-resolution) path for records past 14.
