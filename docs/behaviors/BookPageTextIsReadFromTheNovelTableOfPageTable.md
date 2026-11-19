# BookPageTextIsReadFromTheNovelTableOfPageTable

- **Kind:** observed behaviour
- **Scope:** engine (book reader)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [Novel_GetPageText](../functions/Novel_GetPageText.md), [NovelReader_Open](../functions/NovelReader_Open.md), [NovelReader_ShowPage](../functions/NovelReader_ShowPage.md), [NovelReader_SendReadThrough](../functions/NovelReader_SendReadThrough.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A book's pages are the rows of one of five Novel tables, chosen by the Book page_table value; the page number is the row key and the text is the row's string.

## Behavior

- V: page_table 225, 227, 229, 231, 233 select Novel00..Novel04 (tables 164..168); any other value gives empty pages.
- V: the reader sends a NovelReadThroughNotification with the book id when the book is read to the end.
- V: the shelf lists a book only while the event variable of Book event_var is non-zero, in the order of sort_order.

## Open questions

None recorded.
