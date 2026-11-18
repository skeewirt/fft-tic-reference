# RandomBattleModeSelectsTheLightingVariantOfAMapsTextures

- **Kind:** observed behaviour
- **Scope:** engine (map variation, map textures)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md), [MapTextures_NameOfFrame](../functions/MapTextures_NameOfFrame.md), [MapTextures_LoadSystemSlots](../functions/MapTextures_LoadSystemSlots.md), [MapTextures_LoadMapSlots](../functions/MapTextures_LoadMapSlots.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle started from a random encounter runs MapRow_SelectVariation in its 'random battle' branch, which always yields a kind code from 1 to 6, and the name builder then reads the second name array of each texture row at index kind - 1. Only the maps of the random-encounter set (71..90 except 73) carry names there (the lighting variants _ra to _rf); every other map has an empty second array, so such a map requests no map texture and no system texture in that mode and draws as a black void with the deployment tiles floating. The same map draws normally when the mode global reads 0 at load.

## Behavior

- V: MapRow_SelectVariation reads the 32-bit global at 0x141853C08 first. Not 1: it matches the map row's variation structs by scene variables and writes kind code 0, and the textures come from the first name array at the variation index. 1: kind code from scene variable 35 (v35) and 36 (v36): v35 = 0 or 5 and above: 4 if v36 is non-zero else 1; v35 = 1 or 2: 5 if v36 non-zero else 2; v35 = 3 or 4: 6 if v36 non-zero else 3; the variation index is the last struct whose field at +16 equals the kind code, else 0.
- V (seen live): the global read 0 on the world map and 1 once the battle of a random encounter was loading (title card, deployment); scene variables read 35 = 0, 36 = 1, 48 = 0, 39 = 0 and the name builder was called with kind 4 (index 3); another battle read kind 1 (index 0) and another kind 2 (index 1) for stock map 84, whose requested files were the _rb set (lut_chara_a_0_rb.tga, gt_0_map084_map_lighting_rb.tga).
- V (data): the keys of RefinedBgTexture rows whose second name array is not empty are exactly 71, 72, 74..90; the other 99 keys (maps 0..70, 73, 91..116) have empty second arrays. These are the maps 71..90 the random-encounter table names (byte 22 values 71, 72, 74..90).
- V (seen live, picture and requests): stock maps 10 and 20 (anim file, rows present, texture folders present) in that mode: the mesh loaded (result 0), the texture gate was open, the name builder ran with kind 4 or 1 and returned no name, and no texture file of the map was requested (no gt_ and no lut_chara file); the deployment view was a black void. Stock maps 72, 84 and 85 in that mode drew their terrain.
- V (seen live): with the global written to 0 before the map load task ran, stock map 10 requested bg/textures/010/lut_chara_a_0.tga and the rest of its first-array files and drew its stone-dungeon terrain; map 20 likewise (MapAnim_Load and MapAnim_ReadRows were entered and the anim file was requested). Map 72 with an anim file drew in mode 1 without any change, so an anim file is not what blanks a map.
- I: a battle started from a story event leaves the global at a value other than 1, which is why the story maps draw there; a story battle was not read for it (?). What the global means for the rest of the battle was not studied; only the picture at deployment was seen with it at 0.

## Notes

Scene variables 35 and 36 change from battle to battle (kind 1, 2 and 4 were all seen on the same world-map spot), so the lighting variant of a random battle is not fixed by the map.

## Open questions

None recorded.
