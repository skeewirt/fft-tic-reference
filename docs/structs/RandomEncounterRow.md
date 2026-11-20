# RandomEncounterRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the RandomEncounters table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="arrival_road"></a>`0x0` | arrival_road | `uint8` | V | road id the party came along (exe.worldmap.roads); 0 = unused row |
| <a id="battle_low"></a>`0x1` | battle_low | `uint8` | V | battle number low byte; the battle started is 0x200 + this |
| <a id="tier[4]"></a>`0x2` | tier[4] | `bytes[12]` | V | four story tiers of 3 bytes: {highest value of the story variable for this tier, encounter chance %, bit mask of the allowed formations 0..7} |
| <a id="formation[8]"></a>`0xE` | formation[8] | `pointer` | V | formation / entry ids; formation k is the byte at +21 - k |
| <a id="map"></a>`0x16` | map | `uint8` | V | battle map id of the random battle, kept with the pick (dword_140D49464) and written to scene variable 51 when the world-map screen ends (see RandomEncounterRowByte22IsTheBattleMapId) |
| <a id="story_var"></a>`0x17` | story_var | `uint8` | V | event variable that selects the tier (111 in every stock row) |

## Referenced by

- Described by tables: [RandomEncounters](../tables/RandomEncounters.md)

## Open questions

None recorded.
