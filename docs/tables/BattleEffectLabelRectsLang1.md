# BattleEffectLabelRectsLang1

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x1407B3A40`
- **Rows:** 60 rows of 4 bytes
- **Keyed by:** label number 0..59
- **Row layout:** [EffectLabelRectRow](../structs/EffectLabelRectRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Texture rectangles of the effect label pictures for text language 1. Verdict: designer-data.

## Behavior

- V: the effect id (word +834 of the effect object, 9 bits) selects the label through compare chains in the readers
- V: four copies, one per text language: 0 at 0x1407B3770, 3 at 0x1407B3860, 2 at 0x1407B3950, 1 (default) at 0x1407B3A40

## Notes

Our names. Tags: V layout, I fields.

## Open questions

- ?: field meaning of the packed word
- ?: which label each number is
