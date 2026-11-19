# Guide_OpenWindow

- **Address:** `0x1401A9000`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Guide_OpenWindow(int id)`
- **Callers:** not recorded
- **Callees:** sub_1401A6AFC, sub_1401A7C14, UITable_GetRowByKey, UIAddon_LoadByRow, PauseManager_Push

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the window that shows a guide.

## Behavior

- V: picks the add-on by window_type (+8): 1 = the guide window of UI row 181 (sub_1401A6AFC), 2 = UI row 182 (sub_1401A7C14) (both pause the game), 3 = GuideTip (UI row 184).
- V: stores the guide id at add-on +3968 / +3680 / +256; sets agent +152 = add-on +32 and +156 = 1.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [UIAddon_LoadByRow](UIAddon_LoadByRow.md), [PauseManager_Push](PauseManager_Push.md)

## Referenced by

- Observed behaviours: [GuideListsAndAutoShowRule](../behaviors/GuideListsAndAutoShowRule.md)

## Open questions

None recorded.
