# SaveData_InitHeaderStrings

- **Address:** `0x140245A88`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void *SaveData_InitHeaderStrings(void)`
- **Callers:** Game_MainLoop (two call sites), sub_14021A030, sub_140245B7C, sub_140245D44, sub_140331864; two data references
- **Callees:** memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the save-data header text slots (a title, a save-slot caption and a data description) in the language the game is running in, sets two size fields and points the slot-cache table pointer at the slot cache.

## Behavior

- V: starts with English strings for the three texts; when the language info object `g_LanguageInfo` exists and its language code at +8 is 0 the three texts are replaced by other string constants; when the object is missing the code is taken as 1.
- V: stores the address of `g_SaveSlotCache` in `tbl_SaveSlotCachePtr` and writes the same value 2008200 into two dwords (`dword_1408F9618`, `dword_1408F961C`).
- V: copies the three strings (including the terminator) into three buffers 0x80 bytes apart in the header block starting at 0x1408F9BF4, and zeroes `dword_142E7FADC`.
- I: the three buffers are the strings shown for the save entry by the platform save layer (rests on the strings' wording).

## Notes

Whole body read (242 bytes). The 0x80 spacing is the difference of the three destination addresses.

## Open questions

What the value 2008200 measures.
