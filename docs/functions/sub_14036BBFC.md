# sub_14036BBFC

- **Address:** `0x14036BBFC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void __fastcall sub_14036BBFC(_DWORD *message)`
- **Callers:** not in the exported set; the shop/equip screen message dispatcher
- **Callees:** `sub_140121938`, `sub_1402C185C`, `sub_14019C234`, `sub_1401987F0`, `sub_140289894`, `sub_14036C2A8`, `sub_1402C4880`, `sub_1402C40BC`, `sub_1401158E4`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The shop/equip detail screen's message handler: it builds the detail record from the scratch unit, applies a
picked row, and closes the screen.

## Behavior

- V: The message id is `*a1`, tested by a subtract chain (corrected 2026-11-10; the earlier reading was one off):
  3 closes; 36 (0x24) posts a shop message (text 63497); 62 (0x3E) applies the picked row through `sub_14036C2A8`;
  63 (0x3F) builds the detail.
- V: Message 63 copies the scratch party record (the record of party pointer 54, `qword_141801100`) into stack buffers:
  its +0x22..+0x6F fields and its whole block from +0x70 (+112) to the record's end (unlock mask, learned bits, job levels,
  JP), and calls `sub_1402C185C` with them to build the detail; it stores `word_141876C50 > 0` as a byte in the detail.
- V (live 2026-11-10): it is the Outfitter's Fitting screen (Shop_Open). Its stack copy is no known record.
- V: It reads the scratch record raw but only the non-hand fields; the hand copy is in `sub_14036C2A8`.
- I: The `word_141876C50 > 0` byte is the two-handed marker of the displayed detail.

## State touched

- Calls: [sub_1402C185C](sub_1402C185C.md), [sub_14036C2A8](sub_14036C2A8.md)
- Reads: [qword_141801100](../globals/qword_141801100.md), [g_EquipSet](../globals/g_EquipSet.md)

## Referenced by

- Observed behaviours: [PreviewBuildersReadPartyRecordCopies](../behaviors/PreviewBuildersReadPartyRecordCopies.md)

## Notes

V: the shop/equip message handler. It builds a record from the scratch unit and stores the two-handed word as a byte (0x14036BD23); it does not test the hand flags.

## Open questions

None recorded.
