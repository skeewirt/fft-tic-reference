# NovelReader_ShowPage

- **Address:** `0x1401DFED0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void NovelReader_ShowPage(void *reader, int page)`
- **Callers:** not recorded
- **Callees:** Novel_GetPageText, sub_1401E2014, sub_1401E1AD0, sub_14018012C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows one page of the open book (vtable slot at 0x143D36238).

## Behavior

- V: the flags at +64 are masked with 0xFFFFFEC7 (the complement of 0x138, clearing those bits) and set with |= 8; +348 = 0, +344 = 1, +100 = page.
- V: the text comes from Novel_GetPageText(reader +88, page) through sub_1401E2014; then sub_1401E1AD0(+88, page).

## State touched

- Calls: [Novel_GetPageText](Novel_GetPageText.md)

## Referenced by

- Observed behaviours: [BookPageTextIsReadFromTheNovelTableOfPageTable](../behaviors/BookPageTextIsReadFromTheNovelTableOfPageTable.md)

## Open questions

None recorded.
