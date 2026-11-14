# AbilityTextKeysPast2047

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Ability data](../areas/ability-data.md)
- **Affects:** [sub_140226208](../functions/sub_140226208.md), [EventText_FindMessage](../functions/EventText_FindMessage.md), [BattleMsg_ResolveEntry](../functions/BattleMsg_ResolveEntry.md), [sub_1403015A4](../functions/sub_1403015A4.md), [sub_140301ED8](../functions/sub_140301ED8.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The game names an ability by the 16-bit key pool << 11 | id (11 bits).

## Behavior

- V (code): the ability text keys are 0x7000 + id (name, pool 14) and 0x7800 + id (help, pool 15); sub_140226208 takes 11 bits of the id, so 2047 is the last id with its own key.
- V (code): 44 producers build 0x7000 / 0x7800 + id; 32-bit carriers (S3, S5, the event queue) pass a 32-bit key, 16-bit ones (the S6 command cells, the timeline string arrays, the crystal list) truncate it; readers test (key & 0xF800) == 0x7000 and take id = key & 0x7FF; the info-window dword reads a negative value as none.
- V (code): the help arrays read the word 0x7FF as none, so ability id 2047 is reserved; ability ids are loaded sign-extended in many places, so the ceiling is 0x7FFF.
- V (code, live 2026-11-12): the banner message row is pool * 1000 + (key & 0x7FF) (BattleMsg_IdFromDescriptor, BattleMsg_ResolveEntry), so the game's text names an ability by key only below 1000: a derived row for ability 2015 replaced the 'Wait' banner (row 16015).

## Open questions

? the set-C crystal window (sub_140364408); the writers of the static help arrays (word_14186AF14 / 1E / 22).
