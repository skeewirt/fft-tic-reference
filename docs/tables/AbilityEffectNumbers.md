# AbilityEffectNumbers

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140683500`
- **Rows:** 454 rows of 2 bytes
- **Keyed by:** ability id 0..453
- **Read by:** [Effect_SelectForAbility](../functions/Effect_SelectForAbility.md), [sub_140210AF0](../functions/sub_140210AF0.md)
- **Held in:** [g_AbilityEffectNumber](../globals/g_AbilityEffectNumber.md)
- **Row layout:** [AbilityEffectNumberRow](../structs/AbilityEffectNumberRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle effect number and flag of each ability.

## Behavior

- V: the effect selector takes the low 9 bits.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
