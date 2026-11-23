# MenuCtl_Entry44

- **Address:** `0x1403193CC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MenuCtl_Entry44(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 44)
- **Callees:** sub_1402BC388, sub_1403793DC, SceneVar_Write, SceneVar_Read, HelpMessage_Open

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a list of 7 flagged entries opened from index 43 (table index 44): confirm marks the entry as seen and starts the scene for it.

## Behavior

- V: sub_140319218 builds the list: 7 rows, a row is shown with flag 8 when its bit of the dword array at 0x141D33024 is set.
- V: browse: cancel starts the close (record dword 0 = 0), confirm (only when the list has rows, dword 12 nonzero) sets dword 0 to 1 and starts the close; the help action opens HelpMessage_Open(4235).
- V: after the close with dword 0 = 2 it sets the chosen bit in the array, loads a scene (sub_1402BC388 with index + 1), picks one of four state tables by the language (tbl_LegacyWorldMenuStateLang0 to 3), toggles masks 0x44 of the state dword, pops and pushes kind 49 through sub_1403793DC(44, 0, 0).
- V: after the close with dword 0 = 1 it stores the picked row in 0x140D49690, writes 0 and then back the scene variable 508 and sets scene variable 100 to 0; with dword 0 = 0 it pops and re-opens the screen below.

## State touched

- Calls: [sub_1403793DC](sub_1403793DC.md), [SceneVar_Write](SceneVar_Write.md), [SceneVar_Read](SceneVar_Read.md), [HelpMessage_Open](HelpMessage_Open.md)

## Notes

Index 45 has the same layout over a second flag array.

## Open questions

? what the seven scenes are. I: the list looks like a scene list, opened from a menu of index 43.
