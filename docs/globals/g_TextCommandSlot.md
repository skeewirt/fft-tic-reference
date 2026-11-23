# g_TextCommandSlot

- **Kind:** global
- **Address:** `0x140D40940`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `ptr`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The callback slot the battle text command installs: sub_140243390 is stored here and every branch of the text dispatcher calls it.

## Behavior

- V: sub_140243330 writes the slot and then calls the dispatcher.

## Referenced by

- Written by: [BattleTask_ActorForecastPanel](../functions/BattleTask_ActorForecastPanel.md), [sub_140243330](../functions/sub_140243330.md)

## Open questions

None recorded.
