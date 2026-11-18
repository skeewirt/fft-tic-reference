# Errand_RollBonusLoot

- **Address:** `0x1402D3120`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void Errand_RollBonusLoot(void)`
- **Callers:** Errand_ComputeRewards
- **Callees:** EventVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

On a successful errand (grade 0) picks a treasure or a random bonus and adds its JP and gil to the result.

## Behavior

- V: does nothing unless the grade is 0; clears the loot kind and the bonus gil first.
- V: treasure pool 1 (loot kind 1) lists the unowned items among event variables 801..831 and picks one uniformly; if all are owned it picks any of the 31. Pool 2 (kind 2) does the same over variables 848..863 (16 entries).
- V: for a treasure the category selects a pair from a table: one tier adds JP to every unit and the other sets the bonus gil.
- V: otherwise, when the bonus-roll word is 1, it rolls 0..99: 60 percent tier 0, 30 percent tier 1, 10 percent tier 2 (loot kind 3), and uses row 3 x (category - 1) + tier of a second pair table in the same way.
- V: the random value comes from the game's shared xorshift generator (15 bits of its output).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md)

## Referenced by

- Called by: [Errand_ComputeRewards](Errand_ComputeRewards.md)
- Reads tables: [ErrandBlob](../tables/ErrandBlob.md)

## Notes

The chosen treasure index is stored for Errand_ApplyResult.

## Open questions

None recorded.
