# EventSoundGroupAndMusicSlotOperandWidths

- **Kind:** observed behaviour
- **Scope:** engine (event sound commands)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [EventSoundGroup_Play](../functions/EventSoundGroup_Play.md), [EventCmd_SelectIndexedSet](../functions/EventCmd_SelectIndexedSet.md), [EventCmd_ServiceRequests](../functions/EventCmd_ServiceRequests.md), [EventCmd_Run](../functions/EventCmd_Run.md), [EventCmd_SetSlotRecord](../functions/EventCmd_SetSlotRecord.md), [MusicSlot_FetchRecord](../functions/MusicSlot_FetchRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The event sound group number reaches the player as a byte of a command record (class 44), as the replay of that byte from a word of the command state, or as the value of event variable 93 (a 32-bit cell); the music slot's sound id is stored in the low byte of a 16-bit word with the slot number in the high byte.

## Behavior

- V: EventSoundGroup_Play widens its int argument with a sign extension and reads the byte at 4 x group - 4 + voice for the four voices, with no bound; group 0 therefore reads the four bytes before the table (in the stock image the high half of a data pointer) and a group above 56 reads whatever follows the table.
- V (2026-11-16): the class 44 command passes byte 9 of its record (0..255) and also stores it in the 16-bit word at 0x141862472 of the command state; the other writers of that word are class 45 (clears it) and class 47 (byte 9 or 0x4000), and the state restore function sub_1402F109C plays the word when it is nonzero unless bit 14 (0x4000) is set, which selects a UI dispatch with the bit removed. So the word never holds a group above 255: it replays the class 44 group.
- V: EventCmd_ServiceRequests plays the value of event variable 93 when it is nonzero (variable 92 goes to another function, variable 94 sets the music slot); EventCmd_Run reads the three variables with EventVar_Read, which returns an unsigned 32-bit value.
- V (2026-11-16): event variables below 128 are whole 32-bit cells (EventVar_Alu stores a full dword for an index below 128; 128..863 are single bits, 864..1023 four-bit nibbles, 1024 and above end the task), so variable 93 can hold any 32-bit number; the ALU's add and multiply let a script build any value from a 16-bit operand. A value of 0x80000000 or more is a negative group after the conversion to int.
- V: the class 32 command passes byte 9 of its record as the music sound id; the recorder stores it as (id or slot shifted left by 8) in a 16-bit word and the id again in a dword array indexed by the slot, so an id above 255 would overwrite the slot byte.
- V: MusicSlot_FetchRecord reads three dwords at 3 x id from the music slot table, with an int id.

## Notes

A group above 255 is started only through event variable 93; the class 44 command, the state word and the UI dispatch carry at most a byte.

## Open questions

? which stock scripts write event variable 93, and whether any uses a group above 56.
