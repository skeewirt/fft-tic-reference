# EventControl_Reset

- **Address:** `0x1401DB370`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_Reset(EventControl *ctl)`
- **Callers:** sub_14020DC78, sub_14020E174 (when the event tick did not return 1), and sub_1402024A8 right after it allocates the 64-byte EventControl
- **Callees:** sub_1401DBBB0, sub_1401D6F9C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the event pause overlay state on frames where no event script tick ran.

## Behavior

- V: closes the overlay (sub_1401DBBB0), zeroes the qwords +8 (state and previous state) and +16, the dword +32, the qword +24 and the qword +36, writes 256 to the dword +44, zeroes the dword +49, the byte +53, the word +55 and the byte +57.
- V: calls sub_1401D6F9C(qword_143CD9DD8, 7, 0).

## State touched

- Writes: [EventControl.state](../structs/EventControl.md#state), [EventControl.prev_state](../structs/EventControl.md#prev_state), [EventControl.pause_block_a](../structs/EventControl.md#pause_block_a), [EventControl.pause_block_b](../structs/EventControl.md#pause_block_b)

## Notes

So EventControl +8 is 0 whenever no event script is ticking.

## Open questions

None recorded.
