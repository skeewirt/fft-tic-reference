# ZodiacStone_AnyMetAndNew

- **Address:** `0x14016BDB8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool ZodiacStone_AnyMetAndNew(void)`
- **Callers:** not recorded
- **Callees:** UserSituation_IsMet

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tells whether any ZodiacStone row is met and still carries its new mark.

## Behavior

- V: the same walk as ZodiacStone_AnyMet; returns 1 at the first row whose user_situation is met and whose byte at save block +6608 + 4 * set + index is non-zero.
- I: that byte is the row's 'new' mark (see SaveBlockUiMarks).

## State touched

- Calls: [UserSituation_IsMet](UserSituation_IsMet.md)

## Open questions

None recorded.
