# Party_EggUpkeep

- **Address:** `0x140289900`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void Party_EggUpkeep(void)`
- **Callers:** sub_1402CCEE0
- **Callees:** EventVar_Read, sub_14027528C, sub_140278B24, sub_140279328, sub_1402CD168, sub_1403D325C, sub_1403D3AE8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-step upkeep of monster eggs over the 54 save slots: counts down existing eggs and hatches them, and may also create a new egg from a monster that carries an Egg key. The name (I) covers the hatch part only; the function does both.

## Behavior

- V: seeds a random generator state from event variables and a fixed constant, then loops save slots 0..0x35, skipping empty ones (slot id byte A+1 = 0xFF).
- V: for a unit with the egg flag (A+4 bit 2), decrements the low nibble of A+5; when it reaches zero the flags are set to 0x20, event variables 46 and 47 are read, a value is written into the word at A+5, and an egg-hatched notification object is posted.
- V: for other units, reads the Job row (table 46) of the unit's job (A+2); a nonzero dword at row +52 marks the unit as an egg parent candidate and its slot index is added to a candidate list.
- V: with at least one candidate, one random byte decides a stage: below 6 gives stage 3, below 16 gives stage 2, below 32 gives stage 1, otherwise nothing happens.
- V: a random candidate's job row +52 is the key into the Egg table (id 310); Egg row +8 / +12 / +16 (job / job_2 / job_3) gives the new monster's job id for stage 1 / 2 / 3.
- V: a free save slot is found with sub_14027528C; the new unit gets the job id at A+2, the egg flag (A+4 bit 2), and a random value 0..3 at A+288.
- I: Egg row +20 acts as a modulus: n = random % value + 1 (minimum 2); the egg timer stored at A+5 is 17 * n (reset to 1 when above 0x16D).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [sub_1402CD168](sub_1402CD168.md)

## Referenced by

- Called by: [sub_1402CCEE0](sub_1402CCEE0.md)
- Reads tables: [NxdDataEgg](../tables/NxdDataEgg.md)

## Notes

Also known as Party_HatchEggMonster (earlier proposal; renamed because the function creates eggs as well as hatching them).

## Open questions

Exact meaning of the value written to A+5 on hatch (built from event variables 46 and 47).
