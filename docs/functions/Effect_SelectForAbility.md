# Effect_SelectForAbility

- **Address:** `0x140319B50`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Effect_SelectForAbility(uint32 chargeElement, int effectWord, void *request)`
- **Callers:** BattleAct_SetupEffect, sub_140273708 (event effects), sub_140318090 (0xDB / 0xDC)
- **Callees:** sub_140310B64

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Picks the effect number for an effect word and starts the effect.

## Behavior

- V: word >= 512: g_EffectNumberPseudo[word - 512] (37 rows, else row 0): the effects of event scripts (sub_140273708); word 393: by the weapon's element bits (16, 24, 20 or the current); else g_AbilityEffectNumber[word < 0x1C6 ? word : 0].
- V: a number >= 0 is stored in word_141D330BC and the effect starts (sub_140310B64 with byte_140682B98[chargeElement & 0xFFFF]); a negative one (-1: none) only runs the special cases of 138..145 and 146 / 406..413; dword_142E801F4 = word.
- V (2026-11-12): the stored number is masked with 0x1FF (0x140319C23 / 0x140319C32) after the sign test; the g_AbilityEffectNumber row is loaded into eax at 0x140319BF1 (zero-extended, indexed from rdi = the image base), and a jump then reaches the store at 0x140319C13.

## Referenced by

- Called by: [BattleAct_SetupEffect](BattleAct_SetupEffect.md)
- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)

## Notes

An effect word of 512 or more selects one of the pseudo effects (512..548) here.

## Open questions

None recorded.
