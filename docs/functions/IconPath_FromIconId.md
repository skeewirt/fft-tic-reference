# IconPath_FromIconId

- **Address:** `0x1403DB140`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void IconPath_FromIconId(char *out, int iconId)`
- **Callers:** sub_1403DB6B8
- **Callees:** UITable_GetRow, sub_1403DBBBC, Str_Format, UITexturePath_Select4k

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the file path of an icon from its Icon id, using the IconGroup table to decide on the 4k texture variant.

## Behavior

- V: walks the IconGroup rows from index 1 and keeps the last row whose first_icon (+4) is not above the icon id; a first_icon of 0 ends the list.
- V: takes the Icon row's path (+8) and formats 'ui/ffto/icon/<path>'; when the kept group's select_4k byte (+9) is non-zero the path goes through UITexturePath_Select4k ('_2k_' becomes '_4k_').
- V: an empty path gives an empty string.
- M: 54 of 75 IconGroup rows have select_4k set; no stock Icon path contains '_2k_', so the rewrite changes nothing in the shipped data.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md), [Str_Format](Str_Format.md), [UITexturePath_Select4k](UITexturePath_Select4k.md)

## Referenced by

- Observed behaviours: [IconGroup4kPaths](../behaviors/IconGroup4kPaths.md)

## Notes

Name is ours. Row +0 of IconGroup and Icon, and IconGroup +8 / +0xA / +0xB, are never read.

## Open questions

None recorded.
