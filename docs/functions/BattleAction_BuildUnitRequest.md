# BattleAction_BuildUnitRequest

- **Address:** `0x140283280`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleAction_BuildUnitRequest(void *unit, uint8_t command, uint16_t action, int preview)`
- **Callers:** Battle_PreviewUnitAction, sub_140282E38
- **Callees:** BattleRange_MarkRing, BattleAction_ApplyRequest

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes a command and action word into a unit action block, optionally marks the ring, and applies the request through the common wrapper.

## Behavior

- V: the unit action block is at unit +0x1A0; the command byte goes to +1 and the action word to +2.
- V: when the preview argument is non-zero it calls BattleRange_MarkRing on the block and rejects a result of -1.
- V: a ring result of 0 or 1 is also rejected, and the function returns -2.
- V: it then reads the acting unit slot from the global current-unit word, takes the unit level byte and checks the action record flags.
- V: the block fields at +0xA, +0xB, +0xC and +0x10 are filled with 5, a global byte, the level-derived word and the action record value.
- V: BattleAction_ApplyRequest is called on the block and its result is returned.
- V: the two callers are the preview refresh and the second action path, both in battle.
- I: the routine builds a request that has not been consumed yet; the consume step lives in the apply wrapper and its callee.
- ?: the meaning of the -2 return; the callers treat it as a refusal but the reason is not named.

## State touched

- Calls: [BattleRange_MarkRing](BattleRange_MarkRing.md), [BattleAction_ApplyRequest](BattleAction_ApplyRequest.md)
- Reads: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)
- Writes: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Referenced by

- Called by: [Battle_PreviewUnitAction](Battle_PreviewUnitAction.md)

## Notes

Whole function read (265 bytes). The field writes and the two calls are the commit step of the item flow.

## Open questions

None recorded.
