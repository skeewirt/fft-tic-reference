# GUIComponent_Init

- **Address:** `0x140408E78`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIComponent_Init(GUIComponentCustom *c, void *def)`
- **Callers:** GUIComponentCustom_Create
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initializes a component from its definition; copies the component object id (+8) into the layer node (+0x140).

## Behavior

- V: contains a store at 0x1404089E3 that copies the dword at +8 of the object (loaded into a register a few instructions earlier) into the dword at +0x140 of the same object - the write that gave the component root its object id (caught by hardware watch).

## Referenced by

- Called by: [GUIComponentCustom_Create](GUIComponentCustom_Create.md)

## Notes

Object ids are unique runtime ids: stock tree components got ids 4754..4934 (step 10), the extra got 4964. They are NOT sprite part ids.

## Open questions

None recorded.
