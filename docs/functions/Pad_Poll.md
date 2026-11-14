# Pad_Poll

- **Address:** `0x1400200F8`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `char Pad_Poll(PadObject *pad, uint8 *out)`
- **Callers:** pad update (not traced)
- **Callees:** XInputGetState, Pad_ReadSticks, sub_140020350

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Polls pad number pad+608 with XInputGetState and fills one output block: sticks, triggers, buttons.

## Behavior

- V: XInputGetState(pad+608, state); a non-zero result returns 0 and nothing is written.
- V: Pad_ReadSticks writes out[0..3]; out[4] = left trigger / 255 * 100 and out[5] = right trigger / 255 * 100 (truncated, 0 .. 100); sub_140020350 merges the button bits into the dwords at out +8 / +12 / +16 (bit numbers: Input_UpdateActionRow). Returns 1.
- I: the trigger bytes are the input state's bytes +1228 / +1229 (sub_1400F0BC8, the 'any input' test, reads +1224 .. +1229 together).

## State touched

- Calls: [Pad_ReadSticks](Pad_ReadSticks.md)

## Notes

The name is ours (IDB: sub_1400200F8).

## Open questions

None recorded.
