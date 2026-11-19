# Formula_MagicAvgDamage

- **Address:** `0x140306F9C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_MagicAvgDamage(void)`
- **Callers:** Formula_95_NanoflareReDispatchesToF30, sub_140309310
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets A = MA and B = (MA + Y) / 2, then jumps into the magic damage tail.

## Behavior

- V: A = caster MA (+0x3F); B = (MA + Y) >> 1 with Y the ability record copy's byte +10 (block +0x2E).
- V: it continues in Formula_MagicDamageTail by a tail jump (no return to this body).

## Referenced by

- Called by: [Formula_96_MagicAveraged](Formula_96_MagicAveraged.md)

## Notes

Source: block B45 (MagicAvgDamage). 45 bytes, read whole. Called by Formula_95_NanoflareReDispatchesToF30 (ids 30, 94, 95) and sub_140309310 (96). Crosscheck: Y (block +0x2E) is the byte at 0x1407B079E, byte 14 of the 16-byte item at 0x1407B0790, a RIP-relative operand.

## Open questions

None recorded.
