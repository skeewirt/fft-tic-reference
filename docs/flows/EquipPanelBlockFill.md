# EquipPanelBlockFill

- **Kind:** flow
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the five hand words travel from a unit record to the two panel blocks and what the two flag-aware panels do with them.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1 field copy"></a>1 field copy | [JobScreen_RefreshAfterChange](../functions/JobScreen_RefreshAfterChange.md) | V | Copies record +0x30..+0x6F to 0x141876E90 with four movaps; +0x54..+0x5C lands at +0x24..+0x2C. |
| <a id="2 field copy"></a>2 field copy | [PartyUnit_ReloadEquipment](../functions/PartyUnit_ReloadEquipment.md) | V | Copies the five live hand words to a 32-byte stack value and stores it at block +0x20, so +0x24..+0x2C are raw g_PartyUnits words; the stat fields are filled separately. |
| <a id="3 battle copy"></a>3 battle copy | [sub_14033E394](../functions/sub_14033E394.md) | V | Copies a battle record +0x30..+0x6F to 0x141D3B880, the same slice at the same offsets. |
| <a id="4 panel read"></a>4 panel read | [sub_14032EDB8](../functions/sub_14032EDB8.md) | V | Walks five words at the carrier's +0x24, masks the id with 0x1FF, and extracts bits 14..15 with shift 12 and mask 0xC into a UI dword. |
| <a id="5 battle panel read"></a>5 battle panel read | [sub_140399A64](../functions/sub_140399A64.md) | V | The same walk and extraction over 0x141D3B880 +0x24. |

## Behavior

- V: the panel's id bound is 0x105 and 0xFF is the empty marker; a word with bit 15 set still passes the 0x1FF mask, so the id is shown and the bit is only used for the two-bit UI value.
- V: no stock writer sets bit 14 in the block hands; the bit exists in the same word positions on the shop/list side.

## Open questions

? what the two-bit value selects in the text draw.
