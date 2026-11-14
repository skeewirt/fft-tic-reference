# Errand_IsAvailable

- **Address:** `0x1402CCE20`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `bool Errand_IsAvailable(int errandIndex, int town)`
- **Callers:** `sub_1402EE0A4`, `sub_1402EE0F0` (board builders)
- **Callees:** Errand_LoadRecord, EventVar_Read, `sub_1402CD168`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether an errand is offered at a town right now.

## Behavior

- V: loads the errand record; if its town word (16) is non-zero it must equal the given town.
- V: condition bit 0: event variable 111 (story progress) must be at least the record's story threshold (word 21).
- V: condition bit 1: a pair of world values (event variables 46 and 47) is converted and its first value must equal the record's reference word (22).
- V: condition bit 2: event variable 864 + reference (word 22) must have bit 4 set, i.e. the prerequisite errand has been completed with success.
- V: all active conditions must hold; otherwise it returns false.

## State touched

- Calls: [Errand_LoadRecord](Errand_LoadRecord.md), [EventVar_Read](EventVar_Read.md), [sub_1402CD168](sub_1402CD168.md)

## Referenced by

- Called by: [Errand_BuildBoardEntry](Errand_BuildBoardEntry.md), [Errand_IsOffered](Errand_IsOffered.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md), [TavernErrandsOpenAtSituationCounter450](../behaviors/TavernErrandsOpenAtSituationCounter450.md)

## Notes

Bit 2 of the condition flags reuses the reference word as a prerequisite errand number, bit 1 reuses it as a world value.

## Open questions

What the conversion in `sub_1402CD168` represents.
