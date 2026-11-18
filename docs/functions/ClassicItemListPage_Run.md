# ClassicItemListPage_Run

- **Address:** `0x140393E70`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int ClassicItemListPage_Run(void)`
- **Callers:** sub_140393330
- **Callees:** Item_IsInCategory, VramPage_CopyRect, sub_14033E224, sub_14033E270, sub_14033E2C0, sub_14033E30C, sub_140394940, sub_140394C14, sub_14039AD30

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Legacy party menu item list page: draws the list body and its header.

## Behavior

- V: picks the page script of the text language (0x1408FD0B0 language 0, 0x1408FD860 language 3, 0x1408FD5D0 language 2, 0x1408FD340 otherwise) and a second chunk of the same block (0x1408FD1B0, 0x1408FD960, 0x1408FD6D0, 0x1408FD440 in the same order); one of two cell code grids (0x1408FD9F0 or 0x1408FEC70) is used by a page flag.
- V: starts the scene tasks of the neighbouring panels through the wrappers sub_14033E270, sub_14033E2C0 and sub_14033E224 and sets up the cursor.

## State touched

- Calls: [Item_IsInCategory](Item_IsInCategory.md), [VramPage_CopyRect](VramPage_CopyRect.md)

## Referenced by

- Reads tables: [LegacyItemListBodyGridA](../tables/LegacyItemListBodyGridA.md), [LegacyItemListBodyGridB](../tables/LegacyItemListBodyGridB.md), [LegacyItemListLayoutLang0](../tables/LegacyItemListLayoutLang0.md), [LegacyItemListLayoutLang1](../tables/LegacyItemListLayoutLang1.md), [LegacyItemListLayoutLang2](../tables/LegacyItemListLayoutLang2.md), [LegacyItemListLayoutLang3](../tables/LegacyItemListLayoutLang3.md)

## Open questions

None recorded.
