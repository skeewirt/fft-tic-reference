# GlossaryPagesAreMetRowsOfOneEntry

- **Kind:** observed behaviour
- **Scope:** engine (glossary)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [LoreDictionary_CurrentRow](../functions/LoreDictionary_CurrentRow.md), [LoreDictionary_PageCount](../functions/LoreDictionary_PageCount.md), [LoreDictionary_BuildList](../functions/LoreDictionary_BuildList.md), [LoreDictionary_CompareEntries](../functions/LoreDictionary_CompareEntries.md), [Glossary_OnSortInput](../functions/Glossary_OnSortInput.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A glossary entry is a first key; its rows (second key) are pages that appear as their user_situation is met, and a row flagged replaces_previous overwrites the page before it instead of being a page of its own.

## Behavior

- V: pages are counted and picked only among met rows with replaces_previous 0; a later met row with it set replaces the page until the next page row.
- M: no row with replaces_previous set is the first row of its entry.
- V: the list holds up to 150 entries, one for each first key with a met row; sort mode 1 (default) orders by sort_order, mode 2 by sort_order_2, mode 3 by family_name_first; 0 sorts last in modes 1 and 2.
- V: the sort command sets the tab's mode to 2 when the chosen row is row 0, else 3.
- V: the strings full_name, description, plain_name and family_name_first are stored relative to +0x34.
- V: no code reads +0x30 or +0x4C.

## Open questions

None recorded.
