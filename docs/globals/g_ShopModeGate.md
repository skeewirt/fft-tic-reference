# g_ShopModeGate

- **Kind:** global
- **Address:** `0x1407D453C`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Global mode word that gates the shop and den badge refresh; the badge routine runs only while it is non-zero.

## Behavior

- ?: what the mode word selects; the sheet leaves it open.

## Referenced by

- Read by: [BattleControl_FrameUpdate](../functions/BattleControl_FrameUpdate.md), [EventControl_Update](../functions/EventControl_Update.md), [Game_MainLoop](../functions/Game_MainLoop.md), [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md), [OpeningMenu_Task](../functions/OpeningMenu_Task.md), [OpeningScene_Start](../functions/OpeningScene_Start.md), [OpeningTask_4](../functions/OpeningTask_4.md), [sub_140346524](../functions/sub_140346524.md)

## Open questions

None recorded.
