# JournalList_Build

- **Address:** `0x140169D28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalList_Build(void *list)`
- **Callers:** JournalScreen
- **Callees:** UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the Chronicle Events list from the Journal rows that are met.

## Behavior

- V: walks the rows by index; for each met user_situation (+0xC) pushes {key, row +8, kind, save byte at save block +6922 + i, byte at +7050 + i} (kind: 1 when movie (+0x24) is set, 2 when event_id (+0x18) is 0, else 0).
- V: the list is insertion-sorted by entry +4 (= Journal sort_order, +8).

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md)

## Open questions

None recorded.
