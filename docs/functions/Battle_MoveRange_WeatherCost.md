# Battle_MoveRange_WeatherCost

- **Address:** `0x14027AD6C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `uint8 Battle_MoveRange_WeatherCost(void)`
- **Callers:** Battle_MoveRangeSetup, sub_14027DDB8
- **Callees:** SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The movement cost of the weather-dependent terrains: 1, 2 or 3 from event variable 35 and two bits of dword_140D3A830.

## Behavior

- V: v = SceneVar_Read(35); returns 1 when dword_140D3A830 bit 1 is set or v is below 2.
- V: adds 3 to v when dword_140D3A830 bit 0 is set; then returns 1 for v below 3 or v = 5, 2 for v = 3 or 6, else 3.
- I: variable 35 is the weather (SceneVar_Read's own code packs variables 35 and 36 into variable 34); the names of the values were not read.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Called by: [Battle_MoveRangeSetup](Battle_MoveRangeSetup.md)

## Notes

Battle_MoveRangeSetup uses the result for every terrain whose entry in the cost set is 0 (terrains 9, 10, 11, 26 and 36 in the walking set), unless unit byte +0x9D bit 0x02 forces 1.

## Open questions

? What the two bits of dword_140D3A830 are.
