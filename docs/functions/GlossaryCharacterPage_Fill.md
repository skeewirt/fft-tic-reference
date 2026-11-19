# GlossaryCharacterPage_Fill

- **Address:** `0x140177004`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GlossaryCharacterPage_Fill(void *page, ...)`
- **Callers:** not recorded
- **Callees:** SpriteRecord_Fill, FaceWidget_SetFace, LoreDictionary_GetFaceByPair

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the glossary's character page, whose entry comes through a pair of table 283.

## Behavior

- V: looks the glossary row up through the table 283 pair; sets the sprite flag 0x8000000 when the pair's +8 is 4800; reads family_name_first (+0x40) and the figure columns through the pair getters.

## State touched

- Calls: [SpriteRecord_Fill](SpriteRecord_Fill.md), [FaceWidget_SetFace](FaceWidget_SetFace.md), [LoreDictionary_GetFaceByPair](LoreDictionary_GetFaceByPair.md)

## Notes

Named from the screen it fills; the body was read only for these uses.

## Open questions

? the rest of the page.
