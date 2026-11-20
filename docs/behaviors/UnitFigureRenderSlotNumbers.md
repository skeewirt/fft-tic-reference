# UnitFigureRenderSlotNumbers

- **Kind:** observed behaviour
- **Scope:** engine (menu unit figures)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [CharaRender_RegisterSlot](../functions/CharaRender_RegisterSlot.md), [CharaRender_SetSlotRequest](../functions/CharaRender_SetSlotRequest.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobTree_SetPanelRecord](../functions/JobTree_SetPanelRecord.md), [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every unit figure a menu draws is registered under a render slot number 0..255; the Change Job list, the Job Tree and the Status header each use fixed numbers, so two figures registered under one number draw as one.

## Behavior

- V: CharaRender_SetSlotRequest refuses a slot number above 255; the manager keeps a 112-byte entry per number at +14920 (the image node at +0, the number at +56).
- V: JobTree_FillJobRecords numbers the sprite record of list position n as 61 + n (lea eax, [r14+3Dh]) before it hands it to the Change Job list cell and to the tree; JobTree_SetPanelRecord then numbers panel p as 80 + p (lea eax, [r14+50h]; the only place that adds 80) and registers it. Stock: at most 19 cells (61 .. 79) and 20 panels (80 .. 99).
- V: sub_1401151EC registers the figure record it is given as slot 107 and again under the number its addon keeps at +8136; sub_140125C88 registers the record it is given, keeps that number at +8136 and a copy numbered 106 at +792. The two callers of sub_140125C88 (sub_140114ECC, sub_1401153A4) pass number 108.
- V (immediates stored as a figure's number before a registration): 59 (sub_140114D74), 60 (sub_14011545C), 107 (JobScreen_UpdateState, sub_1402C2BFC), 108 (sub_140114ECC, sub_1401153A4), 136 (sub_1401AC6A8).
- V (live read 2026-11-19, the Change Job grid open): the registered numbers were 61 .. 79 without 73 (the cells), 80 and up (the panels) and 108, the pedestal figure of the Status header, whose addon held 108 at +8136; no number above 108 was registered.
- V (seen live 2026-11-19): a figure registered under 108 while that screen is open is what the header's pedestal draws, for every unit shown, until the header registers its own again.

## Open questions

? the numbers the roster, the formation screen and the battle use; ? what 59, 60 and 136 show.
