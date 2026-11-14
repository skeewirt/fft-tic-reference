# EquipSetBlock

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The equip screen's computed set at 0x141876C40: stat deltas at +0x00..+0x23, the five candidate equipment words at +0x24..+0x2D, a five-word display array at +0x2E..+0x37, and unclassified words at +0x38..+0x3F. It is rebuilt per screen refresh and never saved.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="stat_delta"></a>+0x00 | stat_delta | `int32` | V | A stat delta computed from two compared equipment words; sub_140286BDC clears it and writes the difference of two category-derived values at 0x140286C46. |
| <a id="stat_word_04"></a>+0x04 | stat_word_04 | `uint16` | V | Second stat delta; sub_140286BDC writes it at 0x140286C81. |
| <a id="stat_words_06"></a>+0x06 | stat_words_06 | `uint16[4]` | V | Four stat words cleared at 0x140286BF7 and read by sub_1402C20F0 (0x1402C24C7-0x1402C24E4) as the attack/defence pair it shows. |
| <a id="mode_word"></a>+0x0E | mode_word | `uint16` | V | The panel variants test it for zero: sub_14032EDB8 at 0x14032EE8B (alias 0x141876C4E) and sub_14032F410 at 0x14032F4DA. Zero selects the one-row layout, non-zero the two-item layout. |
| <a id="two_handed"></a>+0x10 | two_handed | `uint16` | V | 0 or 1 from sub_140284998: 1 when the selected hand weapon is two-handed or carries the record byte's bit 4. Written at 0x1402D5DE8, 0x1402D6A34, 0x1403340A2 and 0x14036C35B; read by sub_14032EDB8 (0x14032EE84) and sub_14036BBFC (0x14036BD23). |
| <a id="stat_words_12"></a>+0x12 | stat_words_12 | `uint16[4]` | V | Four stat words cleared at 0x140286C02; sub_1402C20F0 reads the pair at +0x16/+0x18 (0x1402C2479, 0x1402C24A5) and the pair at +0x20/+0x22 (0x1402C2486, 0x1402C24B2). |
| <a id="stat_words_1c"></a>+0x1C | stat_words_1C | `uint16[4]` | V | Four stat words cleared at 0x140286C0C and read as the defence pair by sub_1402C20F0. |
| <a id="candidates"></a>+0x24 | candidates | `uint16[5]` | V | The five candidate equipment words (g_EquipCandidates, 0x141876C64..0x141876C6D). Bits 0..9 are the id; bit 15 marks a proposed change; 0 is empty. The builder marks only the first four; the fifth (word at +0x2C) is copied from the unit's +0x5C by the session functions. |
| <a id="display_words"></a>+0x2E | display_words | `uint16[5]` | ? | Five words read by sub_14032F410 (0x14032F4D3/0x14032F4C0) as a second row of item ids. No instruction in the .text census writes them; ? writer and meaning. |
| <a id="tail"></a>+0x38 | tail | `uint8[8]` | ? | No reader or writer found in the exported set; ? content. |

## Behavior

- V: the block is one 0x40-byte object; g_EquipCandidates is its +0x24 field, not a separate array (0x141876C40 + 0x24 = 0x141876C64).
- V: sub_14028728C and sub_140287354 fill only the stat words and read the equipment words masked with 0x3FF; neither writes the candidate or display words.
- V: sub_140287D9C marks four candidate words with 0x8000 (loop count four at 0x140288471) and leaves the fifth to its callers.

## Referenced by

- Global instances: [g_EquipSet](../globals/g_EquipSet.md)
- Observed behaviours: [EquipSessionFlagLifecycle](../behaviors/EquipSessionFlagLifecycle.md)

## Notes

V: addresses and writers from a census of the sites; the stat field names are descriptive only, the pair order was not decoded.

## Open questions

? the exact stat each word at +0x00..+0x23 holds; ? who writes the display words at +0x2E.
