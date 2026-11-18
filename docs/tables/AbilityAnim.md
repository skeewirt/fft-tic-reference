# AbilityAnim

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140672DA0`
- **Rows:** 454 rows of 3 bytes
- **Keyed by:** ability id 0..453
- **Read by:** [BattleAct_SetupEffect](../functions/BattleAct_SetupEffect.md), [sub_1402059AC](../functions/sub_1402059AC.md), [sub_140206CE8](../functions/sub_140206CE8.md), [sub_14020CC50](../functions/sub_14020CC50.md)
- **Held in:** [g_AbilityAnim](../globals/g_AbilityAnim.md)
- **Row layout:** [AbilityAnimRow](../structs/AbilityAnimRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle presentation of each ability: charge type, execution motion and text selector.

## Behavior

- V: the effect word and this table are indexed by the same ability id; an id of 454 or more reads past the table and 512 is the no-ability sentinel.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: meaning of the text selector values
