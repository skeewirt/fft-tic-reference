# Formula_EvadeRoll

- **Address:** `0x14030588C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_EvadeRoll(void)`
- **Callers:** sub_140306C90, sub_140306D70, sub_1403072F8
- **Callees:** Formula_EvadeByteRoll

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The shared evade step of the physical and magic gates: scales the shown hit percent by the four evade bytes and rolls each of them.

## Behavior

- V: runs only when the ability word (g_FormulaBlock +8) is 0 or bit 0x02 of the ability record copy's flag byte (0x1407B079A, record +6) is set; otherwise it returns at once.
- V: the baseline is the byte at g_FormulaBlock +0x0F (0x1407B077F, the last byte of the 16-byte block) and the four evade bytes sit at 0x1407B0781..0x1407B0784 (block +0x11..+0x14), set by the gate that called. When any evade byte is >= the baseline it stores R+0 = 0 and R+44 = 0 (a sure evade, nothing rolled by chance).
- V: otherwise R+44 = R+44 * (the product of the four percentages 100 * (baseline - evade) / baseline, divided by 10^6) / 100, so the preview percent falls by each evade.
- V: then it calls Formula_EvadeByteRoll for the four bytes in order with reasons 1, 2, 3, 4 and stops at the first roll that fails the hit (the helper stores R+0 = 0 and R+2 = reason).
- I: the four bytes are class / accessory / shield / shield evade (the two gates fill them from different record bytes); the names come from the gates' reads, not from a label.

## State touched

- Calls: [Formula_EvadeByteRoll](Formula_EvadeByteRoll.md)
- Writes: [ActionResult.hit_percent](../structs/ActionResult.md#hit_percent)

## Referenced by

- Called by: [Formula_05_WeaponAttackNoElement](Formula_05_WeaponAttackNoElement.md)

## Notes

Source: block B03. 441 bytes, read whole. Contract for a data formula: needs the baseline byte, the four evade bytes and R+44; writes R+0, R+2 and R+44. Crosscheck: the evade bytes 0x1407B0781..0x1407B0784 (block +0x11..+0x14) are read as the dword at 0x1407B0781 and its byte parts, RIP-relative operands.

## Open questions

? which of the four evade bytes is which beyond the gates' field reads.
