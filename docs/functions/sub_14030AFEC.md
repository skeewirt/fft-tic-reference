# sub_14030AFEC

- **Address:** `0x14030AFEC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void sub_14030AFEC(void)`
- **Callers:** Battle_ResolveAction
- **Callees:** sub_140278FA8, sub_14030DD1C, sub_140278E68, Item_GetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A post-resolution reaction helper: after an action resolves it can queue one of a small set of reaction abilities
for the acting unit, under a set of command, unit-flag and item-category conditions.

## Behavior

- V: it returns immediately when the battle state dword at `0x14186AF9C` is nonzero.
- V: it returns when the byte at battle context +0x18 is 7 or `0x6A`.
- V: it returns when the 16-bit word at context − 8 is set while the word at context − 6 is zero.
- V: it loads the acting unit from `0x14186AF68` and the action block from `0x14186AF70`.
- V: when the unit's byte at +0x65 has bit 2, the word at context − 8 is zero, the byte at context +6 is not `0x15`
  and the byte at context +0x29 has bit `0x80`, it writes ability `0x1B8` at action +0x10, copies the word at
  context +8 into action +0x28, clears action +0x2C and action +0, and sets action +2 to 9.
- V: it returns when action +0x10 is already set or when the state dword is nonzero.
- V: it calls sub_140278FA8 with the unit and the constant 4, then sub_14030DD1C; a nonzero result from either ends
  the function.
- V: when the unit's byte at +0x97 has bit 4 and the byte at context +0x2A has bit `0x10`, it writes 100 minus the
  unit's byte at +0x2B into action +0x2C, then calls sub_140278E68 with 100 and that same unit byte.
- V: the same branch then stores ability `0x1C3` at action +0x10 and sets action +2 to `0x0B`.
- V: when +0x97 has bit 2 instead, the function requires the byte at context +0x27 to have bit `0x20` and the item id
  at context +0xA to name an item whose equip-category byte is `0x0B` or `0x0C`.
- V: that second branch does the same CT arithmetic, then stores ability `0x1C4` and sets action +2 to 4.
- V: both branches refuse to run while the dword at `0x14186AF80` is nonzero, and check it again after the call.
- I: the two abilities are reactions, because they lie in the reaction range of the ability id space and the block
  fields written are the ones an action queue uses.
- I: 100 minus the unit byte is a CT spend, because 100 is the CT scale and the value is written into the action
  block the queue reads.
- ?: which reaction each of the two branches represents.
- ?: what the byte at context +0x18 and the word pair before the context mean.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md)
- Reads: [g_BattleActingUnit](../globals/g_BattleActingUnit.md), [g_BattleActionBlock](../globals/g_BattleActionBlock.md), [g_BattleContextGate](../globals/g_BattleContextGate.md), [g_BattleStateGate](../globals/g_BattleStateGate.md)
- Writes: [g_BattleActionBlock](../globals/g_BattleActionBlock.md)

## Referenced by

- Called by: [Battle_ResolveAction](Battle_ResolveAction.md), [sub_1403099B0](sub_1403099B0.md)

## Notes

- V: the context offsets +0x18, +0x27 and +0x2A are absolute RIP operands of the block based at 0x1407B0770 (0x1407B0788, 0x1407B0797 and 0x1407B079A); base+offset is folded into each displacement, so the literal offsets do not appear as operands.
- V: the whole function was read; the three helper calls were not.

## Open questions

None recorded.
