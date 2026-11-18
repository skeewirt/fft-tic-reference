# LegacyMenuNode

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 88 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LegacyMenuNodesLanguage0 table and the tables that share its shape.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="node"></a>`0x0` | node | `bytes[88]` | I | menu node record: layout words at +0..+0x1B, message / screen code at +28 (written by the step table), flag at +32, remembered row at +80 |

## Referenced by

- Described by tables: [EventMenuNodesDefault](../tables/EventMenuNodesDefault.md), [EventMenuNodesLanguage0](../tables/EventMenuNodesLanguage0.md), [EventMenuNodesLanguage2](../tables/EventMenuNodesLanguage2.md), [EventMenuNodesLanguage3](../tables/EventMenuNodesLanguage3.md), [GridMenuNodesDefault](../tables/GridMenuNodesDefault.md), [GridMenuNodesLanguage0](../tables/GridMenuNodesLanguage0.md), [LegacyMenuNodesDefault](../tables/LegacyMenuNodesDefault.md), [LegacyMenuNodesLanguage0](../tables/LegacyMenuNodesLanguage0.md), [LegacyMenuNodesLanguage2](../tables/LegacyMenuNodesLanguage2.md), [LegacyMenuNodesLanguage3](../tables/LegacyMenuNodesLanguage3.md), [SceneMenuNodesADefault](../tables/SceneMenuNodesADefault.md), [SceneMenuNodesALanguage0](../tables/SceneMenuNodesALanguage0.md), [SceneMenuNodesBDefault](../tables/SceneMenuNodesBDefault.md), [SceneMenuNodesBLanguage0](../tables/SceneMenuNodesBLanguage0.md)

## Open questions

None recorded.
