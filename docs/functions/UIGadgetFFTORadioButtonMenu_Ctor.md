# UIGadgetFFTORadioButtonMenu_Ctor

- **Address:** `0x1402AD5BC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 sub_1402AD5BC(UIGadgetFFTORadioButtonMenu *menu)`
- **Callers:** `sub_140153020` (battle command addon ctor, twice: `+840` and `+1144`)
- **Callees:** `sub_14028B9C8`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructs the 304-byte radio-button menu gadget used by the battle command page (Move / Abilities / Wait / Status) and by other UIB screens.

## Behavior

- V: sets vtable `vftable_ffto::Game::UI::UIGadgetFFTORadioButtonMenu_140716730`, `+16` (entry count) = 0, `+24..` (entry node pointers) left as allocated.
- V: `+280` (selected index) = -1 (`0x1402AD5F8`), `+284` (hover index) = -1 (`0x1402AD5FE`).
- V: `+288` word (changed/pending bytes) = 0 (`0x1402AD5E0`), `+290` byte (hover pending) = 0 (`0x1402AD5EB`).
- V: registers the gadget with the UI gadget module `qword_143CDA380`.

## Referenced by

- Called by: [WorldMapBaseList_Construct](WorldMapBaseList_Construct.md)

## Notes

In `UIAddonFFTOBattleCommand` the gadget sits at addon `+840`, so its fields are addon `+856` (count), `+864` (entries), **`+1120` (selected)**, `+1124` (hover), `+1128` / `+1130` (flags), `+1136` (page/command id). The Legate's live read confirmed `+1120` as the visible command row (0 Move, 1 Abilities, 2 Wait, 3 Status).

## Open questions

? which function fills the entry array (count +16, pointers +24) when the page is built.
