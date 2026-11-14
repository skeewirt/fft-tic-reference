# g_SelectedUnitIndex

- **Kind:** global
- **Address:** `0x141811428`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint16`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The selected unit index the item, shop and equip screens read as their unit argument (sub_140287D9C, sub_1402D7640, sub_1403331F8, sub_140333FE0, sub_140366FE0).

## Behavior

- V: sub_140287D9C and sub_1402D7640 take the unit from this word rather than from their arguments.

## Referenced by

- Read by: [EventScene_QueueHelpText](../functions/EventScene_QueueHelpText.md), [JobScreen_BuildAbilityTabList](../functions/JobScreen_BuildAbilityTabList.md), [JobScreen_FillUnitRows](../functions/JobScreen_FillUnitRows.md), [sub_140287D9C](../functions/sub_140287D9C.md), [sub_1402D7640](../functions/sub_1402D7640.md), [sub_1403331F8](../functions/sub_1403331F8.md), [sub_140333FE0](../functions/sub_140333FE0.md), [sub_140338250](../functions/sub_140338250.md), [sub_140366FE0](../functions/sub_140366FE0.md)

## Open questions

None recorded.
