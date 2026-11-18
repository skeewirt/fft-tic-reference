# ClassicJobDetailPage_Run

- **Address:** `0x140392DB8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int ClassicJobDetailPage_Run(void)`
- **Callers:** sub_14033D9E4
- **Callees:** ClassicUi_RunLayoutScript, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Legacy party menu job detail page: four pages of the chosen job with page switching.

## Behavior

- V: on the first frame installs 16 condition functions and builds the page data of the job in word_143C52190; cancel ends the page with state 2, confirm with state 1 and result -1.
- V: a page selector (0..3) changes with the direction input and rebuilds the page data; the layout script of the text language is run (0x1408FC760 / 0x1408FCD30 / 0x1408FCB40 / 0x1408FC950) followed by a fixed corner cell.

## State touched

- Calls: [ClassicUi_RunLayoutScript](ClassicUi_RunLayoutScript.md), [Input_TestAction](Input_TestAction.md)

## Referenced by

- Reads tables: [LegacyJobDetailLayoutLang0](../tables/LegacyJobDetailLayoutLang0.md), [LegacyJobDetailLayoutLang1](../tables/LegacyJobDetailLayoutLang1.md), [LegacyJobDetailLayoutLang2](../tables/LegacyJobDetailLayoutLang2.md), [LegacyJobDetailLayoutLang3](../tables/LegacyJobDetailLayoutLang3.md)

## Open questions

?: what each of the four pages shows.
