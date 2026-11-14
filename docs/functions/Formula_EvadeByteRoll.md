# Formula_EvadeByteRoll

- **Address:** `0x140305130`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_EvadeByteRoll(uint16_t evade, uint16_t baseline, char reason)`
- **Callers:** Formula_EvadeRoll
- **Callees:** Rng_Percent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One evade roll of Formula_EvadeRoll: a failed hit stores the miss reason.

## Behavior

- V: Rng_Percent(baseline, evade) true (the evade roll won) or g_BattleSimulating != 0 returns 0 with no change.
- V: otherwise R+0 = 0, R+2 = reason (1..4 by the evade byte) and R+4 is stored from a register the decompile lost; returns 1.

## State touched

- Calls: [Rng_Percent](Rng_Percent.md)

## Referenced by

- Called by: [Formula_EvadeRoll](Formula_EvadeRoll.md)

## Notes

Source: helper of block B03. 71 bytes, read whole.

## Open questions

? what R+4 receives here (a register the caller leaves in r11).
