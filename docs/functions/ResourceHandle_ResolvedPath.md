# ResourceHandle_ResolvedPath

- **Address:** `0x1400962FC`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `const char *ResourceHandle_ResolvedPath(ResourceHandle *h)`
- **Callers:** ResourceHandle_FinishLoad, sub_14009494C, sub_140094D4C and two others
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The path the reader resolved (+40, a string object whose text is at +8, heap pointer when its capacity +32 is 16 or more), else the requested path (+24), else an empty string.

## Behavior

- V: as the purpose says.

## Referenced by

- Called by: [ResourceHandle_FinishLoad](ResourceHandle_FinishLoad.md)

## Notes

None recorded.

## Open questions

? the exact form of the resolved name of a localised nxd file (I: it carries the language token, FinishLoad looks for '.en.').
