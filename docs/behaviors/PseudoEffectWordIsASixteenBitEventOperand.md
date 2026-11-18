# PseudoEffectWordIsASixteenBitEventOperand

- **Kind:** observed behaviour
- **Scope:** engine (effect selection)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Effect_SelectForAbility](../functions/Effect_SelectForAbility.md), [EventScript_Run](../functions/EventScript_Run.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An effect word of 512 or more selects a row of the 37-word pseudo effect table (row = word - 512, row 0 when 37 or more) and the effect number is masked to 9 bits; event command class 0x18 sets the word, which the event state keeps as a 16-bit value with -1 meaning none.

## Behavior

- V: Effect_SelectForAbility compares the effect word with 512 as a SIGNED int; for a word of 512 or more it tests word - 512 below 0x25 (an immediate byte, so at most 127 could ever be encoded there) and takes that row, else row 0; words below 512 use the ability effect number table (bound 0x1C6, else row 0). A negative word (0x8000..0xFFFE as a 16-bit value) takes the ability branch and row 0, never the pseudo table.
- V: the class 0x18 case of EventScript_Run builds its operand as a 16-bit little-endian word from the script bytes 1 and 2 and stores it as a word at 0x140D40930; the event state snapshot copies it as a 16-bit value at +554; the effect starter (sub_14023A0B4) reads it with a sign extension, treats -1 as none and otherwise passes it as an int to EventEffect_Start, which calls Effect_SelectForAbility.
- V (2026-11-16): so the highest word that reaches the pseudo table from an event script is 32,767, which is row 32,255; BattleAct_SetupEffect also passes the action's ability number as the effect word (a stock ability number is below 512).
- V: the number read from the row is a 16-bit value: a negative one (bit 15) means no effect, and the number is masked with 0x1FF (nine bits) after that test, so bits 9..14 are ignored.

## Notes

Two other callers pass constants below 512.

## Open questions

? which stock scripts use the command, and whether any word above 548 occurs in them.
