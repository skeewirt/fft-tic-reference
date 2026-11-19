# Guide_QueueAutoShow

- **Address:** `0x1400EDFBC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Guide_QueueAutoShow(int id)`
- **Callers:** not recorded
- **Callees:** Guide_GetEntry, Input_PauseFor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues a guide to be opened, with its input-pause delay.

## Behavior

- V: when delay (+0x20, f32) is above 0, calls Input_PauseFor(value + 1/30 s); the id is queued with the delay in the queue at [[qword_143CD9DA8+16]+264] +88, 12-byte entries {id, delay, 0}.

## State touched

- Calls: [Guide_GetEntry](Guide_GetEntry.md), [Input_PauseFor](Input_PauseFor.md)

## Open questions

None recorded.
