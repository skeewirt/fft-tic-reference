# CodePointerRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of UiLegacyLayoutScriptOps.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="handler"></a>`0x0` | handler | `pointer` | V | function that runs one layout script record and returns the next record; slots 3, 6, 7, 8 and 11 are empty; slots 4 and 5 share one handler |

## Referenced by

- Described by tables: [UiLegacyLayoutScriptOps](../tables/UiLegacyLayoutScriptOps.md)

## Open questions

None recorded.
