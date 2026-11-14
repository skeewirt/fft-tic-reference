# LookSumSeesTheBaseJob

- **Kind:** observed behaviour
- **Scope:** engine (portrait look index)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [sub_14032AB3C](../functions/sub_14032AB3C.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [EventMessage_Scripted](../functions/EventMessage_Scripted.md), [sub_140300768](../functions/sub_140300768.md), [sub_140300D74](../functions/sub_140300D74.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Five functions compute a save unit's portrait look index from its job byte (2 * job - 52, + 1 for marker 0x81), each against its own copy of the portrait code words. A job byte of 174..255 gives index 296..458.

## Behavior

- V: in all five the code after the marker test is the same: marker 0x80 loads the job byte (record +2) and computes 2 * job - 52, 0x81 2 * job - 51, Mime (93) two less; the loaded byte is also copied for the job 91 / 92 tests (index 130 / 131); the index guard compares with 0xD3.
- V: stock (211 rows) an index of 211 or more fails the guard and takes the no-code path.
- V: the later job 160 / 161 / 164 tests read the job byte from the record again; a job in 74..93 never matches them.

## Open questions

None recorded.
