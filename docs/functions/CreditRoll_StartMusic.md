# CreditRoll_StartMusic

- **Address:** `0x1401BF8C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void CreditRoll_StartMusic(void *roll, int sound)`
- **Callers:** sub_1401BDD94, sub_1401CB254
- **Callees:** EventSoundEntry_SetStateById, EventSoundEntry_Append

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts the credit roll's first music.

## Behavior

- V: sets the state of the previous event sound entry (EventSoundEntry_SetStateById) and appends the new one with EventSoundEntry_Append.

## State touched

- Calls: [EventSoundEntry_SetStateById](EventSoundEntry_SetStateById.md), [EventSoundEntry_Append](EventSoundEntry_Append.md)

## Notes

Name is ours.

## Open questions

None recorded.
