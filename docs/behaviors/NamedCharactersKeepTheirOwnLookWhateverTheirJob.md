# NamedCharactersKeepTheirOwnLookWhateverTheirJob

- **Kind:** observed behaviour
- **Scope:** engine (unit look by character byte)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_ResolvePreviewShape](../functions/Unit_ResolvePreviewShape.md), [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A named character (character byte +0 of the save, party or battle record below 0x80, e.g. Ramza 0x01) keeps its own sprite and portrait whatever job it holds; Ramza's change with the chapter. A generic unit (0x80 male, 0x81 female) is drawn with its job's look, the male or female version by that byte.

## Behavior

- V (owner, game knowledge 2026-11-17): named characters do not change model or portrait with the job; Ramza's changes with the chapter.
- V (seen live 2026-11-17): in battle, with Knight (76) in his job byte, Ramza's figure on the battle Status screen was his blue Chapter 1 sprite; the generic units of the party drew their jobs' sprites on the Change Job grid.
- I: the shape resolvers read the character byte before the job (a byte below 0x80 selects the character's own shape row).

## Open questions

None recorded.
