# LoreDictionary_PageCount

- **Address:** `0x1401E4594`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int LoreDictionary_PageCount(int key)`
- **Callers:** not recorded
- **Callees:** UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counts the pages of a glossary entry.

## Behavior

- V: the number of rows of the entry whose user_situation is non-zero and met and whose replaces_previous (+0x4E) is 0.

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md)

## Referenced by

- Observed behaviours: [GlossaryPagesAreMetRowsOfOneEntry](../behaviors/GlossaryPagesAreMetRowsOfOneEntry.md)

## Open questions

None recorded.
