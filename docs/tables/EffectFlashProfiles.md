# EffectFlashProfiles

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1407B0738`
- **Rows:** 4 rows of 14 bytes
- **Keyed by:** flash profile 0..3
- **Read by:** [EffectFlash_Start](../functions/EffectFlash_Start.md)
- **Row layout:** [EffectFlashProfilesRow](../structs/EffectFlashProfilesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Seven parameter words per screen flash profile (timing and strength values; the high byte of the last word picks a blend weight row). Verdict: designer-data.

## Behavior

- V: EffectFlash_Start copies words 0..6 of the row into the flash state; word 6 splits into two bytes

## Notes

Our names. Tags: V layout, ? parameter meanings.

## Open questions

- ?: what the five leading words do (durations, intensities)
