# RandomEncounters

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B69D0`
- **Rows:** 57 rows of 24 bytes
- **Keyed by:** battleground location id 24..42 (3 rows each), row chosen by the road the party arrived on
- **Read by:** [WorldEncounter_Roll](../functions/WorldEncounter_Roll.md)
- **Row layout:** [RandomEncounterRow](../structs/RandomEncounterRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Random encounters: per battleground and arrival road, the chance and formations by story progress. Verdict: designer-data.

## Behavior

- V: location - 24 <= 0x12 guard (19 locations) x 72 bytes = 0x558, next symbol at +0x560
- V: sub_140248BE4: for the location and arrival road, picks the tier from the story variable, rolls the chance (an option forces always / never), picks one allowed formation at random

## Notes

Our names. Tags: V layout, I names.

## Open questions

- ?: meaning of +22
- ?: formation id to battle setup mapping
- ?: which option value 1 / 2 forces encounters on / off
