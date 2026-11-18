# EventText_FindMessage

- **Address:** `0x1402DDBC8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint8_t *EventText_FindMessage(int messageRef, int64_t context)`
- **Callers:** About 19 callers, including EventMessage_Scripted and `sub_14032D31C`.
- **Callees:** `sub_140332B48`, `sub_1402BACCC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds an event message in memory from its packed 16-bit reference and returns a pointer to the start of its text.

## Behavior

- V: the top 5 bits of the reference (`ref >> 11`) pick a text bank from a 32-entry table of bank pointers at `qword_14184A8A0`.
- V: bank 14 is fetched through `sub_140332B48` (with the context argument); a reference whose top bits are 0xB000 (bank 22) first calls `sub_1402BACCC(9)` and then uses the pointer in `qword_14375F938`.
- V: the low 11 bits are the message index within the bank: the routine walks the bank byte by byte and counts bytes whose value, ignoring the lowest bit, is 0xFE (so 0xFE and 0xFF), stopping when the count equals the index.
- V: returns the position after that many terminators, which is the first byte of the requested message.
- I: 0xFE and 0xFF are the end-of-message markers; the two special banks are loaded or built on demand.

## State touched

- Calls: [sub_140332B48](sub_140332B48.md)

## Referenced by

- Called by: [BattleCommand_BuildUnitList](BattleCommand_BuildUnitList.md), [EventMessage_Scripted](EventMessage_Scripted.md), [sub_1401DF120](sub_1401DF120.md), [sub_1402DF374](sub_1402DF374.md), [sub_14036A294](sub_14036A294.md), [sub_140371550](sub_140371550.md)
- Observed behaviours: [AbilityTextKeysPast2047](../behaviors/AbilityTextKeysPast2047.md), [TextReferenceIsABankAndAnElevenBitIndex](../behaviors/TextReferenceIsABankAndAnElevenBitIndex.md)
- Reads file formats: [TextId](../formats/TextId.md)
- Resolves registries: [TextIdKinds](../registries/TextIdKinds.md)

## Notes

Pairs with EventText_NextChar: this finds where a message starts, that routine steps through it.

## Open questions

What `sub_140332B48` and `sub_1402BACCC` load for banks 14 and 22.
