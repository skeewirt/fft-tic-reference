# SceneObject_SnapFieldBands

- **Address:** `0x140272B6C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `struct _exception *SceneObject_SnapFieldBands(void)`
- **Callers:** EventScript_Run (the 0xE3 transition path)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Walks the linked list at qword_140D3A410 and sets a 16-bit field of each entry from that entry's low 12 bits of another field; EventScript_Run calls it at the start of the 0xE3 transition path.

## Behavior

- V: starts at qword_140D3A410 and follows the first qword of each entry as the next pointer until it reaches null.
- V: for each entry it reads a 16-bit field at an offset inside the entry that the decompile expresses through the entry's third sub-record (exact byte offset not resolved) and keeps its low 12 bits.
- V: when those bits are 512 to 1535 it writes 1024 to the second 16-bit field of the entry; when they are 1536 to 2559 it writes 2048; when they are 2560 to 3583 it writes 3072.
- V: otherwise, including values below 512 and from 3584 up, it writes 0 to that field.
- V: returns the end of the list (null).

## Notes

The same list is walked by the mode 255 branch of EventScript_SetupScene.

## Open questions

What the two fields of each list entry are; what the value written represents; the exact byte offsets, which the decompile shows only as field-unit offsets.
