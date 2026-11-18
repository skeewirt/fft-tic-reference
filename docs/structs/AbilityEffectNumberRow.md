# AbilityEffectNumberRow

- **Kind:** structure
- **Area:** [Ability data](../areas/ability-data.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Effect word of one ability.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="effect_word"></a>`0x0` | effect_word | `int16` | V | -1 = no effect file (Throw Stone is a projectile); low 9 bits = effect number loaded by the effect selector; bit 11 (0x800) is a flag one reader tests. |

## Referenced by

- Described by tables: [AbilityEffectNumbers](../tables/AbilityEffectNumbers.md)

## Open questions

None recorded.
