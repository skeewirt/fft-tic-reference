# Formula_BardDancerGate

- **Address:** `0x140304D5C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_BardDancerGate(void)`
- **Callers:** Formula_28_BardSongs, Formula_29_DancerDances
- **Callees:** Rng_Percent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The Bard and Dancer hit roll: scales the shown percent by X and rolls a miss against X.

## Behavior

- V: R+44 = X * R+44 / 100, with X the ability record copy's byte +9 (block +0x2D).
- V: while g_BattleSimulating is non-zero it returns 0 without rolling; otherwise Rng_Percent(100, X) true (the roll failed the X-percent event) stores R+0 = 0 and R+2 = 6 and returns 1.

## State touched

- Calls: [Rng_Percent](Rng_Percent.md)

## Notes

Source: block B08. 99 bytes, read whole. Called by Formula_28_BardSongs and Formula_29_DancerDances. Crosscheck: block +0x2D is read as the byte at 0x1407B079D (byte 13 of the 16-byte item at 0x1407B0790), a RIP-relative operand.

## Open questions

None recorded.
