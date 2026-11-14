# PartyUnit_FillFromWorkRecord

- **Address:** `0x140360048`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void PartyUnit_FillFromWorkRecord(UnitWork *c, PartyUnit *b)`
- **Callers:** 2
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a party record B from a work record C alone (the per-job arrays come from C).

## Behavior

- V: copies the unlock mask byte-swapped (C +159..161 -> B +120..122), learned bits, levels, JP and total JP in 16-byte blocks.
- V: fixes JP and total JP of the current job to at least the value it already had (two compares per word).

## Open questions

None recorded.
