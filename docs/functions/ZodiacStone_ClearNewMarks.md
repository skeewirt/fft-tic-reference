# ZodiacStone_ClearNewMarks

- **Address:** `0x14016BF68`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ZodiacStone_ClearNewMarks(void)`
- **Callers:** not recorded
- **Callees:** UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the new mark of every ZodiacStone row that is met.

## Behavior

- V: the same walk; for every met row it clears the byte at save block +6608 + 4 * set + index.
- I: the save block therefore holds a 4-byte-per-stone array of row marks at +6608 (see SaveBlockUiMarks).

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md)

## Open questions

None recorded.
