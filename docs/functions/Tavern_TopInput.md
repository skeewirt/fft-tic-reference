# Tavern_TopInput

- **Address:** `0x1402D5210`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void Tavern_TopInput(int *state)`
- **Callers:** sub_140246078
- **Callees:** sub_1402D50E4, Input_TestAction, sub_1402D541C, sub_1402CD714, sub_14034004C, sub_14019DF88, sub_14019DCD4, sub_1402D5068, Errand_BuildBoard, sub_14036EE50

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The tavern top screen's input step: rumors, errands, or leave.

## Behavior

- V: reads the widget's request (sub_14019DF88): 2 opens the rumors (sub_14036EE50), 4 builds the errand board (Errand_BuildBoard), 1 / 5 / 0x1A set screen states.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [sub_14034004C](sub_14034004C.md), [Errand_BuildBoard](Errand_BuildBoard.md), [sub_14036EE50](sub_14036EE50.md)

## Notes

Name is ours (was sub_1402D5210).

## Open questions

None recorded.
