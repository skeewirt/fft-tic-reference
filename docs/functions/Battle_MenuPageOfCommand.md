# Battle_MenuPageOfCommand

- **Address:** `0x140154248`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `unsigned int sub_140154248(UIAddonFFTOBattleCommand *addon, unsigned int menuId)`
- **Callers:** `sub_1401542AC`, `sub_140155E04`
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a battle command/menu id to one of the six `BattleMenu` page numbers.

## Behavior

- V: `menuId <= 0x13`: `0x0F` and `0x12` -> 2; `0x10` -> 1; `0x11` -> 3; `0x00`, `0x0E`, `0x13` -> 5; every other value -> 0.
- V: `menuId == 20 (0x14)` -> 5.
- V: `menuId == 46, 47, 48, 49` -> 6.
- V: `menuId == 54` -> 1; every other value -> 0.

## Notes

`sub_1401542AC` uses `page-1` to index addon `+96..+136` (the six `BattleMenu0N` nodes), so 0 means "no page". The special ids 46..49 come from `sub_14030DBAC` for units with a negative command-row byte.

## Open questions

? which command ids 15..20 correspond to Move / Abilities / Wait / Status in the UI list; ? why 54 maps to page 1.
