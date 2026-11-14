# GUIFontSet_FontTypeForLanguage

- **Address:** `0x1403DCD50`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIFontSet_FontTypeForLanguage(UIFontSetRow *row)`
- **Callers:** GUITextNode_Layout, sub_1403DBA94
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Picks the UIFontType id of a font-set row for the current game language.

## Behavior

- V: language code = *(int*)(qword_143CD9B10 + 8). Codes 1, 2, 3 (English, French, German) and a missing language object return row byte +68 = FontTypeId2; code 4 (Simplified Chinese) returns +72 = FontTypeId6; 5 (Traditional Chinese) +73 = FontTypeId7; 6 (Korean) +74 = FontTypeId8; every other code (0 = Japanese) returns the dword at +0 = FontTypeId1.
- V: the language codes are the index into the exe's name table japanese(0) english(1) french(2) german(3) schinese(4) tchinese(5) (strings at 0x1406FA8B8).
- V (data): font set 60 (the hover name plate) = FontTypeId1 7 (BO-ShinMGo, Japanese), FontTypeId2 5 (Zilvertype Pro Bold); font sets 51 and 98 (level badge, chips) = type 6 (Jura SemiBold) in every column.

## State touched

- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [GUIFontRenderer_UploadPalette](GUIFontRenderer_UploadPalette.md), [GUITextNode_Layout](GUITextNode_Layout.md)

## Notes

The studio's label extractor reproduces this selection (English).

## Open questions

None recorded.
