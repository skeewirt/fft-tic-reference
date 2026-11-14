# EquipPanelBlock

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A 64-byte copy of a party or battle record's bytes +0x30..+0x6F, kept at 0x141876E90 for the field equip screens and at 0x141D3B880 for the battle panels. Its five hand words sit at +0x24 (record +0x54) and a second five-word array at +0x2E (record +0x5E). It is a screen copy, not a field of the unit record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="record_30"></a>+0x00 | record_30 | `uint8[0x10]` | V | Copy of record +0x30..+0x3F. Filled by JobScreen_RefreshAfterChange (0x1402BD15D) and sub_1402BBBCC (0x1402BBF68) with movaps; by PartyUnit_ReloadEquipment (0x1402BDB20) from record B +0x30. |
| <a id="record_40"></a>+0x10 | record_40 | `uint8[0x10]` | V | Copy of record +0x40..+0x4F in the screen writers. PartyUnit_ReloadEquipment overwrites the whole 16 bytes with a local value whose low word is the two-handed result (0x1402BDB37). |
| <a id="record_50"></a>+0x20 | record_50 | `uint8[0x10]` | V | Copy of record +0x50..+0x5F; its words at +0x24..+0x2C are the five hand words. |
| <a id="hands"></a>+0x24 | hands | `uint16[5]` | V | The five equipment words at record +0x54..+0x5C. PartyUnit_ReloadEquipment copies them raw from g_PartyUnits (movsd at 0x1402BDABB, word at 0x1402BDAB7, movaps to +0x24 at 0x1402BDB42); JobScreen_RefreshAfterChange and sub_1402BBBCC copy record +0x30..+0x6F with movaps, which carries +0x54..+0x5C to +0x24..+0x2C. |
| <a id="second_row"></a>+0x2E | second_row | `uint16[5]` | ? | Five words at record +0x5E..+0x66; read by sub_14032F410 (0x14032F4D3) and sub_14032F9F8 (0x14032FCEC). ? who fills them; they are not the hand words. |
| <a id="record_68"></a>+0x38 | record_68 | `uint8[8]` | V | Copy of record +0x68..+0x6F. |

## Behavior

- V: the field copy is written by PartyUnit_ReloadEquipment (0x141876E90), JobScreen_RefreshAfterChange (0x141876E90) and sub_1402BBBCC (0x141876E90); the battle copy is written by sub_14033E394 (0x141D3B880).
- V: the two panel readers extract bits 14..15 of the hand word with shift 12 and mask 0xC: sub_14032EDB8 at 0x14032F178/0x14032F17D and sub_140399A64 at 0x140399E24/0x140399E29.
- V: the id is masked with 0x1FF by both panel readers, so the panel's id field is nine bits wide even though the source party word uses ten.

## Referenced by

- Observed behaviours: [EquipSessionFlagLifecycle](../behaviors/EquipSessionFlagLifecycle.md)

## Notes

V: the 0x141D3B880 layout is the same 0x30..0x6F copy, written by sub_14033E394 from a battle record.

## Open questions

? the source battle record of sub_14033E394 and whether a flagged party word can still be in it when a battle panel opens.
