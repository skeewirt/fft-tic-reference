# BUi_BattleMenuWindowsSetPage

- **Address:** `0x1401015FC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void sub_1401015FC(agent, unsigned int menuId, unsigned int state)`
- **Callers:** `sub_1400E68BC`, `sub_1400E6BD8`, `sub_1402100F4`, `sub_140210184`
- **Callees:** `sub_1400FB3B0`, `sub_1400FB7C8`, `sub_1400F5828`, `sub_140154308`, `sub_140154624`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The command menu's show/hide entry point: maps a caller's state to a page show or hide.

## Behavior

- V: requires both addons (`agent+64` and `agent+72`) to be non-null.
- V: calls `sub_1400FB3B0(state, 0, 0)` and `sub_1400FB7C8(..., 0)` (UI focus/input bookkeeping).
- V: when the HUD addon (`agent+64`) is shown and `state <= 1`, resets its `+104` and `+112` nodes with `sub_1400F6148`.
- V: when the command addon is shown: `state == -1` -> `sub_140154308(addon, menuId, -1)` (hide); `state == 0` or `1` -> `sub_140154624(addon, menuId)` (show page) and sets `+5628 = 1`; any other state -> `+5628 = state`, then hide with that state as frame. The visible row lives in the radio menu (`addon+1120`), not in `+5628`/`+5629` (live, Legate).

## Notes

The two event-facing wrappers `sub_1400E68BC` / `sub_1400E6BD8` take `(a1, state, menuId, outChanged)` and set `*outChanged = 1` when `state <= 1`.

## Open questions

? what `sub_1400FB3B0` / `sub_1400FB7C8` do (input focus and cursor).
