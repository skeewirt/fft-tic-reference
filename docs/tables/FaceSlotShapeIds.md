# FaceSlotShapeIds

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x140714D50`
- **Rows:** 82 rows of 4 bytes
- **Keyed by:** face slot number
- **Read by:** [SpriteId_ToShape](../functions/SpriteId_ToShape.md)
- **Row layout:** [FaceShapeId](../structs/FaceShapeId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite shape number for each dialogue face slot below 0x52. Verdict: engine-data.

## Behavior

- V: three dialogue builders read table[slot] for slots up to 0x51 in face display mode 1 and use SpriteId_ToShape above that
- V: starts like g_SpriteIdToShape (0x1407146D0) but differs from entry 16

## Notes

Our names. Tags: V.

## Open questions

None recorded.
