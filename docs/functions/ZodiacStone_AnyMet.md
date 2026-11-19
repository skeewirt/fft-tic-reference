# ZodiacStone_AnyMet

- **Address:** `0x14016BC30`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool ZodiacStone_AnyMet(void)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetSetEntries, UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether any ZodiacStone row has its user_situation met.

## Behavior

- V: walks every set and every row of the ZodiacStone table (the last row of each set first) and returns 1 at the first row whose user_situation (+8) passes UserSituation_IsMet, else 0.

## State touched

- Calls: [NxdTable_GetSetEntries](NxdTable_GetSetEntries.md), [UserSituation_IsMet](UserSituation_IsMet.md)

## Open questions

None recorded.
