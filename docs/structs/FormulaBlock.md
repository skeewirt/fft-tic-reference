# FormulaBlock

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 72 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The state of the one action being resolved: Battle_ResolveAction fills it per target and every formula handler reads and writes it. It holds the request's command kind, the ability and item ids, the formula id and copies of the ability, weapon and inflict records the handlers read. Instance: g_FormulaBlock (0x1407B0770).

## Fields

| Offset | Field | Type | Conf | Meaning | Observed behaviours | Read by |
|---|---|---|---|---|---|---|
| <a id="working_word_0"></a>`0x0` | working_word_0 | `uint16` | I | A working word the handlers use (the formulas write and read it; its meaning differs per formula). |  |  |
| <a id="working_word_2"></a>`0x2` | working_word_2 | `uint16` | I | A second working word, as +0x00. |  |  |
| <a id="command_kind"></a>`0x6` | command_kind | `uint8` | V | The request's action type, the index into g_CommandKind; Battle_ResolveAction stores it at 0x140309C27. |  |  |
| <a id="ability_id"></a>`0x8` | ability_id | `uint16` | V | The ability being resolved (0x1407B0778): five writers, fourteen readers; the handlers that branch on it are listed in FormulaHandlersBranchOnTheAbilityId. |  |  |
| <a id="item_id"></a>`0xA` | item_id | `uint16` | V | The weapon or item id of the action; Battle_ResolveAction clears it for formula 100 after the handler (0x140309F68). |  |  |
| <a id="flag_c"></a>`0xC` | flag_c | `uint8` | ? | Written 0 or a request value by Battle_ResolveAction (0x140309B60, 0x140309F15, 0x140309F3D), tested against 0 by sub_140306E34; its meaning was not read. |  |  |
| <a id="inflict_row"></a>`0xD` | inflict_row | `uint8` | V | The row of g_InflictRecords (6-byte rows) the action inflicts from: the weapon record's byte +7 (0x140309BCE), the chemist record's byte +2 (0x140309E6E) or the ability record's byte +0x0B (0x140309D70, skipped for ability 358); read at 0x140309DB5, where formula 3 uses row 0 instead. |  |  |
| <a id="chemist_slot"></a>`0xE` | chemist_slot | `uint8` | V | Chemist branch only: a stack byte (the item list index) plus 0x10, stored at 0x140309E5D; read by ItemAction_SetAmount, sub_140308C30, sub_140308C98 and sub_1401F9CC4, which rebuild the item id from it. |  |  |
| <a id="weapon_bonus"></a>`0x17` | weapon_bonus | `uint8` | V | Zeroed at the start of each resolve (0x140309BDB writes the word 0x0100 over +0x17 and +0x18), set from the weapon branch at 0x140309ECB; read by the handlers of formulas 2..7 (sub_140306EF0, sub_1403071A4, sub_1403071DC, sub_1403072F8, sub_140307388, sub_1403073C4). It is not a formula id. |  |  |
| <a id="formula_id"></a>`0x18` | formula_id | `uint8` | V | The clamped formula id: stored once at 0x140309E12 (default 1 at 0x140309BDB), dispatched through the registry at 0x140309F53, and read by ten places (0x1402058F6, 0x140305F34, 0x14030A2A0, 0x14030AA6F, 0x14030B002, 0x14030B2B0, 0x14030B3A5, 0x14030B778, 0x14030BBAC, 0x14030BC6E) and copied to and from the capture buffer (0x14030DA88, 0x14030D89A). | [FormulaPostHooksAreKeyedByFormulaId](../behaviors/FormulaPostHooksAreKeyedByFormulaId.md) | [sub_14030A11C](../functions/sub_14030A11C.md) |
| <a id="mp_cost"></a>`0x1E` | mp_cost | `uint8` | V | The MP cost of the action (global g_AbilityMpCost, 0x1407B078E). |  |  |
| <a id="flags"></a>`0x20` | flags | `uint8` | ? | A flag byte: sub_140304DC0 writes 0x81 or 0x82; Battle_ResolveAction's callees test and clear bit 0x80 together with word +18 bit 0x4000 of the result block (sub_14030A11C, sub_140305504, sub_1403067D0, sub_140307140); its meaning was not read. |  |  |
| <a id="ability_record"></a>`0x24` | ability_record | `uint8[20]` | V | A copy of the 20-byte action record of the ability (or zero for a chemist item), made by Mem_CopyChecked with size 0x14 (0x140309BAC, 0x140309D49); its byte +8, the record's own formula byte (block +0x2C), is never read from here (the resolver reads the record). Byte +10 (block +0x2E) is read by sub_1401F9C54 as a percentage. |  |  |
| <a id="weapon_record"></a>`0x38` | weapon_record | `uint8[8]` | V | A copy of the weapon's 8-byte record, made by Mem_CopyChecked with size 8 (0x140309BC5 and 0x140309D39). |  |  |
| <a id="weapon_formula"></a>`0x3A` | weapon_formula | `uint8` | V | The weapon record's own formula byte (record +2): read only by Formula_106_ReDispatchChainFormula (0x14030D724), unclamped, as the index of its second dispatch. |  |  |
| <a id="inflict_record"></a>`0x40` | inflict_record | `uint8[6]` | V | A copy of g_InflictRecords[row] (6-byte row; row = +0x0D except formula 3 uses row 0), made by Mem_CopyChecked with size 6 at 0x140309DEC; its byte +5 is copied to byte_14186B02C (0x140309E0A). |  |  |

## Behavior

- V: the block starts at 0x1407B0770 and ends with the inflict record copy at 0x1407B07B0..0x1407B07B6; sub_14030A11C also clears the byte at 0x1407B07B8 (+0x48), the first byte after it (I: the block's extent is 0x48).
- V: the capture buffer of Battle_SaveCapture / Battle_RestoreCapture keeps the formula byte at buffer +0x48; a wider formula id would change that layout.
- V: the block's two bytes +0x17 and +0x18 are one word at 0x1407B0787 for the stores at 0x140309BDB (0x0100) and the reads of +0x17 through `byte word_1407B0787`.
- I: the weapon and chemist formula bytes come from the copied records of the same resolve (ability record +8 at the ability branch, weapon record +2, chemist record +0): the block keeps only the clamped result at +0x18, plus the weapon record copy that Formula_106 reads.

## Referenced by

- Global instances: [g_FormulaBlock](../globals/g_FormulaBlock.md)
- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)
- Written by: [Battle_ResolveAction](../functions/Battle_ResolveAction.md)

## Notes

Source: IDA reads of 2026-11-12. The existing global record g_FormulaBlock names the first 16 bytes; this record is the whole block.

## Open questions

? the meaning of +0x00, +0x02, +0x0C, +0x20 and of the bytes not listed (+0x07, +0x1B..0x1D, +0x1F, +0x21..0x23, +0x34..0x37).
