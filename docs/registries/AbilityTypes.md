# AbilityTypes

- **Kind:** registry
- **Area:** [Ability data](../areas/ability-data.md)
- **Values stored in:** [AbilityAuxFlagBits](AbilityAuxFlagBits.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The ability type nibble in the low five bits of AbilityAux flags3, with names.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="none"></a>0 | `None` | `flags3 & 0x1F = 0` | V | Empty / dummy rows and the passive rows without a type. |
| <a id="normal"></a>1 | `Normal` | `1` | V | Ordinary abilities (the learned command abilities). |
| <a id="item"></a>2 | `Item` | `2` | V | Item use. |
| <a id="throwing"></a>3 | `Throwing` | `3` | V | Throw. |
| <a id="jumping"></a>4 | `Jumping` | `4` | V | Jump. |
| <a id="aim"></a>5 | `Aim` | `5` | V | Charge / aim. |
| <a id="math"></a>6 | `Math` | `6` | V | Math skill. |
| <a id="reaction"></a>7 | `Reaction` | `7` | V | Reaction ability. |
| <a id="support"></a>8 | `Support` | `8` | V | Support ability. |
| <a id="movement"></a>9 | `Movement` | `9` | V | Movement ability. |

## Behavior

- V: solved over the 512 stock rows: the type name of each row equals flags3 & 0x1F for every row.

## Referenced by

- Indexed by registries: [AbilityAuxFlagBits](AbilityAuxFlagBits.md)

## Open questions

None recorded.
