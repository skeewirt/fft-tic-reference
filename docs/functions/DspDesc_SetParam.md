# DspDesc_SetParam

- **Address:** `0x140608B24`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void __fastcall DspDesc_SetParam(__int64 state, int paramId, float value)`
- **Callers:** only through the table at 0x14065CB00 (slot 6)
- **Callees:** powf, sub_140420C50

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 6 of the descriptor table at 0x14065CB00: sets one of three float parameters of a state object from a normalised value.

## Behavior

- V: the state holds a parameter count at +12 and a pointer to a float array at +16.
- V: parameter 0 (when the count is non-zero) and parameter 1 (when the count is above 1) are set to `2 ^ (2 * value - 1)` through `powf`; parameter 2 (when the count is above 2) is set to `value` unchanged.
- V: any other id calls `sub_140420C50(0, text)` with a message that reads "Invalid DSP Parameter ID" after a numeric prefix, and sets nothing.

## Notes

V: whole body read. The name is ours. The formula maps 0..1 to 0.5..2.

## Open questions

?: what the three parameters are (two are exponential ratios, one linear).
