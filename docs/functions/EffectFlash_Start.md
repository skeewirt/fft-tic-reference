# EffectFlash_Start

- **Address:** `0x140313F34`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `long EffectFlash_Start(void)`
- **Callers:** EffectSequence_Run (slot 4 of the effect sequence handler table (0x140682F30))
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sequence kind 4 handler: the screen flash effect that tints the view with an element colour.

## Behavior

- V: state 1 reads the effect kind from the entry (word +4) and the element mask (word +6); the kind's parameter word (EffectKindRecords, +2) picks a row of EffectFlashProfiles.
- V: the element mask is matched against ElementMaskOrder (nine masks) and replaced by the position of the first match, which later picks the tint of ElementColours (three bytes per slot).
- V: copies the seven profile words into the live flash state; the high byte of the last word picks a row of EffectBlendWeights, whose seven weights scale the tint (weight * colour >> 8) while the flash runs.
- I: later states animate the flash and write the scaled colours into the sprite colour records.

## Referenced by

- Reads tables: [EffectBlendWeights](../tables/EffectBlendWeights.md), [EffectFlashProfiles](../tables/EffectFlashProfiles.md), [EffectKindRecords](../tables/EffectKindRecords.md), [ElementColours](../tables/ElementColours.md), [ElementMaskOrder](../tables/ElementMaskOrder.md)

## Notes

Name is ours; the function is long (about 470 lines) and only the table reads were decoded.

## Open questions

?: the animation states after the set-up.
