# ZodiacStoneBoardShowsStonesByHeldState

- **Kind:** observed behaviour
- **Scope:** engine (Zodiac Stone screen)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [ZodiacStoneBoard_Setup](../functions/ZodiacStoneBoard_Setup.md), [ZodiacStone_FillTip](../functions/ZodiacStone_FillTip.md), [ZodiacStone_FillDetail](../functions/ZodiacStone_FillDetail.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Each of the 13 stones shows the row with the highest second key whose user_situation is met; the owner-timeline column decides whether the stone is shown held, or as not yet acquired with the owner's portrait state.

## Behavior

- V: a stone with no met row is hidden ('HideStone').
- V: zodiac_stone_owner_timeline 0 plays 'ShowStone' (held); a non-zero value plays 'ShowUnacquired', and a value other than 1 first plays the state named by the ZodiacStoneOwnerTimeline row of that id (the 'Show<owner>' portrait states).
- V: name and description of a row fall back to the stone's first row (n, 0) when the chosen row's string is empty.

## Open questions

? the reader of ZodiacStoneOwnerTimeline +0xC (the 'Hide<owner>' state names).
