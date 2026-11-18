# MusicCommandWordHasEighteenOperandsAndSixOfThemOnlyWriteZeroOrTestNonzero

- **Kind:** observed behaviour
- **Scope:** engine (event command state)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [sub_1402F2500](../functions/sub_1402F2500.md), [EventCmd_ServiceRequests](../functions/EventCmd_ServiceRequests.md), [EventCmd_SetParamBlock](../functions/EventCmd_SetParamBlock.md), [EventCmd_ActivateSlotParam](../functions/EventCmd_ActivateSlotParam.md), [EventCmd_ReleaseSlot](../functions/EventCmd_ReleaseSlot.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 16-bit word at 0x14186246A (the music id and slot of the command state) is addressed by eighteen instructions in seven functions; six of them only clear it or test it for nonzero, twelve read the id or the slot or store a new value.

## Behavior

- V: census of every rip-relative operand into the word: sub_1402F109C at 0x1402F1145 (dword zero), 0x1402F1243 (low byte compared with dil), 0x1402F1265 (word read for the replay id), 0x1402F1283 and 0x1402F12BC (word zero), 0x1402F1298 (word read as the queue parameter); EventCmd_ServiceRequests at 0x1402F17DB (word read, low byte compared with the request) and 0x1402F17F0 (slot byte); sub_1402F2500 at 0x1402F250A (low byte test), 0x1402F2513 (slot byte) and 0x1402F254D (store); EventCmd_SetParamBlock at 0x1402F26E5 (low byte store); EventCmd_ActivateSlotParam at 0x1402F26F6 (word test) and 0x1402F2700 (slot byte); EventCmd_ReleaseSlot at 0x1402F2A98 (word test), 0x1402F2AAD and 0x1402F2AB9 (slot byte) and 0x1402F2AC8 (word zero).
- V: the four slot-byte reads in EventCmd_ServiceRequests, EventCmd_ActivateSlotParam and EventCmd_ReleaseSlot (two) and the one in sub_1402F2500 load the high byte with a sign extension; the word itself is read with a sign extension in three places.
- V: the register that sub_1402F109C compares with the low byte at 0x1402F1243 (dil) is zero there (cleared once at 0x1402F10C6 and not assigned again before the compare).

## Notes

Nothing outside these functions addresses the word; the command state is copied whole (16-byte moves) into the five saved context slots, which is how the word reaches a save.

## Open questions

None recorded.
