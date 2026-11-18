# StoryEventListBuildsASharedBoardArrayFromBitVariablesAndHoldsTextReferences

- **Kind:** observed behaviour
- **Scope:** engine (tavern list pages, story event list)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventViewer_BuildList](../functions/EventViewer_BuildList.md), [EventViewer_IsHidden](../functions/EventViewer_IsHidden.md), [EventViewer_ListInput](../functions/EventViewer_ListInput.md), [EventViewer_OpenEntry](../functions/EventViewer_OpenEntry.md), [EventViewer_EntryPage](../functions/EventViewer_EntryPage.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A list of replayable story events has 78 entries: 64 plain ones that read event variables 444 to 507 and 14 special ones that read 427 to 440 (only 430, 433 and 440 can be listed); a listed entry is a 16-bit text reference (bank 29, message index 0 to 77) appended to a 128-entry array that other tavern lists share; the confirm starts the story event named by a 78-word table indexed by the message index.

## Behavior

- V: the builder walks positions 0 to 77; the positions 14, 16, 28, 33, 47, 61, 62, 63, 64, 65, 66, 75, 76 and 77 are special (a chain of compares with constants) and read event variable 427 plus their own count; the other 64 read 444 plus theirs. All of these are single-bit variables (the variable space has 32-bit cells below 128, bits from 128 to 863 and nibbles from 864 to 1023).
- V: an entry is listed when its variable is nonzero and the helper that hides eleven special variables (427, 428, 429, 431, 432, 434 to 439) says no; the list item is the variable number minus 6588 (plain, 0xE800 plus 0 to 63) or minus 6507 (special, 0xE840 plus 0 to 13) as an unsigned 16-bit value.
- V: an item is a text reference: bits 11 to 15 name the text bank (29) and bits 0 to 10 the message index; the page text is the message index plus 59392, and the confirm reads the event number from the table at 0x1407B81B0 with the message index (a 16-bit read; entry 67 holds 0xFFFF, no event).
- V: the builder stores each item in the array at 0x140D498F0 and a zero in the parallel array at 0x140D497D0 (128 words each) with a range check at a byte offset of 0x100; the same two arrays are addressed by 26 functions (34 and 18 operands, one function a gap chunk of the function table): the tavern list builders, the errand board code and the list widget, whose state keeps the array's address.
- V: every builder that stores into the arrays checks the byte offset with an imm32 compare against 0x100 followed by a jump to __report_rangecheckfailure (14 of them, in 13 functions), Errand_BuildActiveList checks the element index against 0x80, and the level-list builder (sub_140375AD0) compares with r12 = 0x100, the same register that forms its bank-30 text reference.
- V (emulation of the pristine code): the entry page reads row 67 (0xFFFF) into variable 39 as 65535 and EventChain_Find misses; no retail script writes variable 430 with the arithmetic opcodes (I: byte pattern of opcodes 0xB0..0xBE over the 560 retail scripts, which find every plain variable 444..507 set once with 0xBE then 0xB0 1) and no exe instruction loads 430 as an EventVar_Write argument, so the entry is never listed in the retail game.
- I: the entry page also shows the text reference 0x8800 plus the index (bank 17), so an entry has a message in bank 29 (its label) and one in bank 17 (its page).
- V: the list widget keeps a signed 16-bit cursor and two 16-bit count fields; the confirm writes event variable 508 = 1 and variable 39 = the event number and starts the event.
- V: the builder's only callers are EventViewer_EntryPage and sub_140375538, both run as tasks of the in-engine task dispatcher sub_140246078 (called from Game_MainLoop).
- V (seen live 2026-11-16, Enhanced mode): a software tracepoint on the builder had 0 hits while the tavern's Rumors list and the main menu's Chronicle > Events list were opened and reopened; both of those screens are built from another source.

## Notes

Earlier readings of 17 special entries (427 to 443) and 61 plain ones (444 to 504) were wrong: the counts are 14 and 64.

## Open questions

? which screen of the Enhanced UI (if any) starts the in-engine tasks that show this list; ? the resource file behind bank 29 (resource slots 10 and 12) and bank 17; ? the events of the other special entries and why they are hidden; ? how the special variables 433 and 440 are set (no retail script writes 427..440 with the arithmetic opcodes).
