# GuideList_BuildCategory

- **Address:** `0x1400DAB10`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideList_BuildCategory(int category, int *out)`
- **Callers:** sub_14017D144 (from sub_14017BA48)
- **Callees:** Guide_IsUnlocked, sub_1400DBB5C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the guide list of one tutorial tab.

## Behavior

- V: walks Guide rows by index from 1; skips keys of 3001 and above; keeps rows with category (+0xC) below 7 and category - 1 equal to the tab that Guide_IsUnlocked accepts; stores (id word, 0) into a3 (a count and up to 128 dwords) and sorts them with sub_1400DBB5C.

## State touched

- Calls: [Guide_IsUnlocked](Guide_IsUnlocked.md)

## Referenced by

- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
