# GameState_ResetJobFlags

- **Address:** `0x14028433C`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `void GameState_ResetJobFlags(void)`
- **Callers:** new-game path (not traced)
- **Callees:** sub_1400DF7D8, sub_1400B6390, sub_1400C61BC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

New-game reset that initialises byte_1411A7490: 125 per-jobtype flags (at +21) to 1 and 21 per-generic-job flags (at +0) to (GeneralJob.Unknown78 == 0), then clears a block of party/story state.

## Behavior

- V: loop `for (j = 0; j < 21; ++j) flag[j] = (GeneralJob[j] byte +120 == 0)`; Unknown78 is 0 only in rows 0 and 1.

## Referenced by

- Called by: [GameState_ResetParty](GameState_ResetParty.md)

## Notes

Row 20 gets flag 0: its Unknown78 is 1 in stock (data).

## Open questions

Meaning of the flag array (I: 'job / type not yet owned').
