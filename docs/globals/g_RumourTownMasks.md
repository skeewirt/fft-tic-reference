# g_RumourTownMasks

- **Kind:** global
- **Address:** `0x1407BE620`
- **Type:** `event system`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

uint32[64]: per rumour id, the towns whose tavern may list it: bit (0x4000 >> town) for towns 0..14; read only by TavernRumour_IsAvailable (rows 0..21 are set, 22..63 are zero). The table after it is tbl_DissolveOffsets (0x1407BE720).

## Referenced by

- Observed behaviours: [TavernRumoursListGossipRowsByIdTownMaskAndUnlockVariable](../behaviors/TavernRumoursListGossipRowsByIdTownMaskAndUnlockVariable.md)

## Open questions

None recorded.
