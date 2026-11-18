# ClassicListPage_BuildRangeList

- **Address:** `0x14037B8FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char ClassicListPage_BuildRangeList(void)`
- **Callers:** sub_14037BA34, sub_14037C2EC, sub_14037C6C4 and two more list pages
- **Callees:** sub_140327854, sub_1403293E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the list of entry ids of the current category of a legacy list page and hands it to the list drawer.

## Behavior

- V: picks the range table of the text language (0x1408FBCD0 language 0, 0x1408FBEB0 language 3, 0x1408FBFA0 language 2, 0x1408FBDC0 otherwise) and a table of three alternative window templates by the display mode.
- V: the category's ids are start .. next start - 1 of the range table; they are stored as a list terminated by -1 and drawn.

## Referenced by

- Reads tables: [LegacyListPageRangesLang0](../tables/LegacyListPageRangesLang0.md), [LegacyListPageRangesLang1](../tables/LegacyListPageRangesLang1.md), [LegacyListPageRangesLang2](../tables/LegacyListPageRangesLang2.md)

## Open questions

None recorded.
