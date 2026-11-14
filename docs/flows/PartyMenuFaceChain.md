# PartyMenuFaceChain

- **Kind:** flow
- **Area:** [Graphics](../areas/graphics.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a party unit's face reaches a menu with enhanced graphics: the save record's marker and job give a look index, the index a portrait code, the code a byte and a colour, the byte a face number through the face table, and the face number a texture name. Every step after the code is a byte, so at most 256 faces can come out of a code.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md) | V | A screen asks for a unit's face: mode 1 when both dwords of qword_142FF9F30 are 0 (party list, job screen and status headers, errand result); mode 0 goes to the battle pool path (sub_140214134). |
| <a id="2"></a>2 | [g_SceneIdWord](../globals/g_SceneIdWord.md) | V | Scene ids 21, 43, 44 and 51 take the selector branch (scene unit entries, SceneUnit_EntryById); every other scene takes the save-record branch with index below 0x36. |
| <a id="3"></a>3 | [sub_14032AB3C](../functions/sub_14032AB3C.md) | V | Look index from the marker: below 0x80 itself, 0x80 / 0x81 2 * job - 52 / - 51, 0x82 job row +46, 0xA2 / 0xA3 fixed; index below 0xD3 reads the code word of copy F. |
| <a id="4"></a>4 | [sub_14032AB3C](../functions/sub_14032AB3C.md) | V | A code with bit 8 or 9 set is refused (-1); marker 0x82 adds job row +47 << 10 (colour bits). |
| <a id="5"></a>5 | [PortraitCode_FillCell](../functions/PortraitCode_FillCell.md) | V | The classic atlas cell of the code's low byte and the colour 8 + bits 10..11; returns the low byte. |
| <a id="6"></a>6 | [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md) | V | No code (-1): the record index stands in for it. The unmapped value goes to g_HdFaceSlotValues[0] and g_DialogueFaceSlot0; the UI table 0x112 row of the marker adjusts the colour. |
| <a id="7"></a>7 | [g_GraphicsLevel](../globals/g_GraphicsLevel.md) | V | Below 2.0 the function returns -1 (no face from this path). |
| <a id="8"></a>8 | [SpriteId_ToShape](../functions/SpriteId_ToShape.md) | V | When g_FaceDisplayMode & ~2 is 0 the code becomes a face number through g_SpriteIdToShape (or SpriteId_ToShape's list); an unmapped code is returned as it is; then the cap 0xCD (0x1402C0816) turns a larger answer into -1. |
| <a id="9"></a>9 | [FaceWidget_SetFace](../functions/FaceWidget_SetFace.md) | V | The face widget takes the face number and colour (the party list's sub_1402C1EA8). |
| <a id="10"></a>10 | [FaceNumber_Remap](../functions/FaceNumber_Remap.md) | V | A few numbers up to 205 are replaced; every other number passes. |
| <a id="11"></a>11 | [FaceTexture_FormatName](../functions/FaceTexture_FormatName.md) | V | The name: UI texture path row 4 formatted with %d face and colour; then GUIWidget_EnsureSlotGroup(name). |

## Behavior

- V: the classic-graphics portrait goes another way: PartyUnit_GetFaceRecord's +8 word is rebuilt from PartyUnit_BuildJobRecord's code as atlas cell ((code >> 2) + 224) << 6, wrapped with & 0x1FF from 512 up.

## Open questions

? whether GUIWidget_EnsureSlotGroup or the UI pack can serve a name the stock packs do not hold (a face number of 256 or more).
