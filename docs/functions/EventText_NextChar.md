# EventText_NextChar

- **Address:** `0x140221404`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `char *EventText_NextChar(int *runLeft, char *pos, char **returnTo)`
- **Callers:** EventMessage_Task (15 uses), `sub_1402DB09C`
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Advances through an event message byte stream by one position, following the stream's back-reference codes.

## Behavior

- V: returns null when `pos` is null; otherwise moves one byte forward.
- V: `*runLeft` counts the bytes left in a back-reference run; when it reaches 0 the position is restored from `*returnTo`, which is then set to -1.
- V: when the byte at the new position has the high nibble 0xF and a low nibble below 4 (codes F0 to F3) it is a back-reference: `*returnTo` is set to the position three bytes on, `*runLeft` to `(b1 >> 5) + 8 * (b0 & 3) + 4`, and the position moves backwards by `b2 + 254 * (b1 & 0xF)`.
- I: this is an LZ-style compression of the message text: a short reference copies an earlier run of text.

## Referenced by

- Called by: [EventMessage_Scripted](EventMessage_Scripted.md), [EventMessage_Task](EventMessage_Task.md)
- Observed behaviours: [StoryChoiceBalloon](../behaviors/StoryChoiceBalloon.md)

## Notes

Only the position bookkeeping is here; the character codes themselves are handled by the caller.

## Open questions

The meaning of the control bytes above 0xF3 and how the text length is bounded.
