# SaveManager

- **Kind:** structure
- **Area:** [Save data](../areas/save-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The two singletons the save path runs on, with the fields it uses: the save-I/O state object that holds the frame step's command and sub-state, and the save manager object that holds the 50-slot image the `fftsave.bin` payload is built from. The offsets below name the object each field belongs to.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="command"></a>+0x104 (I/O state) | command | `uint32` | V | The step the frame step will run: 1 store, 2 load, 3 image to cache (0 idle). | [sub_140034C64](../functions/sub_140034C64.md), [sub_140034CF0](../functions/sub_140034CF0.md), [sub_1400C3B84](../functions/sub_1400C3B84.md), [sub_1400C4214](../functions/sub_1400C4214.md), [sub_1400C480C](../functions/sub_1400C480C.md), [sub_14018403C](../functions/sub_14018403C.md) |  |
| <a id="sub_state"></a>+0x108 (I/O state) | sub_state | `uint32` | V | Phase of the current step: its progress inside the case the frame step is running. |  |  |
| <a id="image"></a>+0x5F8 (manager) | image | `uint8[0x1EA488]` | V | The 50-slot image, 2,008,200 bytes: the payload of `fftsave.bin` on a store and the source of the cache after a load (1528 decimal). | [sub_1400C2ED8](../functions/sub_1400C2ED8.md), [sub_1400C6008](../functions/sub_1400C6008.md), [sub_140183DD4](../functions/sub_140183DD4.md) | [sub_140034D7C](../functions/sub_140034D7C.md), [sub_140036D8C](../functions/sub_140036D8C.md) |
| <a id="game_save_data"></a>+0x388 (manager) | game_save_data | `ptr` | V | The GameSaveData sub-object the entry queue writes into (904 decimal). |  |  |

## Behavior

- V: the frame step reads the command from the save-I/O state object and runs one case; the UI callbacks only set the command, so the screen never touches the container.
- V: the image is a mirror of the cache: a store copies the cache into it, a load copies it back (2,008,200 bytes), so the two always hold the same 50 slots.
- I: the sub-state is a phase counter rather than a retry count, because a step that finishes clears the command instead of incrementing it.

## Referenced by

- Written by: [sub_1400348F8](../functions/sub_1400348F8.md), [sub_1400C4690](../functions/sub_1400C4690.md)

## Notes

The save-I/O state object is qword_140D405B8 and the manager is qword_143CD9EE0; the request object qword_140C69698 is a third object (SaveRequestRecord).

## Open questions

? the other fields of the save-I/O state object, and whether +0x108 is ever nonzero at the start of a frame.
