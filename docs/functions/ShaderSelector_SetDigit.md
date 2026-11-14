# ShaderSelector_SetDigit

- **Address:** `0x1403C4AA8`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 ShaderSelector_SetDigit(ShaderSelector *s, unsigned slot, int value)`
- **Callers:** UIBlur_DrawPass, sub_1403AD710, UIBlur_CopyTarget (sub_1403ABEDC), the glow / effect passes that bind a sampler state
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets one mixed-radix digit of the selector's state dword (the permutation index that ShaderSelector_Apply uses) and marks the state dirty.

## Behavior

- V: state = dword at s+24; the radix table is the dword array at s+32 with the count at s+28. When slot < count: v8 = table[slot], v9 = table[slot + 1] (1 when slot + 1 >= count).
- V: the old digit (state % v8) / v9 is the return value. The new state replaces that digit: state = state - state % v8 + state % v8 % v9 + v9 * (value * v9 < v8 ? value : 0), so a value that does not fit in the radix is stored as 0.
- V: the state is written back and the byte at s+76 is set to 1 on every call, including when slot is out of range (then the state is unchanged and the return value is an uninitialised register).

## Referenced by

- Called by: [PostTarget_DrawFitted](PostTarget_DrawFitted.md), [UIBlur_CopyTarget](UIBlur_CopyTarget.md), [UIBlur_DrawPass](UIBlur_DrawPass.md), [UIBlur_DrawTexturedPass](UIBlur_DrawTexturedPass.md), [sub_1403B5170](sub_1403B5170.md)

## Notes

The name is ours. The blur code calls it as sub_1403C4AA8(*(b + 32 or 48), slot, value) with slots 0..2. That the object is the selector handed to ShaderSelector_Apply is inferred from its use next to those calls.

## Open questions

What each slot / value means for the shaders (slot 0 = 1 in UIBlur_CopyTarget or the flags argument in sub_1403AD710; slot 1 = filter index 0/1/2 in UIBlur_CopyTarget or (clamp == null) in sub_1403AD710; slot 2 = taps - 2 clamped to 7 in sub_1403AD710); where the radix table is filled.
