# EventSideYawTargets

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140672100`
- **Rows:** 4 rows of 2 bytes
- **Keyed by:** side bit 0..3 (blocked-side mask bit)
- **Read by:** [EventMoveTargets_Rewrite](../functions/EventMoveTargets_Rewrite.md)
- **Row layout:** [EventSideYaw](../structs/EventSideYaw.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The four facing yaw angles an event turn command may snap to. Verdict: engine-data.

## Behavior

- V: loop bound is the next table (word_140672108): 4 entries; values are the four yaws seen live in battle
- V: EventMoveTargets_Rewrite: walks the four entries, skips a side whose bit is set in the mask, picks the yaw with the shortest signed turn from the current yaw (wrap at 4096) and writes current + shortest turn as the angle target

## Notes

Our names. Tags: V layout, V meaning.

## Open questions

None recorded.
