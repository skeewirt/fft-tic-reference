# g_FastForwardStateTable

- **Kind:** global
- **Address:** `0x142FCF730`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint8[256]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per battle state (index g_BattleState): non-zero = fast-forward allowed. Filled with 1, then loaded from GameModeTypes (NXD 88) row byte +16 by sub_1401E9E10.

## Referenced by

- Described by tables: [FastForwardStates](../tables/FastForwardStates.md), [GameModeTypes](../tables/GameModeTypes.md)

## Open questions

None recorded.
