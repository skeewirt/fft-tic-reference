# BattleItemsAreUsedThroughItemAbilities

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Ability data](../areas/ability-data.md)
- **Affects:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle item is used through an Item ability: the Chemist's Items command lists skillset 6's abilities 368..381 as items through the kind1 table, and the action's ability word is item + 0x80.

## Behavior

- V (code): the Items list (Unit_ListItemCommandItems) is command id 6 only, abilities 368..381 mapped to item bytes by the u8 kind1 table, a byte list ending in 0xFF; the menu copies it into a u16 list; the request carries the item as u16 at +8; the action word is item + 0x80 (0x140281727), read back as a 10-bit id; formulas 72, 73, 75 and the recovery preview rebuild the item from g_FormulaBlock +0x0E as byte + 0xF0.

## Open questions

None recorded.
