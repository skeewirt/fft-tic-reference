# TextReferenceIsABankAndAnElevenBitIndex

- **Kind:** observed behaviour
- **Scope:** engine (event text lookup)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [EventText_FindMessage](../functions/EventText_FindMessage.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An event message is named by a 16-bit reference: the top five bits select one of 32 text banks (each a resource), the low 11 bits are the message index inside it; the lookup counts message terminators from the start of the bank, so its cost grows with the index.

## Behavior

- V: bank = (reference >> 11) and 0x1F, pointer = the bank table entry at 0x14184A8A0 + 8 x bank; bank 14 and bank 22 (0xB000) are fetched from resource slots; the others are read from the pointers the loaders set (sub_14032A8A0 and the screens that load their own text).
- V: the message is found by stepping through the bytes of the bank and counting terminator codes (bytes 0xFE and 0xFF) until the count equals the message index (reference and 0x7FF); a bank holds at most 2,048 messages by this rule.
- V: callers pass 16-bit values (list items are 16-bit words); no caller was seen passing a wider reference.

## Notes

The errand board and the tavern lists store these references as their list items.

## Open questions

? which banks hold which screens' text (banks 3, 4, 5, 10, 16, 21 and 26 have no static writer).
