# SpriteAnimScriptsRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the SpriteAnimScripts table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="script"></a>`0x0` | script | `uint64` | V | pointer to a frame list in .rdata (0x140699C88 .. 0x140699E50): a frame count, then per frame a cell group index (low half-word) and hold ticks (high half-word) |

## Referenced by

- Described by tables: [SpriteAnimScripts](../tables/SpriteAnimScripts.md)

## Open questions

None recorded.
