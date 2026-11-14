# BTurn_QueueInvisibilityEnd

- **Address:** `0x14030C240`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 BTurn_QueueInvisibilityEnd(_BYTE *unit)`
- **Callers:** Battle_TurnEngine (two calls)
- **Callees:** Battle_ResultReset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Queues the removal of Invisibility from a unit whose turn has ended, when the other conditions hold.

## Behavior

- V: returns 0 when the unit row is empty, or the unit is Crystal, KO or Jumping (mask 0x64 of +97) or Stone or Chest (mask 0x81 of +98).
- V: otherwise points g_BattleActingUnit and g_BattleActionBlock at the unit and its result block, resets the result block (Battle_ResultReset), and when the turn-ended byte +442 is set, bit 0x10 of the battle-applied byte +497 (Invisibility, id 19) is set and +0x2E is not zero, it sets the pending-remove byte at block +36 to 0x10 and the result flag at block +39 to 8.
- V: returns the result flag at block +39 (0 when nothing was queued).
- I: +0x2E is the byte Battle_StatusApply clears when it applies Invisibility; what it counts is not decoded.

## Notes

Name is ours.

## Open questions

? what the byte +0x2E holds.
