# TerrainProperties

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x14067F750`
- **Rows:** 2 blocks of 64 bytes
- **Keyed by:** terrain type 0..63
- **Read by:** [BTurn_QueueTerrainPoison](../functions/BTurn_QueueTerrainPoison.md), [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [BattleRange_MarkRing](../functions/BattleRange_MarkRing.md)
- **Row layout:** [TerrainPropertiesRow](../structs/TerrainPropertiesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two 64-byte blocks indexed by terrain type: the ability id the terrain gives and a flag byte whose bit 0x80 marks harmful terrain. Verdict: designer-data.

## Behavior

- V: the tile type of the unit's tile (bits 0..5 of the tile table byte) indexes both blocks
- V: BTurn_QueueTerrainPoison returns at once when the flag byte has no 0x80 bit

## Notes

Our names. Tags: V layout, V reader, I ability meaning.

## Open questions

- ?: which terrain types carry the flag
