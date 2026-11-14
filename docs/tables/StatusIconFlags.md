# StatusIconFlags

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (constant)
- **Held in:** [g_StatusIconFlags](../globals/g_StatusIconFlags.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The per-status flag words the status panel update reads: index status+1, no bound check. Entries past 40 exist, so a forty-first status reads a meaningful but unintended value.

## Open questions

None recorded.
