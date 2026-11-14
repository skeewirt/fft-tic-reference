# AbilityListWordsCarryFlags

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Ability data](../areas/ability-data.md)
- **Affects:** [sub_140333338](../functions/sub_140333338.md), [sub_140366FE0](../functions/sub_140366FE0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An ability list word holds the ability id in bits 0..9 and flags above it (0x800 equipped or innate, 0x1000 learned, 0x4000 greyed); every consumer strips them with & 0x3FF before the id is stored or looked up. Widening such a mask for item ids leaks the flags into the stored ability word.

## Behavior

- V: sub_140333338 tests 0x4000, 0x1000 and 0x800 on the word, then stores word & 0x3FF through sub_14028916C; sub_1403333F0 ORs 0x1000 into a combat-set word before calling it.
- V (live 2026-11-10): with the mask widened to 0xFFFF, the reaction ability 514 was stored as 0x1202 in the party and save records; the mask and sub_140366FE0's two (help key 0x7800 + id, history entry) are 0x3FF.
- I: ability ids above 1023 need the flags moved out of the word first.

## Open questions

None recorded.
