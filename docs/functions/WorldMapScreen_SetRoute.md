# WorldMapScreen_SetRoute

- **Address:** `0x140157D74`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapScreen_SetRoute(void *screen, int route, int flag)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Records the route being opened on the world-map screen.

## Behavior

- V: screen +3284 = route, +3296 = flag, +3288 = Route town (+8) when the flag is set, else town_2 (+0xC).

## Open questions

None recorded.
