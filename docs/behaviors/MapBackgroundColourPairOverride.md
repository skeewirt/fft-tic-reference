# MapBackgroundColourPairOverride

- **Kind:** observed behaviour
- **Scope:** engine (map block light command 50, Map variation element +0x38..+0x42)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapBlock_RunCommand](../functions/MapBlock_RunCommand.md), [SceneColourPair_WriteVertexColours](../functions/SceneColourPair_WriteVertexColours.md), [MapVariationStruct](../structs/MapVariationStruct.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A variation element can replace the two background colours that the map block's light command sets; the pair is then written into the colours of four vertices as a two-colour gradient.

## Behavior

- V: the light command of the map block is command 50 (0x32; the compare chain after command 44 sends 46..48 to the sub-command loop, 50 to the light block and 51 to another handler). It reads three light colours, three light vectors and the ambient colour (record +36..+38; fixed values for maps 26 and 127), then the background colours at record +39..+41 and +42..+44.
- V: the chosen variation element of the current map (index from the global work record +116, taken when below the element count) then overrides each of the six bytes with its int16 member background_color_1_red .. background_color_2_blue; a member above 255 keeps the command's byte.
- V: the result is the 8-byte pair qword_14114A4E8 (colour 1 in bytes 0..2, colour 2 in bytes 4..6), copied to qword_142FF9DA8, qword_142FF86A8 and qword_142FF8498; other code (sub_1402F52D8, ClutManager_Update) also writes the pair for fades.
- V: SceneColourPair_WriteVertexColours stores colour 1 into two and colour 2 into two further vertex colour entries of a render block, each value as byte * 128 / 255.
- I: the order red, green, blue of each triple follows the byte order of the pair and the stock values (a sky blue and a sand colour on one random-battle map), not a read of the vertex format.
- M: 111 stock elements hold -1 in all six members (keep the command's colours); the elements that override hold 0..255 and belong to the random-battle maps.

## Open questions

? the vertex format of the render block.
