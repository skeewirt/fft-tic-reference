# SceneWindowColourRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of BattleSceneWindowColours.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flag"></a>`0x0` | flag | `uint32` | I | 0 or 1 |
| <a id="corners"></a>`0x4` | corners | `uint8[16]` | V | four colours (red, green, blue, 0): the four corners of the window gradient |

## Referenced by

- Described by tables: [BattleSceneWindowColours](../tables/BattleSceneWindowColours.md)

## Open questions

None recorded.
