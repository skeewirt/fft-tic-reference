# BattleMenu_ConfirmRow

- **Address:** `0x140237B18`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleMenu_ConfirmRow(int rowId, short arg, int mode)`
- **Callers:** one call site (in the function IDA names __ld12mul_0) and two data references
- **Callees:** SceneTask_Start, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Acts on a confirmed battle command menu row: picks the follow-up screen code and starts the scene task that shows it.

## Behavior

- V: in the mode read here the code is 0x1000 plus the row's byte in the menu row screen-code table (0x140672170); three unit states replace it with fixed codes (0x1003, 0x1007, 0x100C).
- V: the code is stored at +0xC24 of the current scene block and a scene task is started on the previous task slot to run it.
- V: mode 3 builds the code from the second argument instead; other rows fall back to a per-command-kind word table (0x140809920).

## State touched

- Calls: [SceneTask_Start](SceneTask_Start.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Reads tables: [BattleMenuRowScreenCodes](../tables/BattleMenuRowScreenCodes.md)

## Notes

Read: the row-confirm branch and the fallback; the special-state tests only as far as their codes.

## Open questions

?: which row id is which command; what each 0x10xx code opens.
