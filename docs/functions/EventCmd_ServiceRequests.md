# EventCmd_ServiceRequests

- **Address:** `0x1402F1784`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void EventCmd_ServiceRequests(uint32_t reqA, uint32_t reqB, uint32_t reqC, int64_t extra)`
- **Callers:** EventCmd_Run, `sub_1402F109C`
- **Callees:** EventVar_Write (3), `sub_1401D80A8`, `sub_1402F1868`, `sub_1402F2500`, `sub_1402B1F08`, `sub_1402B1FB4`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Services the three request mailboxes (event variables 0x5C, 0x5D and 0x5E) that event commands use to ask for sounds and music, then clears them.

## Behavior

- V: does nothing when all three values are zero.
- V: when a field of the command register (`WORD6(xmmword_141862460)`) is 0, a non-zero first request is sent through `sub_1401D80A8(qword_143CD9DD8, 10, reqA, extra)` and a non-zero second request through `sub_1402F1868`.
- V: when that field is 1, the same two requests are sent, and a non-zero third request different from the byte at `xmmword_141862460 + 10` also goes through `sub_1402F2500` and sets a bit in `qword_140D49558`.
- V: afterwards all three variables are written back to 0 with EventVar_Write.
- I: the three requests are sound-effect, music and a third kind of cue (likely a voice or ambience cue).

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [sub_1401D80A8](sub_1401D80A8.md), [sub_1402F2500](sub_1402F2500.md)

## Referenced by

- Called by: [EventCmd_Run](EventCmd_Run.md)
- Observed behaviours: [EventSoundGroupAndMusicSlotOperandWidths](../behaviors/EventSoundGroupAndMusicSlotOperandWidths.md), [MusicCommandWordHasEighteenOperandsAndSixOfThemOnlyWriteZeroOrTestNonzero](../behaviors/MusicCommandWordHasEighteenOperandsAndSixOfThemOnlyWriteZeroOrTestNonzero.md), [MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath](../behaviors/MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath.md)

## Notes

Event variables 0x5C to 0x5E act as a mailbox between event commands and the sound system.

## Open questions

Decode the three request kinds.
