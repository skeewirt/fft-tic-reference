# Town_GetMapPosition

- **Address:** `0x14015CC00`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Town_GetMapPosition(int location, float *xy)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a location's map position.

## Behavior

- V: converts Town map_x (+8) and map_y (+0xC) to floats (cvtdq2ps).

## Open questions

None recorded.
