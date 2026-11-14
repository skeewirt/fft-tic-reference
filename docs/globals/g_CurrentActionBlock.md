# g_CurrentActionBlock

- **Kind:** global
- **Address:** `0x1418716A0`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[?]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The current-action block Action_BuildCurrentAction fills for the AI and the action preview: command at +0, packed action word at +2, item id at +6, flags at +0x10 and the ability aux flags further in.

## Behavior

- V: the builder clears the first sixteen bytes and the dwords at +0x10 and +0x20, then stores the command, the word, the item id and the flags.

## Referenced by

- Read by: [BattleRange_ApplyShape](../functions/BattleRange_ApplyShape.md), [BattleRange_MarkRing](../functions/BattleRange_MarkRing.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md)
- Written by: [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md)

## Open questions

None recorded.
