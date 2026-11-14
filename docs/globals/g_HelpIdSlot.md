# g_HelpIdSlot

- **Kind:** global
- **Address:** `0x1418736B4`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `int32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The item help-id slot of the shop detail panel: 0x6800 plus the per-item help word when the table word is non-zero, -1 when the item has no help.

## Behavior

- V: sub_1403343E4 reads the per-item word table at 0x3D1ADD8 and stores the token or -1 here.

## Referenced by

- Read by: [EventScene_QueueHelpText](../functions/EventScene_QueueHelpText.md), [Shop_Open](../functions/Shop_Open.md), [UI_GetHelpSlotState](../functions/UI_GetHelpSlotState.md)
- Written by: [sub_1403343E4](../functions/sub_1403343E4.md)

## Open questions

None recorded.
