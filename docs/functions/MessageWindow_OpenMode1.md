# MessageWindow_OpenMode1

- **Address:** `0x1402E09DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 MessageWindow_OpenMode1(void)`
- **Callers:** not recorded
- **Callees:** sub_140305264, Battle_ExecuteSecondaryAction, sub_1402DF374

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the legacy unit info message window for the acting unit with the hit chance, after a preview of the action (mode 1).

## Behavior

- V: finds the actor and target units (preview unit table, 512 bytes per unit), runs the damage and result calculation sub_140305264 and, when the action is not a plain secondary action, starts it (task function Battle_ExecuteSecondaryAction).
- V: waits two frames, refreshes the preview buffers, clamps the predicted hit points and MP against each unit's maxima and stores them in the window widgets.
- V: finally calls the panel window builder with mode 1, the eight-row number table 0x1408E52D0 and the actor preview buffer.

## State touched

- Calls: [sub_1402DF374](sub_1402DF374.md)

## Referenced by

- Reads tables: [UnitStatusNumbersMode1](../tables/UnitStatusNumbersMode1.md)

## Notes

Read in full; the preview arithmetic is only summarised.

## Open questions

?: what the two stored widget words are.
