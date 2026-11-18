# g_BattleModeFlag

- **Kind:** global
- **Address:** `0x141853C08`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `int`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

32-bit mode global the main loop sets around battles and the scene start; 1 while a random-encounter battle loads (seen live: 0 on the world map, 1 at the title card and deployment); MapRow_SelectVariation takes its random-battle branch (kind code 1..6 from scene variables 35 and 36) only when it reads 1; other readers compare it with 4 (battle running?) and the values were not studied

## Open questions

None recorded.
