# EventLookSet_Select

- **Address:** `0x1402459E0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventLookSet_Select(unsigned int setId)`
- **Callers:** EventScript_Run
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Makes one of the eight generic look sets the active pool for an event's placeholder actors.

## Behavior

- V: copies 32 bytes (eight sprite sheet ids) of the set from the generic look set table (0x1407141E0) into the active pool (0x1437A1348).
- V: an id above 7 fills the pool from a default constant instead.

## Referenced by

- Reads tables: [EventGenericLookSets](../tables/EventGenericLookSets.md)

## Open questions

None recorded.
