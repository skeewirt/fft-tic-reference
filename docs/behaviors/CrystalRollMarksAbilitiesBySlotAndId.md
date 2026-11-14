# CrystalRollMarksAbilitiesBySlotAndId

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [sub_140271EFC](../functions/sub_140271EFC.md), [sub_140323D1C](../functions/sub_140323D1C.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A crystal's roll marks each rolled ability by its skillset slot (that is what is learned) and, for the pickup window, by its id in two 512-bit sets; an id above 0x1FF is learned but not listed.

## Behavior

- V (code): sub_140271EFC sets the slot bit (stack byte per job) before the id test; the result block's sets at +94 (all jobs) and +177 + 64 * job get the id's bit only when the id is at most 0x1FF.
- V (code): sub_140323D1C lists one entry per set bit of +94 (text id 0x7000 + id) with the job id of the first job whose set holds it (+158 + job) into two 512-entry lists, then sets up the pages from the count.

## Open questions

None recorded.
