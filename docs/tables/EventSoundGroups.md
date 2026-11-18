# EventSoundGroups

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140681D00`
- **Rows:** 56 rows of 4 bytes
- **Keyed by:** sound group number - 1
- **Read by:** [EventSoundGroup_Play](../functions/EventSoundGroup_Play.md)
- **Row layout:** [EventSoundGroup](../structs/EventSoundGroup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Four sound effect numbers per group, played together by one event command. Verdict: designer-data.

## Behavior

- V: EventSoundGroup_Play: row (n - 1) x 4, four bytes, each plus 0xE10000 then minus one given to the sound player
- I: 56 rows up to the event command handler table

## Notes

Our names. Tags: V reader, I count.

## Open questions

None recorded.
