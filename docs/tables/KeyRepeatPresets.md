# KeyRepeatPresets

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** Executable
- **Address:** `0x140680480`
- **Rows:** 8 rows of 6 bytes
- **Keyed by:** option bits 9..11 of the game option word 0x140782A24
- **Read by:** [EventPad_UpdateRepeat](../functions/EventPad_UpdateRepeat.md)
- **Row layout:** [KeyRepeatPreset](../structs/KeyRepeatPreset.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Key-repeat timing presets, one row per value of a 3-bit input option. Verdict: engine-data.

## Behavior

- V: index masked with 7 (8 rows); the data continues past 48 bytes
- V: sub_140246078 and sub_1402B4710: copy the row of the current option value into the input globals
- V: EventPad_UpdateRepeat compares held-key counters with thresholds +0xFB/+0xFE/+0xFF

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: which settings-menu option bits 9..11 hold (cursor speed?)
- ?: roles of +3..+5
- ?: whether rows past 8 are another table
