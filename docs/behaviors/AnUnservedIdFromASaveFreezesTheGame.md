# AnUnservedIdFromASaveFreezesTheGame

- **Kind:** observed behaviour
- **Scope:** loading a save whose item ids have no row
- **Area:** [Save data](../areas/save-data.md)
- **Affects:** [Unit_ApplyEquipment](../functions/Unit_ApplyEquipment.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The game trusts every id in a save: an equipped item with no item row reaches the unit stat builder, which reads the armor record it does not get and faults inside a game task, freezing the game.

## Behavior

- V: seen live 2026-11-11: slot 50 held items 300 and 3000 (no item row) in two units' hands (save record +0x14); walking into the Dorter story battle faulted at 0x140277B94 in Unit_ApplyEquipment (a byte read through the null result of Item_GetArmorRecord for that id) in a game task; the game froze (no dump; the fault was seen live).

## Open questions

? other unchecked ids of a save the game trusts the same way (a job or skillset word with no row).
