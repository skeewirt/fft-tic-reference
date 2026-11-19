# InputModule_Init

- **Address:** `0x1400F159C`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void InputModule_Init(void *inputModule)`
- **Callers:** sub_1400E1D30
- **Callees:** sub_14001C958, memset, Mem_Alloc

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Initialises the UI input module, among other fields its context mask.

## Behavior

- V: writes the context mask at input module +13720 = 0x15 (contexts 1, 4 and 16); nothing else in the image writes it.
- V: with UIKeyAssign context_2 and context_4 (read by Input_UpdateActionRow, not here) a row's mask is 2 / 4 (1 when both are 0): context 2 is never active, context 4 is.

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md)
- Writes: [InputModule.context_mask](../structs/InputModule.md#context_mask)

## Referenced by

- Appears in flows: [InputBindingBuild](../flows/InputBindingBuild.md)

## Notes

Name is ours; only the context mask was read closely.

## Open questions

? the other fields it initialises.
