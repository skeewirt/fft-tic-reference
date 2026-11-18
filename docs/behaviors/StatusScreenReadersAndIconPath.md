# StatusScreenReadersAndIconPath

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [StatusScreen_BuildLists](../functions/StatusScreen_BuildLists.md), [StatusScreen_DrawLists](../functions/StatusScreen_DrawLists.md), [StatusScreen_SetEntry](../functions/StatusScreen_SetEntry.md), [StatusScreen_SetCaption](../functions/StatusScreen_SetCaption.md), [Status_ListCategory](../functions/Status_ListCategory.md), [Status_ListSortKey](../functions/Status_ListSortKey.md), [UnitPanel_SetStatusBytes](../functions/UnitPanel_SetStatusBytes.md), [TurnPanel_FillUnitEntry](../functions/TurnPanel_FillUnitEntry.md), [BattleUnit_SetStatusVisual](../functions/BattleUnit_SetStatusVisual.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle Status screen lists a unit's statuses in two dword lists (gains, ailments) and reads each one's name, category, sort key and caption from its UIStatusEffect row (key id + 1); the icon path s_%03d is formatted with the status id.

## Behavior

- V (code read): the three UIStatusEffect readers refuse an id above 39 with one compare each.
- V (code read): the icon path s_%03d is formatted with the id.

## Open questions

None recorded.
