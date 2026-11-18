# FaceNumberCapsClipRawCodesToo

- **Kind:** observed behaviour
- **Scope:** engine (portrait face numbers)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [Unit_GetSpriteSetId](../functions/Unit_GetSpriteSetId.md), [sub_1401F3858](../functions/sub_1401F3858.md), [sub_140214134](../functions/sub_140214134.md), [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md), [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md), [sub_1402DF374](../functions/sub_1402DF374.md), [sub_14032B1A4](../functions/sub_14032B1A4.md), [HdLayer_BindSheetTexture](../functions/HdLayer_BindSheetTexture.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sixteen readers cap the face number at 0xCD (205): the twelve caps below and the four readers of the HD face table g_FaceG2dEntryByFace. Several caps also see a value that did not come from the face table.

## Behavior

- V: the caps are at 0x1401F3A03, 0x140214178 (register set, compared at 0x140214272), 0x1402150A2 (compared at 0x14021519D), 0x14021568B (compared at 0x140215786), 0x14021FDEB, 0x140229A50, 0x1402C0816, 0x1402C086C, 0x1402D7BE6, 0x1402E065A, 0x14032C469 and 0x14037651E.
- V: at 0x14021FDEB (sub_14021FA50), 0x1402C0816 (Unit_GetSpriteSetId), 0x1402D7BE6 (sub_1402D7954) and 0x14032C469 (sub_14032B1A4) the mode word at 0x142FF9ED8 can skip SpriteId_ToShape, and the raw value is capped instead.
- V (corrected 2026-11-08): at 0x1402C0816 the raw value comes from sub_14032AB3C through PortraitCode_FillCell and is at most 255 (or the save record index when no code is set): a code with bit 8 or 9 is refused and the colour bits 10 and 11 leave as the colour. The raw codes that can be 0x400 or more (the scripted message writes job row +47 << 10 into the dialogue slots) reach the dialogue-slot readers 0x14021FDEB, 0x14032C469 and 0x1402D7BE6.
- V: the four readers of g_FaceG2dEntryByFace (sub_14041AE44 at 0x14041B34E, sub_14041CAAC at 0x14041CC09, HdLayer_BindSheetTexture at 0x14041DA3F, sub_14041DAA4 at 0x14041DB82) each compare the slot value unsigned with 0xCD before the read; they belong to the same family.
- V: in sub_140214134 and the two turn panel functions an unset code (-1) leaves the per-pool value from sub_14022AA88 in the capped register.
- V: on the generic path of Unit_GetSpriteSetId (0x1402C086C) only a table answer is capped; an unmapped code is returned uncapped, and its bits 10 and 11 give the colour.
- V: HdLayer_BindSheetTexture reads the face table at 0x140714EA0 with a limit of 0xCD for its first three texture ids.
- V: fourteen of the sixteen caps are on battle, dialogue and event paths.

## Open questions

? the stock range of the raw codes on the mode-word path (what values reach the caps in play).
