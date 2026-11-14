# PreviewBuildersReadPartyRecordCopies

- **Kind:** observed behaviour
- **Scope:** engine (party and save records)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [sub_1402C185C](../functions/sub_1402C185C.md), [sub_1402C1628](../functions/sub_1402C1628.md), [sub_14036BBFC](../functions/sub_14036BBFC.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The unit detail and summary builders (sub_1402C185C, sub_1402C1628) read a party record copied in three parts (header from +34, middle from +48, block from +112); the header names the save slot (header + 10 = +44), and the Fitting screen's stack copy of party record 54 is such a copy.

## Behavior

- V (code): the header's +10 is the save slot: sub_1402C1628 indexes the save records by it; every writer of the shared header buffer copies the party record's +0x22 / +0x2A / +0x2E.

## Open questions

? sub_1403783F0 writes a header of its own (its +10 may be stale).
