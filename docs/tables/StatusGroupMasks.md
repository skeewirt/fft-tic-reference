# StatusGroupMasks

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (constant)
- **Rows:** 10 rows of 5 entries of 1 byte
- **Held in:** [g_StatusGroupMasks](../globals/g_StatusGroupMasks.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The ten party-wide status group masks, five bytes each: a group test ANDs these bytes against the unit status bytes at +0x61..+0x65.

## Open questions

None recorded.
