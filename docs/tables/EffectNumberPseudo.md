# EffectNumberPseudo

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1406834B0`
- **Rows:** 37 rows of 2 bytes
- **Keyed by:** effect word 512..548
- **Read by:** [Effect_SelectForAbility](../functions/Effect_SelectForAbility.md)
- **Row layout:** [EffectNumberPseudoRow](../structs/EffectNumberPseudoRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Effect number per pseudo effect word. The per ability effect numbers are a different, already catalogued table (exe.ability.anim). Verdict: designer-data.

## Behavior

- V: Effect_SelectForAbility indexes it with (word - 512) when word >= 512, row 0 above row 36, and keeps the low 9 bits

## Notes

Our names. Tags: V layout, V reader, I meaning.

## Open questions

None recorded.
