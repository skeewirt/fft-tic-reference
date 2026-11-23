# ClassicMenu_HubStep

- **Address:** `0x14036D314`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ClassicMenu_HubStep(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 1; also pushed by sub_14036D21C)
- **Callees:** EventVarEditor_Open, sub_1403793DC, sub_14034637C, EventVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of the controller that sits under the other screens (table index 1): after a screen closes it decides, from flag masks of the state dword, which screen opens next.

## Behavior

- V: mask 0x8 of the state dword (a fade) makes it wait; its first record dword counts down from 3 before it acts.
- V: once the windows of rows 4 to 8 of the window object are idle it pops itself and checks the masks in this order: 0x100 opens kind 28, 0x4000 re-enters the town view, 0x100000 opens kind 43, 0x800000 opens the event variable editor (EventVarEditor_Open), 0x1000000 opens kind 52; with 0x10000 it reloads the scene variables.
- V: with none of those masks it calls WorldMenu_RunTopOpenHook to re-open the screen below.

## State touched

- Calls: [EventVarEditor_Open](EventVarEditor_Open.md), [sub_1403793DC](sub_1403793DC.md), [EventVar_Read](EventVar_Read.md)

## Open questions

? which game action sets each mask (the screens that close set them).
