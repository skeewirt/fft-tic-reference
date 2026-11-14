# sub_14022AFEC

- **Address:** `0x14022AFEC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `?`
- **Callers:** none found (reached indirectly)
- **Callees:** ItemIcon_Set, sub_140243330, sub_1402378C8, sub_1402346D0, sub_14025FA60, sub_140242AFC, sub_14021F820

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds an item list screen: it initialises the screen-state record selected by a global screen index and fills the list cells with icons and text ids.

## Behavior

- V: the per-screen state record is selected from a global screen index with a 0x800-byte stride (the stride is a left shift by 11); a 21 (0x15) marker and a state value are written at the start.
- V: the function walks a 0xFFFF-terminated word list and, for each entry, posts a text id equal to 0x3800 plus the entry through the text command at sub_140243330.
- V: the item icon is set through ItemIcon_Set (0x14022A9E4) and the list row is filled through the row helpers around sub_1402378C8 and sub_1402346D0.
- V: the screen state is set before and after the list loop, and a global word is set to 1 at the start.
- V: the function has no direct caller, which fits a screen constructor stored in a table.
- I: the screen is one of the shop or equipment item lists; the 0x15 marker is a screen or task id.
- ?: which screen, where the word list comes from, and what the marker means.

## State touched

- Calls: [ItemIcon_Set](ItemIcon_Set.md), [sub_140243330](sub_140243330.md), [sub_140242AFC](sub_140242AFC.md)

## Notes

- V: read the constructor prologue and the list loop, as part of the item text research.
- V: the twin function sub_1402E1C64 has the same shape and a different state table.

## Open questions

- ?: which screen this is (buy, sell, inventory or equip).
- ?: the source and lifetime of the word list.
