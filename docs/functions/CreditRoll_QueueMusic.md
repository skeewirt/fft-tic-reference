# CreditRoll_QueueMusic

- **Address:** `0x1401BF828`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void CreditRoll_QueueMusic(void *roll, int sound, int y)`
- **Callers:** sub_1401CB254
- **Callees:** sub_1401C04F0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues a music change of the credit roll at a roll position.

## Behavior

- V: pushes (sound, y position) onto the roll's queue through sub_1401C04F0; the music starts when the roll reaches that position.

## Notes

Name is ours; the start itself is in code not read here.

## Open questions

? where the queue is consumed.
