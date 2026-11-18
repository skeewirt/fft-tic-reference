# ButtonIcon_Draw

- **Address:** `0x1402BE284`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `long ButtonIcon_Draw(short group, short x, short y, short pressed, short disabled, char flag)`
- **Callers:** the button prompt row drawer sub_14037AE7C (and a second user)
- **Callees:** sprite queue routine sub_14031DBE4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one animated button icon: the sprite pieces of an icon group with a press animation.

## Behavior

- V: keeps a press step per icon group (0..6): disabled resets it to 0, pressed sets it to 1, a running step 1..5 advances by one each call, then it falls back to 0.
- V: the piece range of the group is [start[group], start[group + 1]) from the group start list of the current text language; the pieces come from the piece table and the scale pairs from the scale table of the same language (0 uses its own tables with 81 pieces, 1 / 2 / 3 use 80 pieces).
- V: per piece: draw size = |size * scale| >> 12 (a horizontal scale above 4100 adds 2 pixels), source rectangle from the piece, position = icon position + piece offsets, mirror bits from the sign of the scales; the piece is queued with the sprite queue routine.
- I: the step selects the texture page words that show the pressed look (three page values are used).

## Referenced by

- Reads tables: [LegacyButtonIconGroupStartsLang0](../tables/LegacyButtonIconGroupStartsLang0.md), [LegacyButtonIconGroupStartsLang1](../tables/LegacyButtonIconGroupStartsLang1.md), [LegacyButtonIconPiecesLang0](../tables/LegacyButtonIconPiecesLang0.md), [LegacyButtonIconPiecesLang1](../tables/LegacyButtonIconPiecesLang1.md), [LegacyButtonIconPiecesLang2](../tables/LegacyButtonIconPiecesLang2.md), [LegacyButtonIconPiecesLang3](../tables/LegacyButtonIconPiecesLang3.md), [LegacyButtonIconScalesLang0](../tables/LegacyButtonIconScalesLang0.md), [LegacyButtonIconScalesLang1](../tables/LegacyButtonIconScalesLang1.md)

## Notes

Name is ours. The group start, piece and scale tables are also read by sub_1402FAFC8 and sub_14033B7E8.

## Open questions

?: which prompt each of the 14 groups is.
