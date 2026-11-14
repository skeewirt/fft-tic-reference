# FaceLookupInlineCopiesDisagreeAboveCode159

- **Kind:** observed behaviour
- **Scope:** engine (portrait face numbers)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [SpriteId_ToShape](../functions/SpriteId_ToShape.md), [sub_140214134](../functions/sub_140214134.md), [TurnPanel_SetUnitPanel](../functions/TurnPanel_SetUnitPanel.md), [TurnPanel_SetTag](../functions/TurnPanel_SetTag.md), [sub_1402DF374](../functions/sub_1402DF374.md), [sub_1401F3858](../functions/sub_1401F3858.md), [sub_140221798](../functions/sub_140221798.md), [sub_1402F8684](../functions/sub_1402F8684.md), [sub_140338A28](../functions/sub_140338A28.md), [sub_1403980AC](../functions/sub_1403980AC.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The face-number lookup exists as SpriteId_ToShape and ten inline copies; for codes above 0x9F five of the copies answer differently from the function, so one table row cannot stand for all of them.

## Behavior

- V: each copy compares the code with 0x9F (jump if above), reads g_SpriteIdToShape, else runs a switch over codes above 0x9F; the copies in sub_1401F3858, sub_140221798, sub_1402F8684, sub_140338A28 and sub_1403980AC give SpriteId_ToShape's answers for every code (unicorn, codes 160 to 1299).
- V: sub_140214134, TurnPanel_SetUnitPanel and TurnPanel_SetTag give no face (-1) for code 205, where SpriteId_ToShape gives 205.
- V: Battle_UnitStatusFillAlt (0x140228778) and sub_1402DF374 use an older list: codes 184 to 187 give 192 down to 189, and codes 189 to 193, 196 to 201 and 205 give no face.
- V: in each inline copy the fallback register is the -1 the function sets (an or with -1) before the copy (or the copy sets itself), the same register the code is compared with just before to skip an unset code.
- I: the five copies that differ are battle HUD readers (turn panels, the status window)

## Open questions

None recorded.
