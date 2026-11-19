# Book_ShowGuide

- **Address:** `0x14016620C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Book_ShowGuide(int id)`
- **Callers:** not recorded
- **Callees:** UIGuide_Show

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the guide that explains the reading shelf.

## Behavior

- V: an id out of range calls UIGuide_Show(.., 0, 0); otherwise guide 15005 when the word at 0x1411A756E + 56 * id is above 0 (id below 5), else guide 15004.
- I: the per-book word (5 books, 56-byte stride) is a progress or bookmark value; sub_1401662B0 reads it too.

## State touched

- Calls: [UIGuide_Show](UIGuide_Show.md)
- Reads: [g_BookProgressWords](../globals/g_BookProgressWords.md)

## Open questions

? what the word at 0x1411A756E + 56 * id holds.
