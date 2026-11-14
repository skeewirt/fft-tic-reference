# g_BattleMapWords

- **Kind:** global
- **Address:** `0x140D3F950`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint16[]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The runtime per-map word table. It is indexed by scene variable 39 and filled at map load from a static map record table; the battle message and skip code reads it.

## Behavior

- V: readers index it as word_140D3F950[SceneVar(39)].

## Referenced by

- Read by: [sub_14020261C](../functions/sub_14020261C.md), [sub_140204B78](../functions/sub_140204B78.md)

## Open questions

None recorded.
