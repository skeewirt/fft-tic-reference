# NovelReader_Open

- **Address:** `0x1401DFCD4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void NovelReader_Open(void *reader, ...)`
- **Callers:** not recorded
- **Callees:** sub_1401E2774

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the book reader on a book (vtable slot at 0x143D36220).

## Behavior

- V: stores a4 at +72, the book id at +96 and +80; reader +104 (word) = Book row +0x20 (page_table); bit 0 of +64 = a3.
- V: loads the sound bank 'sound/common/novel.sab' once into the audio object at +1232 and calls sub_1401E2774(+16, 2).

## Referenced by

- Observed behaviours: [BookPageTextIsReadFromTheNovelTableOfPageTable](../behaviors/BookPageTextIsReadFromTheNovelTableOfPageTable.md)

## Open questions

None recorded.
