# RuntimeJobList

- **Kind:** table
- **Storage:** Executable (filled at run time)
- **Held in:** [g_RuntimeJobList](../globals/g_RuntimeJobList.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint16[48]: job id (low 13 bits) | 0x2000 locked | 0x4000 released by another member (mode 3) / current (mode 2); 0xFFFF ends it.

## Open questions

None recorded.
