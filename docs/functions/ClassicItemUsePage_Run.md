# ClassicItemUsePage_Run

- **Address:** `0x1403934B0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int ClassicItemUsePage_Run(void)`
- **Callers:** sub_140393330
- **Callees:** Input_TestAction, Inventory_AddCount, SceneTask_Start, sub_140396FEC, sub_14033E30C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Legacy party menu item use page: picks an item and applies it to a unit.

## Behavior

- V: on confirm checks the item count with Inventory_AddCount; with a count of 0 shows an event message, otherwise applies the item to the unit and removes one from the inventory.
- V: runs the item page script of the text language inline (0x1408FCFB0 language 0, 0x1408FD760 language 3, 0x1408FD4D0 language 2, 0x1408FD240 otherwise): a loop that calls handler[opcode] of the 25-slot table at 0x1406932A0 until opcode 25; this is a second runner of the kind ClassicUi_RunLayoutScript implements.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [Inventory_AddCount](Inventory_AddCount.md), [SceneTask_Start](SceneTask_Start.md), [sub_140396FEC](sub_140396FEC.md)

## Referenced by

- Reads tables: [LegacyItemUseLayoutLang0](../tables/LegacyItemUseLayoutLang0.md), [LegacyItemUseLayoutLang1](../tables/LegacyItemUseLayoutLang1.md), [LegacyItemUseLayoutLang2](../tables/LegacyItemUseLayoutLang2.md), [LegacyItemUseLayoutLang3](../tables/LegacyItemUseLayoutLang3.md)
- Resolves registries: [ClassicItemScriptOpcodes](../registries/ClassicItemScriptOpcodes.md)

## Open questions

None recorded.
