# TurnPanel_SetUnitPanel

- **Address:** `0x140214FB4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char TurnPanel_SetUnitPanel(int a1, int a2, int unit, uint8 entryFlags, unsigned int entryAbility)`
- **Callers:** TurnPanel_ShowUnitAction (2 sites), sub_140216C04
- **Callees:** sub_14022AA88, Str_Format, AbilityTable_GetRow, JobCommandTable_GetRow, sub_1400E5910

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the unit panel shown for a turn-order entry, with the pending ability's name when the entry is an action.

## Behavior

- V: the same name decode as TurnPanel_SetTag (0x40 and not 0x20: entryAbility + (0x80 ? 256 : 0), then AbilityTable_GetRow), into unk_143CDA7C0.
- V: unit > 20 returns through sub_140214F54; when the unit's record from sub_140260ABC is the acting one, the panel mode (dword_140C6B1CC) is 25 and no name was set, the name comes from that record's word +0x17A instead (AbilityTable_GetRow, or JobCommand row 18 for 394..405; the word is read as a full u16).

## State touched

- Calls: [sub_14022AA88](sub_14022AA88.md), [Str_Format](Str_Format.md), [AbilityTable_GetRow](AbilityTable_GetRow.md), [JobCommandTable_GetRow](JobCommandTable_GetRow.md)
- Reads: [g_LookPoolFaceValue](../globals/g_LookPoolFaceValue.md)

## Referenced by

- Observed behaviours: [BattleFaceIsThePoolSpriteByte](../behaviors/BattleFaceIsThePoolSpriteByte.md), [FaceLookupInlineCopiesDisagreeAboveCode159](../behaviors/FaceLookupInlineCopiesDisagreeAboveCode159.md), [FaceNumberCapsClipRawCodesToo](../behaviors/FaceNumberCapsClipRawCodesToo.md), [LooksPastTenShowThePoolNumbersFace](../behaviors/LooksPastTenShowThePoolNumbersFace.md), [TurnOrderEntryKeepsNineBitsOfTheAbility](../behaviors/TurnOrderEntryKeepsNineBitsOfTheAbility.md)
- Reads tables: [SceneSpriteToFace](../tables/SceneSpriteToFace.md)

## Notes

TurnPanel_ShowUnitAction passes the flags and ability byte of the unit's own pending-action entry in g_TurnList.

The portrait face is an inline copy of SpriteId_ToShape (the code bound at 0x1402150B4, the table read at 0x1402150BC, the cap register r8d = 0xCD set at 0x1402150A2 and compared at 0x14021519D). For an unset code (-1) the value capped is the per-pool value from sub_14022AA88. Its list for codes above 0x9F differs from SpriteId_ToShape's at code 205 (unicorn).

## Open questions

None recorded.
