# SpriteLookupFailuresPastTheTables

- **Kind:** observed behaviour
- **Scope:** engine (sprite readers)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_CollectJobSkillsets](../functions/Unit_CollectJobSkillsets.md), [sub_140300D74](../functions/sub_140300D74.md), [NxdEntry_GetRow](../functions/NxdEntry_GetRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What went wrong in game when a sprite number or job id above the stock range reached a reader: three failures.

## Behavior

- I (reported from play): a sprite number of 0xAA or more in the battle map's unit queue builder (sub_1403041A4, bound at 0x140304207) drew the unit as sprite 1 (the main character).
- I: the sprite row table of the NXD table 0xAE (looked up with the sprite as key, 15 callers) has no rows above 169; the formation code in sub_140216EB4 read the row's byte at +0x2C from a null row (0x140217172) and crashed placing a unit of sprite 212.
- I: a job id at or above the guard of the job menu list (the immediate 0xAE at 0x140286759, 0x140286803) took the null-row fallback and crashed when the second job page opened (access violation at 0x140286826). The guard at 0x140286759 is in Unit_CollectJobSkillsets, not in a list builder.
- I: the battle read of a story-character code crash is described under UnitFaceFromSpriteNumber.

## Open questions

None recorded.
