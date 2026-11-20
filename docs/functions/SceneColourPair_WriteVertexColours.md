# SceneColourPair_WriteVertexColours

- **Address:** `0x14024A6E8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 SceneColourPair_WriteVertexColours(void)`
- **Callers:** sub_140210AF0
- **Callees:** sub_14027483C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the scene's two-colour pair (qword_14114A4E8) into the colour entries of four vertices of a render block, a two-colour vertical gradient.

## Behavior

- V: first links three render blocks of the object at qword_140DE2BC8 (at +1769608, +1769472 and +1769576) into the list at +6128 of the object at +1769640 and tags each with word_14114A4E4.
- V: writes the pair to four consecutive vertex colour entries of the block at qword_140DE2BC8 + 1769484: bytes 0..2 of the pair (colour 1) into the entries at +1769484 and +1769492, bytes 4..6 (colour 2) into the entries at +1769500 and +1769508, each value as (byte * 128) / 255.
- V: then calls sub_14027483C with the render block and the light tables.
- I: that the two colours are the top and bottom of the background gradient rests on the colour 1 / colour 2 order of the four entries; the vertex layout was not read.

## Referenced by

- Observed behaviours: [MapBackgroundColourPairOverride](../behaviors/MapBackgroundColourPairOverride.md)

## Notes

The pair is set by MapBlock_RunCommand's light block (with the Map variation element's background_color members overriding it) and moved by sub_1402F52D8 and ClutManager_Update (fades).

## Open questions

? what the other writes of the function (the long tail after the vertex colours) do.
