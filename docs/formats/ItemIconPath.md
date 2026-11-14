# ItemIconPath

- **Kind:** file format
- **Extension:** `.utexpt with .tex`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Read by:** [ItemIcon_FormatLargePath](../functions/ItemIcon_FormatLargePath.md), [ItemIcon_FormatSmallPath](../functions/ItemIcon_FormatSmallPath.md), [Icon_FormatPath](../functions/Icon_FormatPath.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The two per-item picture paths: a detail picture (Icon table row 12) and a list picture (row 13), both formatted from the item id and both texture-parts URIs. The number is the item id with %03d as a minimum width; nothing masks it. Each path names a part file that in turn names its texture.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="detail"></a>row 12 | detail | `char[]` | V | equip_item/textureparts/ei_%03d_uitx, prefixed with the UITextureParts scheme and ui/ffto/icon/ by Icon_FormatPath. Used by the equipment detail panel and the detail views. |
| <a id="list"></a>row 13 | list | `char[]` | V | equip_item_s/textureparts/ei_s_%03d_uitx, with the same prefix. Used by list cells (shop rows, item lists). |
| <a id="id_field"></a>%03d | id_field | `decimal` | V | The item id, minimum width 3: 1 gives ei_001, 1000 gives ei_1000, 65535 gives ei_65535. The id is a 32-bit argument with no mask or truncation in the formatters; the caller's buffer cap is the only limit. |
| <a id="scheme"></a>prefix | scheme | `char[]` | V | The UITextureParts scheme, followed by ui/ffto/icon/; this is the texture-parts mode of Icon_FormatPath, selected by both item formatters. |
| <a id="buffer"></a>cap | buffer | `int` | V | 0x104 (260) inside both formatters; the six callers pass 0x100 or 0x104. Str_Format truncates at the cap and no caller checks the result. |
| <a id="pair"></a>files | pair | `file` | V | Each path names a .utexpt part file; the part file carries the path of the .tex texture. The retail packs hold 261 detail textures (100 x 100, BC7) and 261 list textures (48 x 48, BC7), ids 0..260. |

## Behavior

- V: id <= 0 formats as 0 (the formatters replace a non-positive id with 0).
- V: the id is not the record's icon field: the record's two icon bytes feed the classic tile path (ItemIcon_Set), while these paths are named by the id alone.
- V: a missing file is not detected at bind time: ItemCell_BindIconAndName binds the path when the Item-en name row exists and the id is not negative, without checking that the part file or the texture exists.
- V: the UI looks a texture part up by path inside the mounted packs (lower-cased, separators normalised).

## Notes

V: six call sites in six functions: two large (sub_140109134, EquipDetail_Refresh) and four small (sub_140142014, sub_14014D57C, sub_140153CA0, ItemCell_SetItem). The text-id site inside sub_140153CA0 feeds the 11-bit item id of a 0x3800 cell, so it inherits the text-id limit.

## Open questions

? what the screen shows when the part file exists but the texture does not (the size fallback is 1 x 1; the pixels were not observed).
