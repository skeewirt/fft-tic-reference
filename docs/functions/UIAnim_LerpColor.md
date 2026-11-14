# UIAnim_LerpColor

- **Address:** `0x1404022A8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `uint8_t *UIAnim_LerpColor(uint8_t out[4], uint32_t c0, uint32_t c1, float t)`
- **Callers:** UIAnim_SampleColorTrack
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-channel linear blend of two packed RGBA colours with truncation and clamping to 0..255.

## Behavior

- V: for each byte i = 0..3 of the two dwords: v = (float)(c1[i] - c0[i]) * t + (float)c0[i]; out[i] = (int)clamp(v, 0, 255) (compare >= 255.0 then take 255.0; compare <= 0.0 then 0.0; the final (int) is a truncation toward zero).
- V: returns the out pointer. The four channels are treated alike (alpha is byte 3 of the dword).

## Referenced by

- Called by: [UIAnim_SampleColorTrack](UIAnim_SampleColorTrack.md)

## Notes

The name is ours (IDB: sub_1404022A8). Gives the byte-exact rule for colour keyframes: float math on the byte difference, then truncate (not round).

## Open questions

None recorded.
