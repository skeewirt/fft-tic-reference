# TavernRumourPage_Show

- **Address:** `0x1401A041C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void TavernRumourPage_Show(void *page, int id)`
- **Callers:** not recorded
- **Callees:** sub_14019EF74, sub_1400FC1C0, UITable_GetRowByKey, GUINode_PlayShowHide

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows a rumour's text and picture.

## Behavior

- V: the text goes through sub_14019EF74(title, text); 'ShowImage' / 'Default' by (counter (+4) and counter_value (+8) both non-zero).
- V: the picture is the Icon row 21 pattern ('base/textureparts/base_%02d_uitx') filled with picture (+0x28); panel +1044 = 1 + shown; panel +1048 = 1.0f while the situation counter of +4 is still below +8.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [GUINode_PlayShowHide](GUINode_PlayShowHide.md)

## Referenced by

- Observed behaviours: [RumourReadWritesEventVariables](../behaviors/RumourReadWritesEventVariables.md)

## Open questions

None recorded.
