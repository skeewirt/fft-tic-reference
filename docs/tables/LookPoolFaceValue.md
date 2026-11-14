# LookPoolFaceValue

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable (filled at run time)
- **Rows:** 10 entries of 4 bytes
- **Held in:** [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle face value per look pool record 0..9: sub_14026E838 stores the scene unit's sprite byte; cleared to -1 by sub_140210AF0, saved and restored by sub_140304BEC; ten readers use it as a face number behind the 0xCD cap (turn panels, unit status, deployment icons, dialogue face slots).

## Open questions

None recorded.
