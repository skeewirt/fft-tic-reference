# MoveFind_ApplyTrap

- **Address:** `0x14030C39C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int MoveFind_ApplyTrap(BattleUnit *unit)`
- **Callers:** sub_14020435C
- **Callees:** MoveFind_ProbeTile, Battle_ResultReset, Status_FilterPendingSets

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the trap of a unit's tile to the unit as an action result.

## Behavior

- V: makes the unit the acting unit, resets its action result block (+446) and switches on the trap kind reported by MoveFind_ProbeTile.
- V: kind 0 sets a result flag and a value of 256.
- I: kind 0 is Degenerator (a level loss), by elimination.
- V: kind 1 inflicts status 39 Doom; kind 2 inflicts status 35 Sleep; kind 3 deals damage equal to max HP / 5.
- I: kinds 1, 2 and 3 are Death Trap, Sleeping Gas and Steel Needle (matched by effect).
- V: kinds 4, 5 and 6 also exist here and set one status bit each, but the Move-Find flags only produce kinds 0..3.
- I: those bits are statuses 16 Oil, 24 Poison and 3 Undead, by the status byte order.
- V: a status kind first asks Status_FilterPendingSets; when it refuses, the result becomes a miss.

## State touched

- Calls: [MoveFind_ProbeTile](MoveFind_ProbeTile.md)

## Referenced by

- Reads tables: [MoveFindItems](../tables/MoveFindItems.md)

## Open questions

?: the exact meaning of kind 0's value; whether anything else can start kinds 4..6.
