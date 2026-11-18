# MapMeshAndAnimFilesCarryTheirOwnMapId

- **Kind:** observed behaviour
- **Scope:** engine (map mesh and anim files)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [MapMesh_Load](../functions/MapMesh_Load.md), [MapAnim_Load](../functions/MapAnim_Load.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The mesh file and the anim file of a battle map hold the map id in their header, and the loaders refuse a file whose id is not the one requested. The renderer builds nothing for a refused mesh.

## Behavior

- V: the mesh header is 48 bytes: a format tag, the map id at +8 and the layer count at +12; the loader compares the tag and the id and frees the buffer and returns 1 on a mismatch.
- V: the anim header is 32 bytes with a format tag and the map id at +8; the loader checks them the same way.
- V (data): the meshes of maps 1, 5 and 100 and the anims of maps 1, 2 and 100, unpacked from the game's own pack, each hold their own map id at +8; the mesh layer count is 1; the three anim files have the same size.
- V: a mesh larger than 7,534,452 bytes is refused; ids 15 and 33 never load a mesh.

## Notes

A file placed under another map id's name therefore loads only if its header id is changed to match.

## Open questions

None recorded.
