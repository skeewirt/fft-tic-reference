# ScreenTaskSetRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the ScreenTaskSets table: up to four task slots started together.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="handler"></a>`0x0` | handler | `pointer[4]` | V | entry function of each of the four tasks; all bits set = this slot is not used by the set |
| <a id="slot"></a>`0x20` | slot | `uint32[4]` | V | task slot number of each task (10, 11, 12, 13) |
| <a id="expected_kind"></a>`0x30` | expected_kind | `uint32[4]` | V | tag the slot must carry while the set is on screen (0x10, 0x11, 0x14 seen); all bits set = none; a different tag makes the runner stop the slot and start the handler again |

## Referenced by

- Described by tables: [ScreenTaskSets](../tables/ScreenTaskSets.md)

## Open questions

None recorded.
