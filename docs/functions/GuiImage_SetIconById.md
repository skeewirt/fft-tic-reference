# GuiImage_SetIconById

- **Address:** `0x1402A8F40`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `void GuiImage_SetIconById(GuiImage *img, int iconKey, void *parent, char keepFlag)`
- **Callers:** UI screen builders (`sub_140166E08`, `sub_140169068`, `sub_14016D72C`, `sub_14016E218`, `sub_140172B70` and others)
- **Callees:** Icon_FormatPath, `UIName_Key`, `sub_1403D87F4`, `sub_1403FB960`, `sub_1403F3DAC`, `sub_1403F3DFC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binds an icon image, chosen by its Icon table key, to a UI image object; used by many screens that show job, command or ability icons.

## Behavior

- V: a non-null parent replaces the image's stored parent node (+24); with no parent stored it skips the name step.
- V: otherwise it writes the image's name key (string at +56, through UIName_Key) into the parent node's name field (+232).
- V: if iconKey differs from the cached key at +128 it (re)creates the image node at +40 from the layer at +16 and the node name at +96.
- V: for iconKey > 0 it builds the path with Icon_FormatPath(iconKey, buf, 0, 256), i.e. the plain icon path, not the texture-part form, and binds it to the node.
- V: on success it sets the changed flag at +132, caches the key at +128, then copies the Icon row's dword at +12 (the sheet's `UnknownC`) into the parent node at +248.
- V: when keepFlag is 0 it clears the parent node's byte at +144.
- V: has more than a dozen callers in the UI layer.

## State touched

- Calls: [Icon_FormatPath](Icon_FormatPath.md), [UIName_Key](UIName_Key.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [BookShelf_Fill](BookShelf_Fill.md), [CreditRoll_AddPictureLine](CreditRoll_AddPictureLine.md), [GlossaryDetail_Fill](GlossaryDetail_Fill.md), [GuideWindow_ShowPage](GuideWindow_ShowPage.md), [ItemObtainedPanel_Fill](ItemObtainedPanel_Fill.md), [ZodiacStone_FillDetail](ZodiacStone_FillDetail.md), [ZodiacStone_FillTip](ZodiacStone_FillTip.md), [sub_14029BCD4](sub_14029BCD4.md)

## Notes

The Icon table is registry id 118.

## Open questions

What the Icon row dword at +12 controls on the node.
