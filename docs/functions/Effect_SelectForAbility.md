# Effect_SelectForAbility

- **Address:** `0x140319B50`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Effect_SelectForAbility(uint32 chargeElement, int effectWord, void *request)`
- **Callers:** BattleAct_SetupEffect, EventEffect_Start (event effects), sub_140318090 (0xDB / 0xDC)
- **Callees:** sub_140310B64

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Picks the effect number for an effect word and starts the effect.

## Behavior

- V: word >= 512: g_EffectNumberPseudo[word - 512] (37 rows, else row 0): the effects of event scripts (EventEffect_Start); word 393: by the weapon's element bits (16, 24, 20 or the current); else g_AbilityEffectNumber[word < 0x1C6 ? word : 0].
- V (2026-11-16): the compare with 512 is signed (a signed greater-or-equal jump, at 0x140319B8B), so a negative word (a 16-bit value with its top bit set, 0x8000 and above, is negative as an int) takes the last branch and row 0 of the ability table; the pseudo row bound is a compare of the row counter with an 8-bit immediate (37) followed by a subtract-with-borrow and an AND, so a word 549 or more reads row 0. The row is a 16-bit value: a negative one (bit 15) means no effect. The charge element argument is used as a 16-bit index (the 0xFFFF mask of the charge table read is a 16-bit register move at 0x140319C35, so the constant 0xFFFF is not in the body).
- V: a number >= 0 is stored in word_141D330BC and the effect starts (sub_140310B64 with byte_140682B98[chargeElement & 0xFFFF]); a negative one (-1: none) only runs the special cases of 138..145 and 146 / 406..413; dword_142E801F4 = word.
- V (2026-11-12): the stored number is masked with 0x1FF (0x140319C23 / 0x140319C32) after the sign test; the g_AbilityEffectNumber row is loaded into eax at 0x140319BF1 (zero-extended, indexed from rdi = the image base), and a jump then reaches the store at 0x140319C13.

## Referenced by

- Called by: [BattleAct_SetupEffect](BattleAct_SetupEffect.md), [EventEffect_Start](EventEffect_Start.md)
- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md), [PseudoEffectWordIsASixteenBitEventOperand](../behaviors/PseudoEffectWordIsASixteenBitEventOperand.md)
- Reads tables: [AbilityEffectNumbers](../tables/AbilityEffectNumbers.md), [EffectNumberPseudo](../tables/EffectNumberPseudo.md)

## Notes

An effect word of 512..548 selects a pseudo effect here; the highest word an event script can pass is 32,767 (the operand is a signed 16-bit word).

## Open questions

None recorded.
