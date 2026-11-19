# Novel_GetPageText

- **Address:** `0x1401E1C10`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `const char *Novel_GetPageText(void *book, int page)`
- **Callers:** NovelReader_ShowPage, sub_1401E198C (page-text cache keyed by the page id: a hash lookup, built and cached on a miss)
- **Callees:** NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the text of a book page from the Novel table the book names.

## Behavior

- V: switches on the word at argument +16 (reader +104 = Book page_table): 225 = Novel00 (table 164), 227 = Novel01 (165), 229 = Novel02 (166), 231 = Novel03 (167), 233 = Novel04 (168); each table is read through its cache global; the row is NxdTable_GetRowById(page) and the text is the string at row +4.
- V: an empty string when the case or the row is missing, so any other page_table value gives empty pages.
- V: the only reader of the five Novel tables; row +0 is never read.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md)

## Referenced by

- Called by: [NovelReader_ShowPage](NovelReader_ShowPage.md)
- Observed behaviours: [BookPageTextIsReadFromTheNovelTableOfPageTable](../behaviors/BookPageTextIsReadFromTheNovelTableOfPageTable.md)

## Open questions

None recorded.
