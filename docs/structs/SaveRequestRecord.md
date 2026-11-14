# SaveRequestRecord

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)
- **Size:** 328 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One queued file request of the save container manager: the consumer object, the entry name, the delivery buffer and its status. The queue is a vector on qword_140C69698 (first +0x40, last +0x48) of 328-byte (0x148) records, guarded by the critical section at +0x10 of the same object.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="size"></a>`0x0` | size | `uint64` | V | Size of the delivered payload (the entry minus its 16-byte header). |
| <a id="data"></a>`0x8` | data | `void *` | V | The delivered payload; the delivery allocates it with the record's heap. |
| <a id="heap"></a>`0x10` | heap | `allocator *` | V | Allocator the delivery copies the payload with. |
| <a id="obj"></a>`0x18` | obj | `SaveData *` | V | The object the entry is delivered to: its +624 buffer and +632 size receive the payload. |
| <a id="name"></a>`0x20` | name | `char[256]` | V | Entry name, NUL-terminated; this is what the read kick filters on. |
| <a id="flag"></a>`0x120` | flag | `uint8` | V | Handed to the delivery call unchanged (0 in the requests observed). |
| <a id="status"></a>`0x140` | status | `uint32` | V | Delivery status; 0 on the normal path. |

## Behavior

- V (queue and delivery code, 2026-11-02): a read request is pushed by sub_140033CBC with the object and the name, and served by sub_140033DF0, which copies the entry's 16-byte header into the object, calls the object's handler, then runs the object's post-delivery step.
- V: the records are contiguous at stride 328 between the vector's first and last pointers, so a service can walk first..last and compact the ones it served.
- V: the same queue carries the manual slot request (`fftsave.bin`), the settings request and every autosave entry, so one read kick serves them all.
- I: a request that no kick serves stays queued until a later load or until the object is destroyed.

## Referenced by

- Read by: [sub_140033DF0](../functions/sub_140033DF0.md), [sub_140034D7C](../functions/sub_140034D7C.md), [sub_140035A28](../functions/sub_140035A28.md), [sub_140036064](../functions/sub_140036064.md)
- Written by: [sub_140033CBC](../functions/sub_140033CBC.md)

## Notes

The queue object also holds the busy flag at +392 and a byte at +602 that is cleared before a request, so a request made while a container write is in flight returns an error string.

## Open questions

? the flag at +0x120 (0 in every request seen); ? whether an unserved record is ever removed by the game itself.
