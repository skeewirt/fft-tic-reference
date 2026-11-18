# JobMasteryIds

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x14071EA38`
- **Rows:** 2 rows of 4 bytes
- **Keyed by:** list position
- **Read by:** [Unit_BuildJobUnlockMask](../functions/Unit_BuildJobUnlockMask.md)
- **Row layout:** [JobMasteryIdRow](../structs/JobMasteryIdRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The two jobs whose full mastery gates job index 20 (Knight and Black Mage by id).

## Behavior

- V: mastery of both is tested by the unlock mask builder.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- I: only job index 20 uses it
