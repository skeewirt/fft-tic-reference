# Battle_MenuOpen

- **Address:** `0x140210184`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char sub_140210184(void)`
- **Callers:** battle scene/command flow (data references)
- **Callees:** `sub_140260824`, `sub_14030DBAC`, `sub_1401015FC`, `sub_1400F5828`, `sub_140156074`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the command menu for the acting unit.

## Behavior

- V: node = `sub_140260824(dword_140C6AFB8, dword_140C6ADAC, dword_140C6AFBC)` (the unit at the current battle position).
- V: the menu id comes from `sub_14030DBAC` applied to the byte at offset 444 of the unit node's sub-record (preview index -> command/menu id).
- V: `sub_1401015FC(agent, menuId, 0)` shows the menu page; the agent is the ninth entry (offset 64) of the UI agent manager's agent vector (`qword_143CD9DA8`, vector at +16).
- V: if the command addon (`agent+72`) is present and its `+48` node is "shown" (`sub_1400F5828(+48, 12, 0, 0)`), sets addon `+5629 = 1` and calls `sub_140156074(addon, 0)`.

## Notes

Paired with `Battle_MenuClose` (0x1402100F4). The menu id -> page mapping is in `Battle_MenuPageOfCommand` (0x140154248); the page builder is `Battle_MenuShowPage` (0x140154624). The live selected command row is `addon+1120` (embedded radio menu at +840, field +280); `+5629` is an internal latch and did not match the live menu (Legate). For "command menu up", read the radio menu entry count at `addon+856` (non-zero) and `addon+1120` (>= 0).

## Open questions

? what `dword_140C6AFB8/AC/BC` are (a tile coordinate triple, I); ? `sub_140156074`'s role.
