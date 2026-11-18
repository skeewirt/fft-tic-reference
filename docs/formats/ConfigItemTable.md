# ConfigItemTable

- **Kind:** file format
- **Extension:** `.nxd`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Read by:** [ConfigMenu_ShowTab](../functions/ConfigMenu_ShowTab.md), [ConfigMenu_DrawRowValue](../functions/ConfigMenu_DrawRowValue.md), [ConfigMenu_SetHelpText](../functions/ConfigMenu_SetHelpText.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

`configitem.nxd` (nxd 250): one row per setting of the settings screens. The screen's code names which row ids it lists (0..27, 30..33, 39, 46..56); a row it does not name is never listed.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="nametextid"></a>56 | NameTextId | `int32` | V | The row's name text id. |
| <a id="descriptiontextuiid"></a>64 | DescriptionTextUIId | `int32` | V | The help text id used in mode 1 (the mode select's screen). |
| <a id="unknown44"></a>68 | Unknown44 | `int32` | V | The help text id used in mode 0 (in game). |
| <a id="mode1_flag"></a>72 | mode1_flag | `uint8` | V | In mode 1 only rows with this byte set are listed. |
| <a id="unknown4 (row type)"></a>0 | Unknown4 (row type) | `int32` | V | 1 a value with arrows (Select), 2 a slider, 3 an On / Off switch (Swich), 4 a value from a list (SelectList), 5 a key to press (UIDialog 232). Offset is not read; the column name is. Checked against stock rows: 13 Horizontal Camera Inversion = 3, 7 Master Volume = 2, 0 Display Mode = 1, 46 Confirm = 5. |

## Behavior

- V: read in event 0x1E of UIAddonFFTOConfig_OnEvent, ConfigMenu_DrawRowValue and ConfigMenu_SetHelpText.

## Open questions

None recorded.
