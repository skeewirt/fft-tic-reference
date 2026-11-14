# Pad_ReadSticks

- **Address:** `0x1400201F4`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void Pad_ReadSticks(PadObject *pad, XINPUT_STATE *state, int8 out[4])`
- **Callers:** Pad_Poll
- **Callees:** sub_14001C080 (dead zone)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns the two thumb sticks of one XInput state into four signed bytes in -100 .. 100.

## Behavior

- V: each stick axis is a signed 16-bit value divided by 32767 (negative values by 32768); the pair goes through sub_14001C080 with the stick's threshold (pad+592 for the left stick, pad+596 for the right), then out[i] = truncate(value * 100).
- V: output order out[0] = left stick X, out[1] = left stick Y, out[2] = right stick X, out[3] = right stick Y.
- I: these four bytes become the input state's bytes +1224 .. +1227 (UI code reads those offsets in the same order; +1227 is the right stick's vertical axis in the list scroller).

## Referenced by

- Called by: [Pad_Poll](Pad_Poll.md)
- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The name is ours (IDB: sub_1400201F4).

## Open questions

? what sub_14001C080 does exactly (radial or per-axis dead zone, rescale) and the values of the two thresholds; ? how the output block is copied into the input state at +1224.
