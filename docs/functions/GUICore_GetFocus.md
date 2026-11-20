# GUICore_GetFocus

- **Address:** `0x1403D6E28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUICore_GetFocus(GUICore *core, __int64 *outWidget, __int64 *outNode)`
- **Callers:** GUICursorHand_Update, GUICursorHand_GetTargetPoint, GUICore_FocusNode and others
- **Callees:** GUICore_FindWidgetByKey, sub_1403F9938

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves the focus key triple (core+1968) to the live widget and node; returns 0 when nothing is focused.

## Behavior

- V: widget = GUICore_FindWidgetByKey(core, core+1968); node = sub_1403F9938(widget, core+2000, core+1984, 0); both are written to the out parameters. The returned node is the panel's reference node for the job tree (live: Mystic = kind 12, pos (1220,485), size 64x80).

## State touched

- Calls: [GUICore_FindWidgetByKey](GUICore_FindWidgetByKey.md)

## Referenced by

- Called by: [GUIComponentCustom_CursorEnter](GUIComponentCustom_CursorEnter.md), [GUIComponent_CursorLeave](GUIComponent_CursorLeave.md), [GUICore_FocusNode](GUICore_FocusNode.md)
- Observed behaviours: [BattleCommandMenuStates](../behaviors/BattleCommandMenuStates.md), [BattleHudAndUnitFields](../behaviors/BattleHudAndUnitFields.md), [BattleTextOverlaysAndPreview](../behaviors/BattleTextOverlaysAndPreview.md), [JobsEquipmentShopScreens](../behaviors/JobsEquipmentShopScreens.md), [TitleAndSaveListScreens](../behaviors/TitleAndSaveListScreens.md), [WorldMapLocationsAndBattleEntry](../behaviors/WorldMapLocationsAndBattleEntry.md)

## Notes

Live read: widget = the ffto_job_tree.uib widget, node screen rect (1220, 517, 1284, 597), so the hand target is (left, centre y) = (1220, 557).

## Open questions

None recorded.
