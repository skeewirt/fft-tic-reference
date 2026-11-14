# JobScreen_ShowPopup

- **Address:** `0x1402BB5D4`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `int64_t JobScreen_ShowPopup(int64_t a1, int64_t a2)`
- **Callers:** sub_1402B90D4, sub_1402B9598, sub_140366FE0, sub_140369AB0
- **Callees:** sub_14031E94C, SoundCue_Play

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Thin wrapper that opens a message popup: forwards to sub_14031E94C, sets a screen flag and starts popup SoundCue_Play(a2 - 1).

## Behavior

- V: body is three calls and two stores: sub_14031E94C(a1, a2, a1), byte_140D407BF = 1, SoundCue_Play(a2 - 1), dword_141849E14 = 1.
- V: no name lookup of its own, so it cannot be the source of a wrong job name.
- I: 'popup' from the callers (job-change and learn flows); 4 callers.

## State touched

- Calls: [SoundCue_Play](SoundCue_Play.md)

## Referenced by

- Called by: [JobScreen_BuildLearnList](JobScreen_BuildLearnList.md), [JobScreen_FillUnitRows](JobScreen_FillUnitRows.md), [sub_140366FE0](sub_140366FE0.md)

## Open questions

What a2 selects.
