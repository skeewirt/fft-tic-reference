# BattleWeaponHitSoundCues

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140672C60`
- **Rows:** 3 rows of 32 bytes
- **Keyed by:** row 0..2, weapon type 0..31
- **Read by:** [sub_140269554](../functions/sub_140269554.md)
- **Row layout:** [WeaponHitSoundCuesRow](../structs/WeaponHitSoundCuesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sound cue (+1) played when an attack effect hits, per weapon type, in three variants. Verdict: designer-data.

## Behavior

- V: the weapon type is byte +5 of the item record of the effect's item id; 35 is mapped to 3 and any other value of 32 or more to 1
- V: the stored byte minus 1 is the cue number given to the sound player
- I: row 1 is used on the single-target branch, row 2 when the struck unit has a zero flag byte

## Notes

Our names. Tags: V layout, V reader, I variant meaning.

## Open questions

- ?: which situations pick row 1 and row 2
