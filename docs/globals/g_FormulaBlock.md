# g_FormulaBlock

- **Kind:** global
- **Address:** `0x1407B0770`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[16]`
- **Points to / is a:** [FormulaBlock](../structs/FormulaBlock.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The block the action resolver and the formula handlers share, 0x48 bytes from 0x1407B0770: the request's action type, the ability being worked out (the word at +8, address 0x1407B0778), the weapon or item word, the inflict-record index, the formula id (+0x18) and copies of the ability, weapon and inflict records. See struct FormulaBlock for every field.

## Behavior

- V: Battle_ResolveAction fills it per target: byte +6 is the request's action type (the index into g_CommandKind), word +8 the ability id taken from the request (or from the word at 0x1407B0768 when the word at 0x1407B076A is non-zero), word +10 the weapon or item id, byte +13 the inflict-record index (g_InflictRecords has 6-byte rows; row 0 is used for formula 3).
- V: five places write the word at +8 (0x1407B0778): Battle_ResolveAction at 0x140309B6A and 0x140309C42, sub_1403071DC at 0x140307263, sub_14030B4F0 at 0x14030B6BE and 0x14030B75B.
- V: fourteen places read it: sub_14030588C (0x1403058A2), sub_140305F4C (0x140305F52, the Golem test), sub_1403064D8 (0x1403064D8), Action_PickTargetEquipment (0x1403065E4), sub_140306C10 (0x140306C30, the id 219 test), Formula_28_BardSongs (0x140307AB2), Formula_29_DancerDances (0x140307B84), Formula_42_Speechcraft (0x140308379), Battle_ResolveAction (0x140309D67), sub_14030AFEC (0x14030B069), sub_14030B1A0 (0x14030B1C1), sub_14030B4F0 (0x14030B667, 0x14030B82F) and sub_14030BDC0 (0x14030BE07).
- V: the handlers that read it choose their effect by the id; see FormulaHandlersChooseTheirEffectByAbilityId.

## Referenced by

- Observed behaviours: [FormulaHandlersChooseTheirEffectByAbilityId](../behaviors/FormulaHandlersChooseTheirEffectByAbilityId.md)
- Read by: [sub_1403064D8](../functions/sub_1403064D8.md), [sub_14030B1A0](../functions/sub_14030B1A0.md)

## Notes

The block's other bytes are written by many formula handlers (dozens of write sites); only the fields above were read here.

## Open questions

? the meaning of block bytes +0 .. +5, +11, +12, +14, +15 (written and read by the handlers; not enumerated).
