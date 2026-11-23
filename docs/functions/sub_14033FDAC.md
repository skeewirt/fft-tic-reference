# sub_14033FDAC

- **Address:** `0x14033FDAC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void sub_14033FDAC(int kind, int parameter)`
- **Callers:** sub_14034004C, sub_14033F8C0, the function at 0x140370E14 and the other audio command users
- **Callees:** sub_14033FE00, sub_1402F377C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Pushes one entry (a kind and a 32-bit parameter) onto the 16-entry audio command queue, draining the queue first when it is full.

## Behavior

- V: while the entry count (the dword at 0x140D49558) is 16 or more it calls the queue service function sub_14033FE00 and then sub_1402F377C(1), and tests again.
- V: stores the kind in the dword array at 0x140D494D0 and the parameter in the dword array at 0x140D49510 (reached as the kind array's address plus 0x40 through the same base register) at the position of the entry count, then increments the count.
- V: the parameter is stored as a whole dword; nothing here masks it (the decode of a kind 1 parameter is in sub_14033FE00).

## State touched

- Calls: [sub_14033FE00](sub_14033FE00.md)

## Referenced by

- Called by: [Errand_ProfitEndStep](Errand_ProfitEndStep.md), [EventCmd_FadeOut](EventCmd_FadeOut.md), [EventViewer_EntryPage](EventViewer_EntryPage.md), [sub_14034004C](sub_14034004C.md), [sub_140372F9C](sub_140372F9C.md)
- Observed behaviours: [MusicParameterOfTheAudioQueueIsASmallConstantOrTheCommandWord](../behaviors/MusicParameterOfTheAudioQueueIsASmallConstantOrTheCommandWord.md)

## Notes

The queue arrays and the counter are the ones sub_14033FE00 describes; no lock is taken (the audio command functions run on the game thread).

## Open questions

What sub_1402F377C(1) waits for.
