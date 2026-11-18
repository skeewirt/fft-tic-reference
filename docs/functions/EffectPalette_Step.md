# EffectPalette_Step

- **Address:** `0x140315620`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectPalette_Step(void)`
- **Callers:** EffectSequence_Run (slot 18 of exe.battle.effect_sequence_handlers)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 18 handler: a full screen palette effect that starts from six seed colours.

## Behavior

- V: state 1 clears the effect's sprite records and writes the six 5-bit RGB seed colours of exe.battle.effect_palette_seeds, packed into 15-bit colour words, twice into the live palette (12 words).
- V: state 2 steps the palette using words of the entry; the kind's parameter word is read from exe.battle.effect_kind_records (+2).
- ?: the states after the first were not decoded.

## Referenced by

- Reads tables: [EffectKindRecords](../tables/EffectKindRecords.md), [EffectPaletteSeeds](../tables/EffectPaletteSeeds.md)

## Notes

Name is ours.

## Open questions

None recorded.
