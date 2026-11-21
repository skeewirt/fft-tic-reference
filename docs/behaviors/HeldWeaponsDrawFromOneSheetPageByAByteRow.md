# HeldWeaponsDrawFromOneSheetPageByAByteRow

- **Kind:** observed behaviour
- **Scope:** engine (battle sprites, the weapon a unit holds)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [EquipSprite_BuildPieces](../functions/EquipSprite_BuildPieces.md), [sub_140260CF0](../functions/sub_140260CF0.md), [HdLayer_ResolveQuadTexture](../functions/HdLayer_ResolveQuadTexture.md), [HdQuad_SheetRect](../functions/HdQuad_SheetRect.md), [HdLayer_BuildTextures](../functions/HdLayer_BuildTextures.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The weapon a unit holds is drawn from one sheet: g2d entry 161, 512 x 512 pixels at 4 bits a pixel in the HD renderer (the classic sheet's 256 x 256 drawn twice the size), in HD sheet group 2. An item picks its strip with byte +1 of its palette row; the texture row of every weapon piece is stored as one byte, so no strip lies below the sheet's last row.

## Behavior

- V: EquipSprite_BuildPieces writes the piece header +4 = (frame flags & 0x60) | 9 in mode 1 (| 8 in mode 2) and +6 = object +22 + ((sub-state + 2) << 6), the sub-state 0..2 of the object's three equipment states.
- V: in mode 1 each piece's texture row is the byte 8 * (strip + the frame piece's row bits); in mode 2 the strip is not added.
- V: sub_140260CF0 maps a piece of kind 9 to the HD draw id 10083 + HdSheetGroup_ClaimClutEntry(2, the piece's palette word) and sets dword_142E7FEB4 (g_HdWeaponSheetEntry) to 161; kind 11 uses group 3 and entry 160, kind 30 group 14 and entry 158; kind 8 has no HD branch.
- V: HdSheetGroup_ClaimClutEntry keeps each of a group's 16 slots' palette word at group + 2564 + 8 x slot and returns slot 0 without claiming when all 16 are taken.
- V: HdLayer_ResolveQuadTexture sends draw ids 10083..10098 to group 2 (0x142EB0910); HdQuad_SheetRect turns the quad's UVs into the rectangle (2 x the smallest u, 2 x the smallest v, the sizes rounded up to powers of two) that HdSheetGroup_FindOrAddPiece looks up (the call at 0x14041AFE8).
- V: HdLayer_BuildTextures reads a group's sheet entry into a buffer of 0x80000 bytes allocated once (512 wide, 4 bits a pixel: 2,048 rows) and keys a group texture by the palette colours and the rectangle.
- V (data): entry 161 of the shipped g2d.dat inflates to 131,072 bytes; the stock strips (byte +1 of the palette rows) are 0..28 in steps of 2 for knives, 8 and 10 for ninja blades, 0..6 and 14 for swords, 12 and 14 for knight's swords, 16 and 18 for katanas, 22 and 24 for rods, 26 and 28 for staves; most other categories use 0 to 6.
- I: a category's frames sit at their own places on the sheet and the strip moves them down, so one strip number names different art in different categories.

## Notes

Seen in a picture of the shipped entry: every region of the sheet holds art. The classic renderer (graphics level below 2.0) reads the classic sheet from the emulated video memory instead.

## Open questions

? what draws with kind 8 (mode 2, no strip); ? the art of entries 160 (kind 11) and 158 (kind 30) beyond chests, crystals and monster pieces seen in entry 160.
