# WorldWeather_Update

- **Address:** `0x140304330`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `unsigned long long WorldWeather_Update(void)`
- **Callers:** the calendar update code (sub_14030476C)
- **Callees:** SceneVar_Read, SceneVar_Write

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Updates the world map weather level when the calendar advances.

## Behavior

- I: reads scene variables 46 (month) and 47 (day) and 35 (the current weather level).
- V: finds the calendar span by comparing (month, day) with the four boundary pairs of exe.world.weather_by_season, maps the span to a row of ten adjustments and draws one with the random generator.
- V: new level = level + adjustment, clamped to 0..4; stored in scene variable 35 unless a flag word says the map is busy, then a one in three random value is stored in scene variable 36.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md)

## Referenced by

- Reads tables: [WeatherBySeason](../tables/WeatherBySeason.md)

## Notes

Name is ours; the variable meanings (weather) are inferred.

## Open questions

?: what scene variables 35 and 36 do on screen.
