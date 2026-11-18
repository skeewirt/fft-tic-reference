# UiNames_InstallCoreNames

- **Address:** `0x1403D5934`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UiNames_InstallCoreNames(__int64 ui)`
- **Callers:** sub_1403D6098 (and a data reference)
- **Callees:** sub_1403D321C (registry ready test), UIName_Intern, UIName_ReleaseKey, GUIFontTable_Load, sub_1403D9038, sub_1403DB894, GUIFontSlotGroup_SetImageByName

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Registers the 43 core UI event and part names in the UI name table and loads the font data of the current text language.

## Behavior

- V: returns 0 at once when the data registry is missing or not ready, or when the renderer's ready flag (+44415) is clear or its busy flag (+44416) is set.
- V: copies the text language index (language record +8, 1 when there is no record) into the UI environment object (+216).
- V: walks the 43 name pointers of exe.ui.core_name_keys; for each, resets a 16-byte slot of the UI name table (from +4584), interns the name with UIName_Intern, and releases the key that slot held before.
- V: then loads the GUI font table, runs the font slot setup for the language and sets the bezier pattern image on the font slot group of the caller's object (+208).
- V: returns 1 when it ran to the end.

## State touched

- Calls: [UIName_Intern](UIName_Intern.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUIFontTable_Load](GUIFontTable_Load.md), [GUIFontSlotGroup_SetImageByName](GUIFontSlotGroup_SetImageByName.md)

## Referenced by

- Reads tables: [UiCoreNameKeys](../tables/UiCoreNameKeys.md)

## Notes

Name is ours. The 43-slot loop bound is the end of the string table (344 bytes).

## Open questions

?: what the two callees sub_1403D9038 and sub_1403DB894 build.
