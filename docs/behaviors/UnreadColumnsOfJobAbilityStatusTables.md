# UnreadColumnsOfJobAbilityStatusTables

- **Kind:** observed behaviour
- **Scope:** engine (nxd tables)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [GameState_ResetJobFlags](../functions/GameState_ResetJobFlags.md), [JobRecord_FillIconAndGenericFlag](../functions/JobRecord_FillIconAndGenericFlag.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Columns of the GeneralJob, Job, JobCommand, JobType, Ability and UIStatusEffect tables that no code of the game reads; their values change nothing in play.

## Behavior

- V: every reader of each table was read; none reads GeneralJob +0x00, +0x04, +0x79..+0x7B; Job +0x00, +0x04; JobCommand +0x00, +0x18; JobType +0x00, +0x04; Ability +0x00, +0x14, +0x1A, +0x1C; UIStatusEffect +0x00, +0x04.
- V: GeneralJob +0x78 is read only by GameState_ResetJobFlags, which stores (value == 0) in bytes 0..20 of the job flag block; no code reads those bytes back, so the value has no visible effect.
- V: JobType is read only by JobRecord_FillIconAndGenericFlag (+0x08 and +0x0C, chosen by bit 7 of a unit key byte).

## Open questions

? who, if anyone, reads bytes 0..20 of the job flag block (saved with the game).
