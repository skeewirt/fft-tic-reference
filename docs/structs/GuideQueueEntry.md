# GuideQueueEntry

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of the queue of guides waiting to open, at [[qword_143CD9DA8+16]+264] +88.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="guide_id"></a>`0x0` | guide_id | `int32` | V | The Guide key. |
| <a id="delay"></a>`0x4` | delay | `float` | V | Seconds of input pause before it opens (Guide delay, +0x20). |
| <a id="zero"></a>`0x8` | zero | `int32` | V | Written as 0. |

## Behavior

- V: Guide_QueueAutoShow appends {id, delay, 0}.

## Notes

Sheet: Guide_QueueAutoShow.

## Open questions

? the reader of the queue.
