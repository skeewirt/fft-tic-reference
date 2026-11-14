# GUIInputQueue_Pop

- **Address:** `0x1403DC32C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUIInputQueue_Pop(GUIInputQueues *q, InputEvent *out, int port)`
- **Callers:** GUICore_OnInputState, sub_1403D6098 and two vtable entries
- **Callees:** memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Pops the oldest 68-byte input record of queue `port` (vector at q + 32 * port) into out; false when empty.

## Behavior

- V: v = q + 32 * port; begin = v+8, end = v+16; begin = end -> 0. Otherwise out = the 68 bytes at begin (4 x 16 + 4), memmove the rest down by 68 and end -= 68; returns 1.

## Notes

The name is ours (IDB: sub_1403DC32C). 120 hits per 4 s. A FIFO implemented as erase-front (O(n)); order is strictly first in, first out.

## Open questions

? Layout of the 68-byte record (I: button / stick state).
