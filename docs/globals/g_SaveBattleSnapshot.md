# g_SaveBattleSnapshot

- **Kind:** global
- **Address:** `0x1408167A0`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `uint8[668112]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle snapshot buffer: 668,112 bytes of sparse live battle state (unit table, tile table, scene-task records, action state) captured for a kind-1 resume payload.

## Behavior

- V: the payload builder copies this block and the materialiser copies it back.

## Referenced by

- Read by: [sub_140217EF8](../functions/sub_140217EF8.md)
- Written by: [sub_1402181EC](../functions/sub_1402181EC.md)

## Open questions

None recorded.
