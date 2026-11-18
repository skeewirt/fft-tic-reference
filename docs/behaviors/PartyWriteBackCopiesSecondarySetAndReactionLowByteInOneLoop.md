# PartyWriteBackCopiesSecondarySetAndReactionLowByteInOneLoop

- **Kind:** observed behaviour
- **Scope:** engine (party record to save record)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md), [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

PartyUnit_WriteBackToSave copies two bytes in one two-pass loop: the low byte of the party record's secondary command word into save +7, then the low byte of the equipped reaction word into save +8; the reaction's high byte goes to save +9 on its own. The party record is then rebuilt from the save record.

## Behavior

- V (decompiled): the loop walks the party words at +0x60 and +0x62 (2 bytes apart) and stores each word's low byte into save +7 and +8; +0x63 is copied to save +9, and the support and movement words' bytes to save +10..13.
- V (seen live 2026-11-17, a watch on both records): equipping a reaction stored the word in party +0x62, the write-back copied it to save +8 / +9, a fill cleared the party record and PartyUnit_FillFromWork wrote save +8 / +9 back into party +0x62.
- I: so whatever the write-back stores at save +8 is what the unit has equipped after the rebuild: an equip that the write-back alters is undone at once.

## Notes

The equip path: sub_140333338 -> sub_14028916C (stores party +0x5E + 2 * slot, then rebuilds through sub_140285A6C).

## Open questions

None recorded.
