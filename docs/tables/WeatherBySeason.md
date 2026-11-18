# WeatherBySeason

- **Kind:** table
- **Area:** [Math](../areas/math.md)
- **Storage:** Executable
- **Address:** `0x14071E748`
- **Rows:** 56 bytes: 4 + 4 + 4 x 10 + 4 + 4
- **Keyed by:** season span 0..4; adjustment row 0..3
- **Read by:** [WorldWeather_Update](../functions/WorldWeather_Update.md)
- **Row layout:** [WeatherBySeasonRow](../structs/WeatherBySeasonRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Four calendar season boundaries (month and day) and, per season, ten weighted weather level adjustments. Verdict: designer-data.

## Behavior

- V: the span is the number of boundary pairs the current (month, day) has passed, 0..4; byte [span] selects the adjustment row
- V: the new level is the old level plus a random entry of the row, clamped to 0..4, stored unless a flag word is set

## Notes

Our names. Tags: V layout, V reader, I meaning of the scene variables as weather.

## Open questions

None recorded.
