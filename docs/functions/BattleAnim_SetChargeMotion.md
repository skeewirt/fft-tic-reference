# BattleAnim_SetChargeMotion

- **Address:** `0x140269920`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleAnim_SetChargeMotion(void *obj)`
- **Callers:** sub_140206CE8, sub_14020C704, sub_140269BBC
- **Callees:** sub_1402696E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the charging motion from the charge byte of g_AbilityAnim (the effect word +0x142).

## Behavior

- V: m = byte_1406735A9[2 * charge]; when m != 0, obj +0x10 = m + 1 (or 10 under a condition of sub_1402696E8 and the unit's +0x1B4 bits).

## Referenced by

- Called by: [sub_140206CE8](sub_140206CE8.md)

## Notes

sub_140206C14 reads the other byte of the pair (byte_1406735A8[2 * charge]) and sets motion 3 when the charge byte is 0.

## Open questions

None recorded.
