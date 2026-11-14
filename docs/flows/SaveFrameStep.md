# SaveFrameStep

- **Kind:** flow
- **Area:** [Save data](../areas/save-data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a manual save or load reaches the file: the save screen changes a command, and one frame step does the work once per frame, blocking that frame while the container is read or written. Store, load and image-to-cache are the three cases of the same step; the UI never touches the container.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 |  | V | A save, delete or import callback sets the command on the save-I/O state (1 store, 2 load, 3 image to cache) and returns; the screen keeps reading the cache. |
| <a id="2"></a>2 |  | V | The frame update calls the step once per frame; it reads the command and runs exactly one case. |
| <a id="3"></a>3 | [SaveSlots_StoreToFile](../functions/SaveSlots_StoreToFile.md) | V | Case 1: the 50-slot cache is copied into the manager image and queued as the `fftsave.bin` entry; the PNG write is requested on the request object. |
| <a id="4"></a>4 |  | V | Case 2 first probes the area file; when it is absent the command is cleared and no load happens (an absent file is no save data, not an error). |
| <a id="5"></a>5 | [SaveSlots_LoadFromFile](../functions/SaveSlots_LoadFromFile.md) | V | Case 2: the image is filled with the empty-slot pattern and the entry is requested; the container is read and the payload delivered before the step returns. |
| <a id="6"></a>6 |  | V | Case 3: the manager image is copied into the cache (2,008,200 bytes), which is how a freshly loaded or imported image reaches the list. |
| <a id="7"></a>7 |  | I | The step ends at the reset path, which sets the command back to 0; nothing runs until a callback sets it again (the absent-file path does this explicitly). |

## Behavior

- V: one case per frame, and a load that spans a container read completes inside that same step (the read is synchronous).
- V: the step is the only place the cache and the container meet, so answering store and load there leaves the rest of the save screen untouched.
- V: the load case probes the area file, not the entry, so a container without the entry also ends with an empty list and no dialog.
- I: everything in the step runs on the game thread inside the frame update, so a replacement may block the frame exactly as the game does.

## Notes

The frame update reaches the step once per frame; the save, load and delete callbacks run in the same update, so the command is normally set and consumed in different frames.

## Open questions

? what sets the sub-state at +0x108 within a step that needs more than one frame.
