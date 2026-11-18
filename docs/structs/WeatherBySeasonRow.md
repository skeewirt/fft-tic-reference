# WeatherBySeasonRow

- **Kind:** structure
- **Area:** [Math](../areas/math.md)
- **Size:** 56 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The whole WeatherBySeason object.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="season_rows"></a>`0x0` | season_rows | `bytes[5]` | V | adjustment row of each calendar span (3, 0, 2, 1, 3) |
| <a id="adjustments"></a>`0x8` | adjustments | `int8[40]` | V | four rows of ten level adjustments |
| <a id="start_month"></a>`0x30` | start_month | `uint8[4]` | V | boundary months |
| <a id="start_day"></a>`0x34` | start_day | `uint8[4]` | V | boundary days |

## Referenced by

- Described by tables: [WeatherBySeason](../tables/WeatherBySeason.md)

## Open questions

None recorded.
