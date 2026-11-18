# EventSoundGroup_Play

- **Address:** `0x1402F1868`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventSoundGroup_Play(int group)`
- **Callers:** EventCmd_SelectIndexedSet, sub_1402F109C, EventCmd_ServiceRequests (twice)
- **Callees:** sub_1402B20C0, Sound_PlayNovelSe

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the four sound effects of one event sound group.

## Behavior

- V: calls sub_1402B20C0 first, then builds four ids from row (group - 1) of the sound group table (0x140681D00), each plus 0xE10000.
- V: plays each id minus one through the novel sound player Sound_PlayNovelSe.
- V (2026-11-16): the argument is widened with a sign extension (movsxd) and there is no bound: the row address is table + 4 x group and each voice is the byte at -4 + voice from it, so group 0 reads the four bytes before the table and a group above 56 reads what follows it.
- V (2026-11-16): called with byte 9 of a class 44 command (EventCmd_SelectIndexedSet), with the command state's group word (sub_1402F109C, never above 255), and twice by EventCmd_ServiceRequests with the value of event variable 93 (a 32-bit cell).

## State touched

- Calls: [Sound_PlayNovelSe](Sound_PlayNovelSe.md)

## Referenced by

- Observed behaviours: [EventSoundGroupAndMusicSlotOperandWidths](../behaviors/EventSoundGroupAndMusicSlotOperandWidths.md)
- Reads tables: [EventSoundGroups](../tables/EventSoundGroups.md)

## Notes

Read in full.

## Open questions

?: which stock scripts write event variable 93.
