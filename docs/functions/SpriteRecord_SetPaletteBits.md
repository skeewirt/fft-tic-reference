# SpriteRecord_SetPaletteBits

- **Address:** `0x1400FB328`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `int SpriteRecord_SetPaletteBits(SpriteRecord *r, int a2, int a3, char a4)`
- **Callers:** JobTree_SetPanelRecord, sub_1400FB038
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets frame/palette flag bits at record+12 and the selected palette index at +24 from small tables (word_140672CF8/D7A/D98).

## Behavior

- V: a3 == 4 selects the table entry by (a2 % 4).

## Referenced by

- Called by: [JobTree_SetPanelRecord](JobTree_SetPanelRecord.md), [sub_140132DC8](sub_140132DC8.md), [sub_140132E1C](sub_140132E1C.md)

## Open questions

None recorded.
