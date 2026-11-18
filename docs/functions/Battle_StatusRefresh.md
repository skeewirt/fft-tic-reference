# Battle_StatusRefresh

- **Address:** `0x14030CA00`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Battle_StatusRefresh(int slot)`
- **Callers:** `Battle_StatusResolve` (`0x14030A518`..`0x14030A9C5`), `Battle_StatusApply` (`0x14030C93C`)
- **Callees:** `Unit_SetStatusCountdown`, `BattleUnit_SetStatusVisual`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the pending status clears of a unit and recomputes the effective 40-bit status set.

## Behavior

- V: `rec = g_BattleUnitTable + 512*slot`.
- V: for each of the 40 bits in the pending clears `rec+0x1E0..0x1E4`: clear the bit in `rec+0x1EF..0x1F3`,
  call `Unit_SetStatusCountdown(rec, status, 1)`, and (unless previewing) update the status icon with
  `BattleUnit_SetStatusVisual(status+1, 0, slot)`.
- V: finally `rec[0x61+i] = rec[0x57+i] | rec[0x1EF+i]` for i = 0..4, i.e. the effective statuses are the
  innate statuses OR the battle-applied statuses.
- V: the status id -> bit mapping is MSB first: bit `0x80 >> (id & 7)` of byte `id >> 3`.

## State touched

- Calls: [BattleUnit_SetStatusVisual](BattleUnit_SetStatusVisual.md)

## Referenced by

- Called by: [Battle_StatusApply](Battle_StatusApply.md), [Battle_StatusResolve](Battle_StatusResolve.md)
- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md), [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md), [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)

## Notes

`Battle_StatusResolve` (`0x14030C87C`) is the wrapper: it saves/restores the pending sets, calls
`Status_FilterPendingSets`, `Battle_StatusRefresh` and `Battle_StatusApply`, then applies the Dead status'
side effects (`+0x30 = 0` when status 2 is set, `+0x18D = 0xFF` when none of statuses 0/2/3 are set).

## Open questions

None.
