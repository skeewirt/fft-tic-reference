# BookShelf_Fill

- **Address:** `0x140166E08`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BookShelf_Fill(void *shelf, const void *input)`
- **Callers:** not recorded
- **Callees:** GuiImage_SetIconById, GUINode_PlayState, sub_1401672A0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the five slots of the Reading Materials shelf.

## Behavior

- V: the input is {count; ids[5]; sort values[5]; bookmark bytes at +44}. A selection loop fills each slot with the unused book that has the smallest sort value (Book sort_order).
- V: each slot gets its title (+0x14) and icon (+0x10, GuiImage_SetIconById) and 'ShowBookmark' / 'HideBookmark' from its bookmark byte; it ends with panel +1408 = count and sub_1401672A0.

## State touched

- Calls: [GuiImage_SetIconById](GuiImage_SetIconById.md), [GUINode_PlayState](GUINode_PlayState.md)

## Open questions

None recorded.
