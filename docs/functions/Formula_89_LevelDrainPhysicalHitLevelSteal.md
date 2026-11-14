# Formula_89_LevelDrainPhysicalHitLevelSteal

- **Address:** `0x14030918C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_89(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 89

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Level Drain: a magic hit that sets the level-drain flag.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 75 bytes.
- V: Typical abilities: Level Drain.
- V: The earlier sheet called this physical; the hit chain is magic.

## Calculation

```text
Magic hit check (MA + X chain)
If target level <= 1: miss
On success: attack-type flags = 256 (level drain)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
