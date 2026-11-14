# Skillset_BuildTabAbilityList

- **Address:** `0x14028A370`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `uint16 *Skillset_BuildTabAbilityList(uint16 skillset, int tab, uint8 unitFlags)`
- **Callers:** Job_BuildTabAbilityList, sub_14028A770
- **Callees:** Skillset_BuildAbilityList

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The 24 abilities of a skillset with every entry outside the tab's id window cleared.

## Behavior

- V: Skillset_BuildAbilityList(skillset, 47 when unitFlags bit 6, else 31) (a shared static buffer).
- V: tab 0 keeps ids 1..421 (actions), 1 keeps 422..453 (reactions), 2 keeps 454..485 (supports), 3 keeps 486..509 (movement), any other tab 1..509; the others become 0. Returns the buffer.

## State touched

- Calls: [Skillset_BuildAbilityList](Skillset_BuildAbilityList.md)

## Referenced by

- Called by: [JobScreen_BuildAbilityTabList](JobScreen_BuildAbilityTabList.md), [Job_BuildTabAbilityList](Job_BuildTabAbilityList.md)

## Notes

One of three copies of the tab rule (JobAbilityList_Build, this, sub_140392620). This loop drops an id above 421 from the tab (V native test).

## Open questions

None recorded.
