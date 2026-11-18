# EffectKindRecords

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140682FF0`
- **Rows:** 22 rows of 4 bytes
- **Keyed by:** effect kind id 0..21
- **Read by:** [EffectFlash_Start](../functions/EffectFlash_Start.md), [EffectPalette_Step](../functions/EffectPalette_Step.md)
- **Row layout:** [EffectKindRecordsRow](../structs/EffectKindRecordsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row per effect kind: the sequence handler kind that runs it and a parameter word. Verdict: designer-data.

## Behavior

- V: the first byte is copied into the high byte of a new sequence entry, which EffectSequence_Run later uses as the handler index
- V: EffectFlash_Start and EffectPalette_Step read the word at +2 (word at 0x140682FF2 + 4 * kind)

## Notes

Our names. Tags: V layout, V kind byte use, I param meaning.

## Open questions

- ?: what the 22 kinds are in play
- ?: the exact use of the parameter word for each kind
