# FrameSetPointer

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the UiFrameSets tables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="frame_set"></a>`0x0` | frame_set | `pointer` | V | pointer to a sprite frame set: an i32 piece count, two header dwords and the pieces (two dwords each) |

## Referenced by

- Described by tables: [FrameSetsDefault](../tables/FrameSetsDefault.md), [FrameSetsLanguage0](../tables/FrameSetsLanguage0.md), [FrameSetsLanguage2](../tables/FrameSetsLanguage2.md), [FrameSetsLanguage3](../tables/FrameSetsLanguage3.md)

## Open questions

None recorded.
