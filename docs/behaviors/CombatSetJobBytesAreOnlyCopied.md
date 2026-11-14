# CombatSetJobBytesAreOnlyCopied

- **Kind:** observed behaviour
- **Scope:** engine (party and save records)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md), [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md), [JobScreen_RefreshAfterChange](../functions/JobScreen_RefreshAfterChange.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The three combat-set job bytes of a unit record (party record +462, +550, +638; save record +380, +468, +556) are never read as a job by the status, equipment or combat-set screens: every access seen is a whole-record copy or clear.

## Behavior

- V (read/write data watch on party record 0 +462, 75 s, opening Status, Equipment and Combat Sets on save slot 9): 15 accesses, all from copies. PartyUnit_FillFromWork (4, the save record copied into the party record), PartyUnit_WriteBackToSave (1, the reverse), a library memset (4), and two 16-byte block copies of a whole record at 0x1402BD42E (inside JobScreen_RefreshAfterChange) and 0x1402898D5 (an unnamed function); the disassembly of both shows a run of 16-byte moves over the record, not a test or a lookup of the byte.
- I: nothing compares the byte or uses it as a table row, so the three bytes are plain copy payload. Sets 1 and 2 (+550, +638) and the save-side bytes were not watched separately: the copies move the whole record, so they follow set 0.

## Open questions

? whether a battle or an event reads a set job (only the three menu screens were watched; the job-change screen was not opened in this run).
