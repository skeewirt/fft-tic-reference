# ListPageRangeStart

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LegacyListPageRangesLang0 table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="first_id"></a>`0x0` | first_id | `int16` | V | first message / entry id of the category; a category ends where the next one starts (run of ids start .. next - 1) |

## Referenced by

- Described by tables: [LegacyListPageRangesLang0](../tables/LegacyListPageRangesLang0.md), [LegacyListPageRangesLang1](../tables/LegacyListPageRangesLang1.md), [LegacyListPageRangesLang2](../tables/LegacyListPageRangesLang2.md)

## Open questions

None recorded.
