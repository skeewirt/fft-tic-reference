# Battle_MenuClose

- **Address:** `0x1402100F4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void sub_1402100F4(void)`
- **Callers:** battle scene/command flow (data references)
- **Callees:** `sub_140260824`, `sub_14030DBAC`, `sub_1401015FC`, `sub_1400F5828`, `sub_140155FE8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Closes the command menu for the acting unit.

## Behavior

- V: node = `sub_140260824(dword_140C6AFB8, dword_140C6ADAC, dword_140C6AFBC)`; menuId = `sub_14030DBAC(node->subrecord byte +444)`.
- V: `sub_1401015FC(agent, menuId, -1)` hides the page.
- V: if the command addon (`agent+72`) is present and shown, clears addon byte `+5629` and calls `sub_140155FE8(addon, 0)`.
- V: the page hide path (`sub_140154308`) sets addon `+5624 = -1`, so both "shown" and "page" go to their idle values.

## Notes

Called when a command is confirmed (the owner's observation: choosing Move hides the menu and the glove). After this, tile selection runs with the command menu closed. `+5629` is an internal latch only; the visible selected row is `addon+1120` (radio menu at +840), and this function's hide path clears it to -1.

## Open questions

? whether a cancel path uses the same function or `sub_1401568EC`.
