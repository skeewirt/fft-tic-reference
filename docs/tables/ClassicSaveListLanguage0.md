# ClassicSaveListLanguage0

- **Kind:** table
- **Area:** [Save data](../areas/save-data.md)
- **Storage:** Executable (initialised data, written at run time)
- **Address:** `0x1407DC6F0`
- **Rows:** 1 rows of 176 bytes
- **Keyed by:** text language 0
- **Row layout:** [ClassicSaveListLanguage0Record](../structs/ClassicSaveListLanguage0Record.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Template and cursor of the classic save list, language 0 variant. Verdict: designer-data.

## Behavior

- V: 0xA8 to word_1407DC798; the twin 0x1407DC7A0 has its cursor at 0x1407DC848
- V: sub_14021A030 (classic save / load menu): chooses this or 0x1407DC7A0 by language

## Notes

Our names. Tags: V reader, ? fields.

## Open questions

- ?: template field meanings
