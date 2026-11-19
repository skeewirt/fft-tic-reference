# ClearMarkAppearsOnFourScreens

- **Kind:** observed behaviour
- **Scope:** engine (Zodiac Stone, Events, Chronicle period, glossary)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [ZodiacStone_FillDetail](../functions/ZodiacStone_FillDetail.md), [JournalDetail_Fill](../functions/JournalDetail_Fill.md), [GlossaryDetail_Fill](../functions/GlossaryDetail_Fill.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Four tables carry a one-byte clear_mark column; each shows a node 'Clear' that plays 'Enable' when the byte is set and 'Disable' otherwise.

## Behavior

- V: ZodiacStone clear_mark (+0x24, sub_14016E218), Journal clear_mark (+0x25, sub_14016B49C), LoreDictionary clear_mark (+0x4F, sub_140172B70 and sub_140177004), UIChroniclePeriod clear_mark (+0x24, sub_140176758; the node at +224 is bound in sub_140174878).
- V: every set row is a late-story row.

## Open questions

? what the mark looks like on screen (not seen).
