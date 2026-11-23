# Icon_FormatPath

- **Address:** `0x1400FC9A8`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `char Icon_FormatPath(unsigned int iconKey, char *out, char wantUiUri, int cap)`
- **Callers:** 23 UI functions (JobTreePanel_SetJobIcon, sub_1400FBF30, sub_1400FBFF8, ...)
- **Callees:** Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Formats 'ui/ffto/icon/<path>' (or the same path with a texture-parts URI prefix) from Icon row iconKey (table 118, cache qword_143CDA328).

## Behavior

- V: callers pass template rows: 11 = ability/textureparts/a_%03d_uitx (sub_1400FBFF8), 15 = job/textureparts/j_%03d_uitx (JobTreePanel_SetJobIcon), 16 = job_comm/textureparts/jc_%03d_uitx (sub_1400FBF30), 17 = attribute/at_%02d.

## State touched

- Calls: [Str_Format](Str_Format.md)

## Referenced by

- Called by: [CreditRoll_AddPictureLine](CreditRoll_AddPictureLine.md), [GuiImage_SetIconById](GuiImage_SetIconById.md), [IconBase_FormatPath](IconBase_FormatPath.md), [ItemIcon_FormatLargePath](ItemIcon_FormatLargePath.md), [ItemIcon_FormatSmallPath](ItemIcon_FormatSmallPath.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [WorldMapLocationPanel_Init](WorldMapLocationPanel_Init.md), [ZodiacStoneBoard_Setup](ZodiacStoneBoard_Setup.md)
- Reads file formats: [ItemIconPath](../formats/ItemIconPath.md)

## Notes

Also known as IconTable_FormatPath (earlier sheet name). The template is then filled with the icon / index value by the caller's Str_Format.

## Open questions

None recorded.
