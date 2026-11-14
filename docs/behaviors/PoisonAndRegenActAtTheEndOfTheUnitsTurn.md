# PoisonAndRegenActAtTheEndOfTheUnitsTurn

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_TurnEngine](../functions/Battle_TurnEngine.md), [Battle_ApplyActionResult](../functions/Battle_ApplyActionResult.md), [ActionResult.hp_damage](../structs/ActionResult.md#hp_damage), [ActionResult.hp_heal](../structs/ActionResult.md#hp_heal), [ActionResult.kind_bits](../structs/ActionResult.md#kind_bits)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Poison and Regen change HP when the turn of the unit ends: Battle_TurnEngine phase 19 writes max HP / 8 as damage (Poison) or as a heal (Regen, only when not poisoned) into the result block of the unit, which the game then applies as an action result. A unit that is Crystal, KO, Jumping, Stone or Chest is skipped.

## Behavior

- V (code read, 0x14030F595..0x14030F634): after the units of the turn are finished the engine goes to phase 19; for the active unit it resets the result block, then +0x64 bit 0x80 (Poison) writes max HP >> 3 at +6 and 0x80 at +0x27, else bit 0x40 (Regen) writes max HP >> 3 at +8 and 0x40; a non-zero +0x27 returns the unit with 0x300 so the result is applied.
- V (data): the text of the game for Poison (UIStatusEffect 25) says the damage comes at the end of the turn of the unit.
- I: with max HP below 8 the change is 0 (the shift floors).

## Open questions

? live: the order of the Poison damage and the Invisibility / terrain steps (phases 15, 17) in one turn end.
