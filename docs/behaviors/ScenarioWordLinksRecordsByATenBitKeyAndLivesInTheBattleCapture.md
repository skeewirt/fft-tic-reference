# ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture

- **Kind:** observed behaviour
- **Scope:** engine (scenario setup, battle capture)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [Scenario_CheckBattleRecord](../functions/Scenario_CheckBattleRecord.md), [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md), [EventScript_SkipTick](../functions/EventScript_SkipTick.md), [EventScript_Run](../functions/EventScript_Run.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The scenario setup records are turned into one 16-bit word per EVENT NUMBER (an 887-word array indexed by scene variable 39); a word holds a 10-bit link to another record by event number plus flag bits, and the battle capture and restore copy the 887 words at a fixed place.

## Behavior

- V: the builder walks the records until the first one whose event number is 0 (or 887 records) and stores, for each, the word byte +18 + (byte +19 << 10), OR byte +20 << 8 (16 bits), at the index given by the record's OWN event number, not its row.
- V: the mid-event refresh finds the linked record by the key (word and 0xFF) plus ((word shifted right 2) and 0x300): the link has 10 bits, 0 to 1,023; bits 8, 9 and 12 to 15 are flags, tested together with the mask 0xF300 by three battle functions and by the event runner, and the word is also tested for sign and for zero.
- V: sixteen instructions address the array (census of the whole image): ten index it by an event number (scene variable 39 or the message index global) with no bound, two are the capture copies, six write words 400..404 directly after the builder loop (401 = 0, 402 = 8000h, 403 = 0, 400 and 404 = 8000h or 8200h by scene variable 510).
- V: the battle capture and the restore copy the 0x6EE bytes (887 words) into the capture block at 0x14081CCF2, directly after the 0x2800-byte event script buffer and directly before the next captured byte at 0x14081D3E0.
- V: the row bound 0x377 is an immediate in three places: the battle record check (cmp), and two loads into a register in ScenarioSetup_ApplyRecord, the second of which bounds both the word builder and the record search after it.
- V: the event number is read as byte0 | (int16)(byte1 << 8), sign-extended: a number of 32,768 or more never matches var 39 and would index the word array negatively.

## Notes

The row count and the word array length are the same constant, but they bound different things: rows (the loop bounds) and event numbers (the array index).

## Open questions

? whether any save slot (as opposed to the battle capture) carries the array.
