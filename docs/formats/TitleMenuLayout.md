# TitleMenuLayout

- **Kind:** file format
- **Extension:** `.uib`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Read by:** [UITitleMenu_BindNodes](../functions/UITitleMenu_BindNodes.md), [TitleMenu_Build](../functions/TitleMenu_Build.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

`ui/ffto/title/ffto_title_enhanced.uib` (pack 0008), the layout of the Enhanced title menu: nine components, of which `Menu` carries the row layouts the add-on plays by name.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="homeposition"></a>24780 | HomePosition | `timeline (0x60 bytes)` | V | Menu timeline 0. |
| <a id="show"></a>24876 | Show | `timeline (0x60 bytes)` | V | Menu timeline 1. |
| <a id="hide"></a>24972 | Hide | `timeline (0x60 bytes)` | V | Menu timeline 2. |
| <a id="menu3"></a>25068 | Menu3 | `timeline (0x60 bytes)` | V | Layout for three rows; no y keys were found. |
| <a id="menu4"></a>25164 | Menu4 | `timeline (0x60 bytes)` | V | Layout for four rows: y offsets 16, 66, 116, 166 (50 px apart; 222 for the two hidden rows). |
| <a id="menu5"></a>25260 | Menu5 | `timeline (0x60 bytes)` | V | Layout for five rows: y 4, 48, 92, 136, 180 (44 px apart). |
| <a id="menu6"></a>25356 | Menu6 | `timeline (0x60 bytes)` | V | Layout for six rows: y -24, 20, 64, 108, 152, 196 (44 px apart). |

## Behavior

- V: the file has 9 components: Version, MenuButtonGlow, MenuButton (Layer00 with a Glow reference, text node `Title`, `Collision00`, and 8 timelines among them CursorOver, CursorOut, Enable, Disable, Down, Click), Menu (layer `LayerButton` with six references `MenuButton01` to `MenuButton06`), Copyright, Logo, BG, TitleEnhanced (the root layer, referencing Menu at (872, 770), Logo, Version, Copyright and BG) and Widget.
- V: the Menu component has 7 timelines, each a 0x60-byte record whose first dword is the offset of its name from the record; the dword pairs at +8 / +16 / +24 / +32 are (count, offset from the record) of its key tables.
- I: in Menu3 to Menu6 the key values with property code 5009 are the rows' y offsets and those with code 5002 hold 1.0f (shown / opacity). The values are V (read in the file); the property meanings are I.
- V (seen in play): with the Menu layer at y 770, the Menu4 rows match the hand cursor rows seen in the running title menu (y 817 / 866 / 917 / 965).

## Referenced by

- Observed behaviours: [TitleMenuRows](../behaviors/TitleMenuRows.md)

## Notes

Read with the layout component reader; the timeline offsets are file offsets of the records.

## Open questions

None recorded.
