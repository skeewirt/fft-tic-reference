# ConfigMenu_UpdateFooter

- **Address:** `0x140192790`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ConfigMenu_UpdateFooter(UIAddonFFTOConfig *addon)`
- **Callers:** UIAddonFFTOConfig_OnEvent
- **Callees:** UIGuide_Set

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the guide bar key (UIButtonGuide row) for the current row and state.

## Behavior

- V: key 21017 on the key bindings tab, 21007 with a value list open, 21015 for rows 4 and 27, 21016 for row 5, else 21005 / 21006 for a value-list row and 21003 / 21004 otherwise; the even keys when changes are pending.
- V: ends with a jump to UIGuide_Set(_, key, -1).

## State touched

- Calls: [UIGuide_Set](UIGuide_Set.md)

## Referenced by

- Reads tables: [NxdDataConfigItem](../tables/NxdDataConfigItem.md)

## Notes

Registry: UIButtonGuideKeysOfGeneralOptions.

## Open questions

None recorded.
