# g_CurrentMapId

- **Kind:** global
- **Address:** `0x140784478`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `int`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

32-bit id of the map being loaded or in play, stored by the map load task before it calls Map_LoadBattleData; MapResource_Read indexes the per-map resource pointer tables with it; 0x77777777 means no map; the other readers compare it with stock map numbers

## Open questions

None recorded.
