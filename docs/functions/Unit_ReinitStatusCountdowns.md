# Unit_ReinitStatusCountdowns

- **Address:** `0x140278600`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Unit_ReinitStatusCountdowns(void *unit)`
- **Callers:** Unit_BuildInnateStatuses, sub_1402788EC
- **Callees:** Unit_SetStatusCountdown

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Re-initialises the countdown bytes of a unit after its innate status set has been rebuilt: it merges the saved innate status bytes into the effective set and starts a duration for every battle-applied status that has none.

## Behavior

- V: unit +0x9E bit 3 sets bit 0x40 of unit +0x59 before anything else.
- V: five bytes are processed in one loop: for i 0..4 the innate byte at +0x57+i is ORed with the saved byte at +0x1EF+i into the effective byte at +0x61+i, and the innate bit is cleared from the group byte at +0x5C+i; the loop walks one pointer over +0x5C with displacements -5, +0x193 and +5.
- V: the battle-applied set starts at +0x1EF; the bit for status id s is in byte +0x1EF+(s>>3), so the ids below test the bytes at +0x1EF+3 and +0x1EF+4.
- V: a status whose bit is set in the battle-applied set at +0x1EF and whose countdown byte at +0x66 is still zero gets a new duration through Unit_SetStatusCountdown(unit, id, 0).
- V: the loop covers status ids 24 through 39 (0x28), one countdown byte each at unit +0x66 onward.
- I: the function is the "second half" of the innate-status build: the first half writes the sets, this one repairs the countdowns that the rewrite disturbed.
- ?: whether a status already present with a non-zero countdown keeps it; the code only starts one when the countdown byte is zero.

## State touched

- Writes: [UnitWorkRecord](../structs/UnitWorkRecord.md)

## Referenced by

- Called by: [Unit_BuildInnateStatuses](Unit_BuildInnateStatuses.md), [Unit_InitBattleStatusState](Unit_InitBattleStatusState.md)
- Observed behaviours: [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md), [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)

## Notes

Whole function read (134 bytes). Called from the innate builder and from its reload twin.
V: it starts countdowns only for +0x1EF bits, never from +0x61 (its loop runs from the +0x5C base: +0x57 is -5 and +0x61 is +5 from it).

## Open questions

None recorded.
