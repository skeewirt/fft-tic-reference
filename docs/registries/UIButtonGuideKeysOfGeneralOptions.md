# UIButtonGuideKeysOfGeneralOptions

- **Kind:** registry
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The guide bar keys (`UIButtonGuide` rows, UI table 33) the settings screen uses, with the text id of each sub-row; 'right' marks sub-rows drawn on the right (byte +37 `Unknown25`).

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="rows"></a>21003 | `rows` | `0: 53 Back; 1: 3591 Change Setting; 2: 2554 Restore Defaults (right)` | V | Plain row. |
| <a id="rows"></a>21004 | `rows` | `21003 plus 3: 2555 Apply (right)` | V | Plain row, changes pending. |
| <a id="rows"></a>21005 | `rows` | `0: 53; 1: 3590 View Options; 2: 2554 (right)` | V | Value-list row. |
| <a id="rows"></a>21006 | `rows` | `53, 3590, 0, 0, 2554, 2555 (right), 0` | V | Value-list row, changes pending. |
| <a id="rows"></a>21007 | `rows` | `81 Close, 52 Confirm, 0` | V | Value list open. |
| <a id="rows"></a>21008 | `rows` | `3673 Cancel` | V | Cancel only. |
| <a id="rows"></a>21009 | `rows` | `53, 2617 Claim Bonus` | V | Bonus items. |
| <a id="rows"></a>21011..21013 | `rows` | `53, 2242 Play/Stop, 2243 Change Language / 2244 Revert Language` | V | Language rows. |
| <a id="rows"></a>21015 | `rows` | `53, 3590` | V | Rows 4 / 27. |
| <a id="rows"></a>21016 | `rows` | `53, 3591` | V | Row 5. |
| <a id="rows"></a>21017 | `rows` | `53, 3681 Assign Key, 0, 2554 (right), 3680 Unassign Key (right), 0` | V | Key bindings tab. |

## Behavior

- V: the sub-row text ids are rows of the general UI text table (labels: 52 Confirm, 53 Back, 81 Close).
- V: ConfigMenu_UpdateFooter picks the key: 21017 on the key bindings tab, 21007 with a value list open, 21015 for rows 4 / 27, 21016 for row 5, else 21005 / 21006 for a value-list row and 21003 / 21004 otherwise (the even keys when changes are pending).

## Referenced by

- Observed behaviours: [GuideBarLayout](../behaviors/GuideBarLayout.md)

## Open questions

None recorded.
