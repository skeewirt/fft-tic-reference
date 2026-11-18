# TextLanguage

- **Kind:** observed behaviour
- **Scope:** the text language: where it comes from, where it is read, how the text files are chosen
- **Area:** [Data access](../areas/data.md)
- **Affects:** [ResourceHandle_FinishLoad](../functions/ResourceHandle_FinishLoad.md), [EventEndSlate_ShowTask](../functions/EventEndSlate_ShowTask.md), [sub_1401E7EF8](../functions/sub_1401E7EF8.md), [g_LanguageInfo](../globals/g_LanguageInfo.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the game picks and applies its text language.

## Behavior

- V: the current text language is the u32 at `g_LanguageInfo` (0x143CD9B10) + 8 (registry TextLanguageCodes); it is read in `ResourceHandle_FinishLoad` and `EventEndSlate_ShowTask`.
- V: the first value at start: `sub_14002851C` takes the Windows user locale, then Steam's `GetCurrentGameLanguage` (japanese, english, french, german, schinese, tchinese, koreana) when Steam answers.
- V: after `settings.sav` loads, `sub_1401E7EF8` sets +8 from `g_ConfigData[21] & 0x1F` (the saved text language; the voice language is the next byte). Bit 7 of that byte is not decoded (?).
- V: the Settings option table `ConfigItemTextLanguage` has 7 rows; a chosen code is validated by `sub_14002BCE0` (case 7 of `sub_140189D54`).
- V: a localized resource key carries the language in a nibble (`+8 & 0xF`); the text nxd files come from the packs `data/enhanced/0004.<lang>.pac`; handles flagged localized (flag 8) are walked when the language changes.
- V (seen in play 2026-11-13): a change of Text Language (Enhanced) in General Options reloads the text nxd tables at once, without a restart (the menus redraw in the new language; a shop list showed the new language's item names).
- V (seen in play): the text language is set only in General Options on the mode select screen (Language tab: Text Language (Enhanced), Text Language (Classic), Voice Language); the in-game Settings has no language option.
- V: `root.nxl` lists each nxd table once, so every language's file of one table shares one table id.
- V (offline, every file decoded): the 53 text tables have the same columns, keys, row size and table id in all seven languages (`<name>.<lang>.nxd` decodes with the English layout).

## Referenced by

- Observed behaviours: [NxdTableRebinding](NxdTableRebinding.md)

## Open questions

None recorded.
