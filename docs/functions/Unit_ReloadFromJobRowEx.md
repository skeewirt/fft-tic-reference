# Unit_ReloadFromJobRowEx

- **Address:** `0x1402788EC`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Unit_ReloadFromJobRowEx(uint8_t *work)`
- **Callers:** not enumerated
- **Callees:** not enumerated

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The same re-read of the job row as Unit_BuildInnateStatuses (0x140278688, the plain variant), reading the status bytes from a second copy at +495 (head read).

## Behavior

- V: the row is JobTable + 49 * work[3]; job 0xA1 uses row 164 when the low nibble of work+238 is 8 or more.
- V: the first copies are the same as Unit_BuildInnateStatuses's (+66, +67, +82, +87, +92, +96, +97, +101, +118 from the row).

## Referenced by

- Called by: [sub_1402855F0](sub_1402855F0.md)
- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md)

## Notes

Only the row reads were studied. The row offset is in r8 after 0x140278954 (row stride 49). V: it rewrites Move +0x42 and Jump +0x43 from the job row (+24, +25 & 0x7F) as the plain variant does.

## Open questions

Whether the Ex variant differs from the plain one in anything besides where it takes the saved status bytes (? tail not read).
